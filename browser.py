from playwright.sync_api import sync_playwright
import json
import os
import time

def run():
    with sync_playwright() as p:
        # 启动无头浏览器
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        context = browser.new_context()

        # 加载登录Cookie
        cookie_str = os.environ.get("MJTD_COOKIES")
        if cookie_str:
            cookies = json.loads(cookie_str)
            context.add_cookies(cookies)
            print("✅ 已加载登录状态")

        # 打开页面
        page = context.new_page()
        page.goto("https://bbs.mjtd.com/")
        print("✅ 页面已打开")

        # 停留15秒
        print("⏳ 停留 15 秒...")
        time.sleep(15)

        # 刷新页面
        print("🔄 刷新页面...")
        page.reload()

        # 刷新后停留2秒
        print("⏳ 刷新后停留 2 秒...")
        time.sleep(2)

        # 关闭
        context.close()
        browser.close()
        print("✅ 任务完成，已关闭")

if __name__ == "__main__":
    run()

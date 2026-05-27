from playwright.sync_api import sync_playwright
import json
import os
import time

def run():
    with sync_playwright() as p:
        # 无头启动浏览器
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        context = browser.new_context()

        # 从 GitHub Secrets 加载登录Cookie
        cookie_str = os.environ.get("MJTD_COOKIES")
        if cookie_str:
            cookies = json.loads(cookie_str)
            context.add_cookies(cookies)
            print("✅ 已加载登录状态")

        # 打开页面
        page = context.new_page()
        page.goto("https://bbs.mjtd.com/")
        print("✅ 页面已打开")

        # ======================
        # 这里停留 5 秒
        # ======================
        print("⏳ 等待5秒后关闭...")
        time.sleep(5)

        # 关闭
        context.close()
        browser.close()
        print("✅ 任务完成，已关闭")

if __name__ == "__main__":
    run()

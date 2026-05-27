from playwright.sync_api import sync_playwright
import json
import os

def run():
    with sync_playwright() as p:
        # 无头启动
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        # 创建上下文
        context = browser.new_context()

        # 从 GitHub Secrets 读取 Cookie
        cookie_str = os.environ.get("MJTD_COOKIES")
        if cookie_str:
            cookies = json.loads(cookie_str)
            context.add_cookies(cookies)
            print("✅ 已加载登录 Cookie")

        # 打开论坛（已登录）
        page = context.new_page()
        page.goto("https://bbs.mjtd.com/")
        page.wait_for_timeout(5000)
        print("✅ 页面打开成功，保持登录状态")

        context.close()
        browser.close()

if __name__ == "__main__":
    run()

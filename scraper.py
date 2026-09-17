from playwright.sync_api import sync_playwright, TimeoutError


def get_page_html(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()

            page.goto(url, wait_until="domcontentloaded", timeout=30000)

            html = page.content()

            browser.close()

            return html

    except TimeoutError:
        print("ERROR: Website took too long to load.")
        return ""

    except Exception as e:
        print(f"ERROR: Could not collect website data: {e}")
        return ""


if __name__ == "__main__":
    html = get_page_html("https://example.com")

    if html:
        print("HTML successfully collected!")
        print("HTML length:", len(html))
    else:
        print("HTML collection failed.")
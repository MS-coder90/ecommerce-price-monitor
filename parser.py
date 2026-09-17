from bs4 import BeautifulSoup


def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")

    products = []

    for item in soup.select(".thumbnail"):
        title = item.select_one(".title")
        price = item.select_one(".price")

        product = {
            "title": title.get("title", "").strip() if title else "",
            "price": price.get_text(strip=True) if price else "",
            "product_id": item.get("data-product-id", "")
        }

        products.append(product)

    return products
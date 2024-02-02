from markdownify import markdownify
import requests
from bs4 import BeautifulSoup

# ここでknowledgeのURLと全記事数（大まかで良い）を指定
base_url: str = "https://XXX/open.knowledge/view/"
n_articles: int = 50

for i in range(1, n_articles + 1):
    response: requests.Response = requests.get(base_url + str(i), verify=False)
    if response.status_code != 200:
        print(f"ID {i} not found.")
        continue
    print(i, response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")

    # === 記事タイトルの取得
    page_title: str = soup.select_one("#content_head > div > h4").get_text(
        separator=" ", strip=True
    )

    # === 記事本文を取得してmarkdown形式に変換
    page_html_content: str = str(soup.select_one("#content"))
    page_md_content: str = markdownify(page_html_content, heading_style="ATX")

    # === コメントの取得
    page_html_comments: list[str] = [
        str(comment).replace("\n", "")
        for comment in soup.select(".question_Box > div.markdown")
    ]
    page_md_comments: list[str] = [
        markdownify(comment, heading_style="ATX") for comment in page_html_comments
    ]

    # === 全部出力する
    print(page_title)
    print(page_md_content)
    if len(page_html_comments) == 0:
        continue
    print("===\n## コメント\n")
    _ = [print(comment + "\n---\n") for comment in page_md_comments]

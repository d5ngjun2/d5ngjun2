import feedparser, time, re

URL = "https://nikihwangg.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = ""
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = feed['published_parsed']
    markdown_text += f"📝 [{time.strftime('%Y/%m/%d', feed_date)}] - **[{feed['title']}]({feed['link']})**  <br/>\n"

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!--START_SECTION:blog-->.*<!--END_SECTION:blog-->",
    f"<!--START_SECTION:blog-->\n{markdown_text}<!--END_SECTION:blog-->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

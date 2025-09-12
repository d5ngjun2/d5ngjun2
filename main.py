import feedparser, time, re

URL = "https://nikihwangg.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# 1. 최신 글 마크다운 생성
markdown_text = ""
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = feed['published_parsed']
    markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

# 2. 기존 README 읽기
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 3. 블로그 섹션만 교체
content = re.sub(
    r"<!--START_SECTION:blog-->.*<!--END_SECTION:blog-->",
    f"<!--START_SECTION:blog-->\n{markdown_text}<!--END_SECTION:blog-->",
    content,
    flags=re.DOTALL
)

# 4. 다시 README에 쓰기
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

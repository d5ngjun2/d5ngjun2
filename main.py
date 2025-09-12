import feedparser
import time
import re

# 1️⃣ RSS 설정
URL = "https://nikihwangg.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# 2️⃣ 최신 글 마크다운 생성
markdown_text = ""
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = feed['published_parsed']
    markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

# 3️⃣ 기존 README 읽기
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# 4️⃣ 블로그 섹션만 교체
new_content = re.sub(
    r"<!--START_SECTION:blog-->.*<!--END_SECTION:blog-->",
    f"<!--START_SECTION:blog-->\n{markdown_text}<!--END_SECTION:blog-->",
    content,
    flags=re.DOTALL
)

# 5️⃣ 다시 README에 쓰기 (덮어쓰기지만 기존 내용은 그대로)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

print("✅ README.md 블로그 섹션 업데이트 완료")

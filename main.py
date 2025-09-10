import feedparser

# RSS 피드 URL
RSS_URL = "https://nikihwangg.tistory.com/rss"
MAX_POSTS = 5

# README 파일 경로
README_FILE = "README.md"

# RSS 파싱
feed = feedparser.parse(RSS_URL)

# 블로그 글 Markdown 생성
blog_section = "\n### 📝 Latest Blog Posts\n"
for entry in feed.entries[:MAX_POSTS]:
    blog_section += f"- [{entry.title}]({entry.link})\n"

# README 기존 내용 읽기
with open(README_FILE, "r", encoding="utf-8") as f:
    content = f.read()

# "Latest Blog Posts" 섹션 이전 내용 삭제 후 새로 삽입
import re
new_content = re.sub(r'### 📝 Latest Blog Posts\n(.|\n)*', '', content)
new_content += blog_section

# README 업데이트
with open(README_FILE, "w", encoding="utf-8") as f:
    f.write(new_content)

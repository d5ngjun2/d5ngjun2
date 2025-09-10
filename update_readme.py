import feedparser
from datetime import datetime
import subprocess

RSS_URL = "https://nikihwangg.tistory.com/rss"
README_PATH = "README.md"
POSTS_COUNT = 5

# RSS 읽기
feed = feedparser.parse(RSS_URL, request_headers={'User-Agent': 'Mozilla/5.0'})
if not feed.entries:
    print("RSS feed가 비어있습니다.")
    exit(0)

posts_md = []
for entry in feed.entries[:POSTS_COUNT]:
    title = entry.title
    link = entry.link
    pub_date = datetime(*entry.published_parsed[:6]).strftime("%Y년 %m월 %d일")
    posts_md.append(f"- [{title}]({link}) <br> <small>{pub_date}</small>")

posts_md_str = "\n".join(posts_md)

# README 업데이트
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

start_tag = "<!-- BLOG_START -->"
end_tag = "<!-- BLOG_END -->"

if start_tag in content and end_tag in content:
    before = content.split(start_tag)[0] + start_tag + "\n"
    after = content.split(end_tag)[1]
    new_content = before + posts_md_str + "\n" + end_tag + after
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

# Git 커밋 & 푸시
subprocess.run(["git", "config", "user.name", "GitHub Actions"], check=True)
subprocess.run(["git", "config", "user.email", "actions@github.com"], check=True)
subprocess.run(["git", "add", README_PATH], check=True)
subprocess.run(["git", "commit", "-m", "Update README with latest blog posts", "--allow-empty"], check=True)
subprocess.run(["git", "pull", "--rebase"], check=False)
subprocess.run(["git", "push"], check=False)

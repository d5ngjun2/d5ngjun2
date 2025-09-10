import feedparser
import time
URL="https://nikihwangg.tistory.com/rss" # URL = "내블로그 주소/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

# 기본적으로 바뀌지 않을 Markdown text 입력
markdown_text = """
<div class='blog' align='left'>
  <h2> 📖 BLOG 📖 </h2>

[![Tistory's Badge](https://github-readme-tistory-card.vercel.app/api/badge?name=동준`s블로그&theme=kakao)](https://nikihwangg.tistory.com)

</div>
<hr>
<div class='tech-stack' align='left'>
  <h2> 📚 TECH STACK 🛠 </h2>
  <span stye="">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">&nbsp
  <img src="https://img.shields.io/badge/amazonaws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white">&nbsp
  </span>
<hr>

## ✅ Latest Tistory Posting<div class=blog-post text-align='left'>
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']})\n"
markdown_text +=  """
</div>
</div>
"""
print(markdown_text)
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()

from news_api import fetch_news
from summarizer import summarize_text

def main():
  print("===News Summarizer===")
  topic = input("Enter a topic : ")

  articles = fetch_news(topic)

  if not articles:
    print("No articles found.")
    return
  
  for i, article in enumerate(articles, 1):
    print(f"\n--- Article{i} ---")
    print("Original:", article[:300],"...")
    summary = summarize_text(article)
    print("Summary:", summary)


if __name__ == "__main__" :
  main()



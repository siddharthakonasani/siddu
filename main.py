import re
import sys
import praw
import os
import json
from dotenv import load_dotenv

# --- Load environment variables from .env file ---
load_dotenv()

# --- Reddit API credentials ---
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_SECRET = os.getenv('REDDIT_SECRET')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

# --- Step 1: Extract username from Reddit profile URL ---
def extract_username(url: str) -> str:
    match = re.match(r'https?://(www\.)?reddit\.com/user/([^/]+)/?', url)
    if not match:
        raise ValueError("Invalid Reddit user URL format.")
    return match.group(2)

def get_input_url():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter Reddit profile URL: ").strip()
    return extract_username(url)

# --- Step 2: Connect to Reddit and fetch posts/comments ---
def get_reddit_instance():
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    return reddit

def fetch_user_content(username: str, limit=100):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "text": submission.selftext,
                "url": submission.url,
                "permalink": f"https://www.reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"Error fetching posts: {e}")

    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "text": comment.body,
                "link": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")

    return posts, comments

# --- Step 3: Clean and preprocess text content ---
def clean_text(text):
    text = re.sub(r'http\S+', '', text)             # Remove URLs
    text = re.sub(r'\s+', ' ', text).strip()        # Collapse whitespace
    text = re.sub(r'[\*_>`]', '', text)             # Remove markdown
    return text

def preprocess(posts, comments):
    cleaned_posts = []
    cleaned_comments = []

    for post in posts:
        cleaned = {
            "title": clean_text(post["title"]),
            "text": clean_text(post["text"]),
            "link": post["permalink"]
        }
        cleaned_posts.append(cleaned)

    for comment in comments:
        cleaned = {
            "text": clean_text(comment["text"]),
            "link": comment["link"]
        }
        cleaned_comments.append(cleaned)

    return cleaned_posts, cleaned_comments

# --- Main program ---
if __name__ == "__main__":
    try:
        username = get_input_url()  # This extracts from the URL directly
        print(f"\nExtracted username: {username}")

        posts, comments = fetch_user_content(username)
        print(f"Fetched {len(posts)} posts and {len(comments)} comments.")

        cleaned_posts, cleaned_comments = preprocess(posts, comments)
        print(f"Cleaned {len(cleaned_posts)} posts and {len(cleaned_comments)} comments.")

        # Save cleaned output to JSON
        output_path = f"{username}_cleaned.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({
                "posts": cleaned_posts,
                "comments": cleaned_comments
            }, f, indent=2)

        print(f"\nCleaned data saved to '{output_path}'\n")

    except Exception as e:
        print(f"Error: {e}")



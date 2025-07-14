import json

# Load cleaned Reddit content from JSON file
FILENAME = "Hungry-Move-6603_cleaned.json"  # Change if needed

with open(FILENAME, "r", encoding="utf-8") as f:
    data = json.load(f)

posts = data["posts"]
comments = data["comments"]

# Print first 10 posts
print("\n--- Sample Cleaned Posts (10) ---")
for i, post in enumerate(posts[:10], 1):
    print(f"\nPOST #{i}")
    print(f"Title: {post['title']}")
    print(f"Text: {post['text']}")
    print(f"Link: {post['link']}")

# Print first 10 comments
print("\n--- Sample Cleaned Comments (10) ---")
for i, comment in enumerate(comments[:10], 1):
    print(f"\nCOMMENT #{i}")
    print(f"Text: {comment['text']}")
    print(f"Link: {comment['link']}")

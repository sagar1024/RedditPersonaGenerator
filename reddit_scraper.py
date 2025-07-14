import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

def create_reddit_client():
    return praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

def scrape_user_data(username, post_limit=50, comment_limit=50):
    reddit = create_reddit_client()
    user = reddit.redditor(username)

    posts, comments = [], []

    try:
        for submission in user.submissions.new(limit=post_limit):
            posts.append({
                "title": submission.title,
                "text": submission.selftext,
                "url": f"https://reddit.com{submission.permalink}"
            })
    except Exception as e:
        print(f"Error fetching posts: {e}")

    try:
        for comment in user.comments.new(limit=comment_limit):
            comments.append({
                "text": comment.body,
                "url": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching comments: {e}")

    return {"posts": posts, "comments": comments}

import praw

reddit = praw.Reddit(
    client_id="eHPmqGqJ3ekZRSivWxyY8A",
    client_secret="iCvKYuy_3Z3jejZ1r-0tKtozG3xAKA",
    user_agent="python:boterator-anna:0.0.1 (by u/roguetroll)",
    username="boterator-anna",
    password="xax3IudcTOEnDZ7%vekDR84M",
)

reddit.readonly = True

subreddit = reddit.subreddit("faces")

for submission in subreddit.hot(limit=20):
    print(submission.title)
    print(submission.author)
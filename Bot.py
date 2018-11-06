import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('pythonforengineers')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# loops through top five submissions in "hot"
for submission in subreddit.hot(limit=5):
    # ensures that this post hasn't been replied to already
    if submission.id not in posts_replied_to:
        # checks title of current post to see if phrase is present
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Testy bot says: Me too!!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for post_id in posts_replied_to:
                    f.write(post_id + "\n")

# writes the code for posts that bot replied to in a txt file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

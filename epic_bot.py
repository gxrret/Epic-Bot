import praw
import config
import time
import os

def bot_login():
    print("Logging in...")
    # Create a Reddit instance
    r = praw.Reddit(username = config.username,
                    password = config.password,
                    client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = "name of bot + version + by /u/USERNAME")
    print("Logged in!")
    return r

def run_bot(r, comments_replied_to):
    print("Searching last x comments")

    for comment in r.subreddit('SUBREDDIT_GOES_HERE').comments(limit=x): #You should change the limit to something low, Reddit will detect the rate limit.
        if "fortnite" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("String with \"TEXT_YOU_WANT_TO_DETECT\" found in comment " + comment.id)
            comment.reply("REPLY")
            print("Replied to comment " + comment.id)    
        comments_replied_to = list(comments_replied_to)
        comments_replied_to.append(comment.id)

        with open ("comments_replied_to.txt", "a") as f:
            f.write(comment.id + "\n") # This adds the scraped comment to the txt file

    print("Search completed")

    print(comments_replied_to)
    print("Sleeping for 10 seconds...")

    #Sleep for 30 seconds
    time.sleep(30)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []

    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)
                  
                    
          

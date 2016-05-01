import praw
import re
import json
import time
import random

THREAD = "https://www.reddit.com/r/counting/comments/4h5wqh/1114k_counting_thread/"
CONSTANTLOOP = True
MIN_SLEEP = 10
MAX_SLEEP = 20



def convert_comment_to_num(comment):
    stringForm = re.search(r"[0-9, ]+", comment).group()
    stringForm = stringForm.replace(",", "")
    stringForm = stringForm.replace(" ", "")
    return int(stringForm)

def get_next_number(comment):
    currentNum = convert_comment_to_num(comment)
    nextNum = currentNum + 1
    return format(nextNum, ",d")


def main():
    with open("settings.txt") as file:
        settings = json.loads(file.read())


    r = praw.Reddit(user_agent="counter v1")
    r.login(settings['username'], settings['password'], disable_warning=True)

    newComments = r.get_comments("counting")
    numbersList = []

    #generate the list of all the comments in the specific thread
    for comment in newComments:
        if comment.link_url == THREAD:
            numberForm = convert_comment_to_num(comment.body)
            numbersList.append(comment)

    #sort the list by how big the number is
    numbersList = sorted(numbersList, key=lambda x: convert_comment_to_num(x.body), reverse=True)

    #the biggest comment is the first one
    maxComment = numbersList[0]

    maxCommentAuthor = maxComment.author.name
    myUserName = r.user.name

    #make sure i'm not the author of the biggest comment
    if maxCommentAuthor != myUserName:
        #get the next number after the biggest comment
        nextNumber = get_next_number(maxComment.body)

        #reply and upvote
        print("replying to", maxComment.body, "with", nextNumber)
        print(THREAD + maxComment.id)
        maxComment.reply(get_next_number(maxComment.body))
        maxComment.upvote()
    else:
        print("I am currently the author of the highest comment")



if __name__ == "__main__":
    if CONSTANTLOOP:
        while True:
            main()
            sleepTime = random.randint(MIN_SLEEP, MAX_SLEEP)
            print("sleeping for", sleepTime, "seconds")
            time.sleep(sleepTime)
    else:
        main()
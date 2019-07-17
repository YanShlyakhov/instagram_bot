# -*- coding: utf-8 -*-

def clear_comment(comment):
    try:
        text = comment.split(" ")
        #print(text)
        response = ""
        for t in text:
            if(len(t) == 0):
                continue
            if(t[0] != '@'):
                response += str(t) + " "
        return response
    except:
        print("ERROR")
        return ""

def is_comment_spam(comment):
    spam_filter = set(",.!acehikmnopuxyABCEHKMOPTUX")
    comment = comment.split(" ")
    is_spam = False
    for com in comment:
        if len(list( set(com[1:-1]) & set(spam_filter))) > 0:
            is_spam = True
    return is_spam

filter_list = open("stop.txt", "r").read().split(", ")

comments_list = open("for_markov.txt", "r").read().split("\n")

new_comments = open("kek.txt", "w")

response = ""

for comment in comments_list:

    comment = clear_comment(comment)

    if (is_comment_spam(comment)):
        print(comment)
        continue

    comment_array = comment.split(' ')
    c = list(set(comment_array) & set(filter_list))
    if (len(c) == 0):
        new_comments.write(str(comment))
        new_comments.write("\n")
    else:
        print(comment)

#print(filter_list)
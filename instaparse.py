from instagram import Account, Media, WebAgent, AsyncWebAgent, Comment
import pandas as pd
import re
import requests
import dataset

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#import Model

f = open("for_markov.txt", "w")
db = dataset.connect('sqlite:///texts_for_nn')

table = db.create_table('analyzed')

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    return str(score)

agent = WebAgent()

xl = pd.ExcelFile("for_ns.xlsx")
print(xl.sheet_names)
df = xl.parse("Sheet1")

users_to_parse = []

for s in df["Username"]:
    users_to_parse.append("@"+str(s))

def get_users_from_post(post_text):
    try:
        global users_to_parse
        text = post_text.split(" ")
        #print(text)
        for t in text:
            if(len(t) == 0):
                continue
            if(t[0] == '@'):
                if not (t in users_to_parse):
                    users_to_parse.append(t)
    except:
        print("Bad post")

def clear_comment(comment):
    try:
        text = post_text.split(" ")
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

def comments(post):
    url = 'https://www.instagram.com/p/'+str(post)+'/?__a=1'
    resp = requests.get(url=url)
    data = resp.json()
    response = []
    try:
        for comm in data['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']:
            comment = comm['node']['text']
            comment = clear_comment(comment)
            if(len(comment) > 5):
                score = sentiment_analyzer_scores(comment)
                comment_array = comment.split(' ')
                c = list(set(comment_array) & set(stop_words))
                if (len(c) == 0):
                    f.write(str(comment))
                    f.write("\n")
                    print(cur_result)
                cur_result = {'text':comment, 'sentiment':score}
                
                response.append(cur_result)
    except:
        print("No comments")
    return response

def get_user_media(name):
    try:
        account = Account(name)

        media1, pointer = agent.get_media(account)
        for m in media1:
            media = Media(m)
            print(media.caption)
            res = comments(media)
            try:
                table.insert(dict(text = str(media.caption), vect = str(), results = str(res)))
            except:
                print("No media caption")
        
    except:
        print("Error")

i = 0
for name in users_to_parse:
    i+=1
    if(i==1):
        continue
    print(str(i)+"/"+str(len(users_to_parse)))
    name = str(name)[1:]
    print(name)
    get_user_media(name)
    if(i > 1000):
        break


"""
agent = WebAgent()
account = Account("Miley Cyrus")

media1, pointer = agent.get_media(account)
media2, pointer = agent.get_media(account, pointer=pointer, count=50, delay=1)

for m in media1:
    media = Media(m)
    print(media.caption)
    media.comments
"""
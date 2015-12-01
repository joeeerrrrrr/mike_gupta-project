
#from bs4 import BeautifulSoup
#import html5lib
import json, urllib2
#import re
#import pydot
#import itertools
#import time
#import ast
import csv

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd


DEVELOPER_KEY = "AIzaSyAgiuJaqOqrsrFIfIdp3S17urARba7MHvo"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)


query = raw_input("\n Enter your query: ")
argparser.add_argument("--q", help="Search term", default=query) #change the default to the search term you want to search
argparser.add_argument("--max-results", help="Max results", default=50) #default number of results which are returned. It can vary from 0 - 100
options = argparser.parse_args()

search_response = youtube.search().list( # Call the search.list method to retrieve results matching the specified query term.
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results
    ).execute()

page_tokens = {}

page_tokens['p2'] = (search_response['nextPageToken'])

search_response2 = youtube.search().list( # Call the search.list method to retrieve results matching the specified query term.
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results,
    pageToken = page_tokens['p2']
    ).execute()

page_tokens['p3'] = search_response2['nextPageToken']

search_response3 = youtube.search().list( # Call the search.list method to retrieve results matching the specified query term.
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results,
    pageToken = page_tokens['p3']
    ).execute()

page_tokens['p4'] = search_response3['nextPageToken']

search_response4 = youtube.search().list( # Call the search.list method to retrieve results matching the specified query term.
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results,
    pageToken = page_tokens['p4']
    ).execute()

page_tokens['p5'] = search_response4['nextPageToken']

search_response5 = youtube.search().list( # Call the search.list method to retrieve results matching the specified query term.
    q=options.q,
    type="video",
    part="id,snippet",
    maxResults=options.max_results,
    pageToken = page_tokens['p5']
    ).execute()

print search_response
print search_response2
print search_response3
print search_response4
print search_response5

videos = {} # Add each result to the appropriate list, and then display the lists of matching videos. Filter out channels, and playlists.

res = []

for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video": #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
        #print "Videos:\n", "\n".join(videos), "\n"
        s = ','.join(videos.keys())

        videos_list_response = youtube.videos().list(
        id=s,
        part='id,statistics,snippet'
        ).execute()

        #print videos_list_response['items']

        for i in videos_list_response['items']:
            temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
            temp_res.update(i['statistics'])
            temp_res.update(i['snippet'])

            res.append(temp_res)
        # dislikes = i['statistics']['dislikeCount']
        # likes = i['statistics']['likeCount']
        # reputability = int(likes) / int(dislikes)
        # if reputability >= 0.7:

for search_result in search_response2.get("items", []):
    if search_result["id"]["kind"] == "youtube#searchListResponse": #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
        #print "Videos:\n", "\n".join(videos), "\n"
        s = ','.join(videos.keys())

        videos_list_response = youtube.videos().list(
        id=s,
        part='id,statistics,snippet'
        ).execute()
        #print videos_list_response['items']

        for i in videos_list_response['items']:
            temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
            temp_res.update(i['statistics'])
            temp_res.update(i['snippet'])

            res.append(temp_res)

for search_result in search_response3.get("items", []):
    if search_result["id"]["kind"] == "youtube#searchListResponse": #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
        #print "Videos:\n", "\n".join(videos), "\n"
        s = ','.join(videos.keys())

        videos_list_response = youtube.videos().list(
        id=s,
        part='id,statistics,snippet'
        ).execute()

        #print videos_list_response['items']

        for i in videos_list_response['items']:
            temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
            temp_res.update(i['statistics'])
            temp_res.update(i['snippet'])

            res.append(temp_res)

for search_result in search_response4.get("items", []):
    if search_result["id"]["kind"] == "youtube#searchListResponse": #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
        #print "Videos:\n", "\n".join(videos), "\n"
        s = ','.join(videos.keys())

        videos_list_response = youtube.videos().list(
        id=s,
        part='id,statistics,snippet'
        ).execute()

        #print videos_list_response['items']

        for i in videos_list_response['items']:
            temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
            temp_res.update(i['statistics'])
            temp_res.update(i['snippet'])

            res.append(temp_res)

for search_result in search_response5.get("items", []):
    if search_result["id"]["kind"] == "youtube#searchListResponse": #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
        #print "Videos:\n", "\n".join(videos), "\n"
        s = ','.join(videos.keys())

        videos_list_response = youtube.videos().list(
        id=s,
        part='id,statistics,snippet'
        ).execute()

        #print videos_list_response['items']

        for i in videos_list_response['items']:
            temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
            temp_res.update(i['statistics'])
            temp_res.update(i['snippet'])

            res.append(temp_res)


df = pd.DataFrame.from_dict(res)


df.to_csv('testing.csv', encoding='utf-8')

print df


def display(res):
    for x in res:
        print "=========="
        print "title: " + x['v_title'].encode('ascii', 'ignore').decode('ascii')
        print "description: " + x['description'].encode('ascii', 'ignore').decode('ascii')
        print "dislike count: " + str(x['dislikeCount'].encode('ascii', 'ignore').decode('ascii'))
        print "like count: " + str(x['likeCount'].encode('ascii', 'ignore').decode('ascii'))
        print "comment count: " + str(x['commentCount'].encode('ascii', 'ignore').decode('ascii'))
        # if 'tags' in x.keys():
        #     print "tags: " + x['tags']
        print "timestamp: " + x['publishedAt'].encode('ascii', 'ignore').decode('ascii')
        print "=========="


#display(res)


"""Python function to get latest YouTube video's metadata to post a tweet"""

import re
import os
import json
import html
import urllib.request
import tweepy
from googleapiclient.discovery import build


# Load the credentials
with open('config.json') as config_file:
    data = json.load(config_file)
    youtube_channel_id = data['youtube_channel_id']
    api_key = data['youtube_API_key']
    twitter_API_Key = data['twitter_API_Key']
    twitter_secret_key = data['twitter_secret_key']
    twitter_access_token = data['twitter_access_token']
    twitter_access_token_secret = data['twitter_access_token_secret']

# Get latest video's meta data
with build('youtube', 'v3', developerKey=api_key) as service:
    request = service.search().list(
        part='snippet',
        channelId=youtube_channel_id,
        maxResults=1,
        order='date',
        type='video'
    )
    response = request.execute()

    title = html.unescape(response['items'][0]['snippet']['title'])
    video_id = response['items'][0]['id']['videoId']
    video_url = f"https://youtu.be/{video_id}"

    # Get high res thumbnail and full description
    request = service.videos().list(
        part='snippet',
        id=video_id,
    )
    response = request.execute()

    description = response['items'][0]['snippet']['description']
    thumbnail = response['items'][0]['snippet']['thumbnails']['maxres']['url']

    # hashtags are a part of the last line in the description
    hashtags = re.split("\n", description)[-1]
    hashtags = hashtags.split(" ")
    hashtags = list(filter(None, hashtags))  # Remove any empty hashtags
    hashtags = hashtags[:10]  # Get only first 10 since twitter's char limit
    hashtags = ' '.join(hashtags)

# Save image locally to tweet
try:
    urllib.request.urlretrieve(thumbnail, "tweet.jpg")
except urllib.error.HTTPError as exp:
    print(f"Error: {exp}")
except Exception as exp:
    print(f"Error: {exp}")


# Authenticate to Twitter
auth = tweepy.OAuthHandler(twitter_API_Key, twitter_secret_key)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

# Create API object
api = tweepy.API(auth)

# Custom status message
status = f"{title}\n\nNew Video out now! \n\n{video_url} \n\n{hashtags}"

# Create a tweet and handle any exceptions

try:
    api.update_with_media(filename="tweet.jpg", status=status)
except Exception as exp:
    print(f"Error: {exp}")
finally:
    os.remove("tweet.jpg")

# Automate social media posts

### The background

A part of our workflow at [Abandoned Hope](https://www.youtube.com/channel/UChoxnoqR1SlHHqsnu4A--eg) is:

1. Post YouTube video with custom thumbnail, video title and description
2. Share this on all social media (Twitter, Facebook and IGTV) manually

This takes our certain time which can be automated without errors which we often commit while copy pasting cross platforms. This inspired me to write this script to automate (at least) Twitter's part for now.

### How this works

Using YouTube's API calls, this will fetch metadata from the latest video including video title, high-res thumbnail and the description and post a tweet with a picture and link to YouTube's video. In our videos, we separate the last line of the video description as the hashtags (as most of us) making it easier to scrape them using regex: ```hashtags = re.split("\n", description)[-1]```

### Pre-reqs

1. Google developer account with API keys
2. Twitter developer account with API keys


### Installation

1. [The Google APIs Client Library for Python](https://developers.google.com/youtube/v3/quickstart/python):
```shell
pip install --upgrade google-api-python-client
pip install --upgrade google-auth-oauthlib google-auth-httplib2
```
2. [Tweepy API](http://docs.tweepy.org/en/latest/index.html) for twitter:
```shell
pip install tweepy
```
3. Clone this repo:
```shell
git clone https://github.com/shreyasgaonkar/social-media-posts.git
```
4. Rename ```config.sample.json``` to ```config.json```
5. Update config.json with your developer keys from Twitter and YouTube:
```json
{
    "youtube_API_key": "XXXX",
    "twitter_API_Key": "XXXX",
    "twitter_secret_key": "XXXX",
    "twitter_bearer_token": "XXXX",
    "twitter_access_token": "XXXX",
    "twitter_access_token_secret": "XXXX"
}
```
6. Run ```python app.py``` to post thumbail image from your latest video

### Customize tweet

Replace this section from ```app.py``` to what fits your use-case and Twitter's character count:
```python
# Custom status message
status = f"{title}\n\nNew Video out now! \n\n {video_url} \n\n {hashtags}"
```

### Output:

![Sample Tweet](/images/twitter.jpg)

## Missing Info / Bugs

- :cold_sweat: Something broken? [Open an issue](https://github.com/shreyasgaonkar/social-media-posts/issues) with additional context and I'll try to fix it. Screenshots help!

- More additional services/use-cases, [open a new issue](https://github.com/shreyasgaonkar/social-media-posts/issues)

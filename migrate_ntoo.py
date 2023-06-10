import json 
import csv

csv_file_path = "tweets.csv"
file_path = "fullTweetsData.json"
fieldnames = ["username","text","url"]

def extract_tweet_data(tweet):
    try:
        
        # Extract text
        text = tweet['retweeted_status']['extended_tweet']['full_text'] 
        # Extract URL
        url = None
        entities = tweet['retweeted_status'].get('entities', {})
        urls = entities.get('urls', [])
        if len(urls) > 0:
            url = urls[0]['expanded_url']
        
        # Extract username
        username = tweet['retweeted_status']['user']['screen_name']
        
        return text, url, username
    
    except (KeyError, IndexError, json.JSONDecodeError):
        return None, None, None

# Example JSON string of a tweet
tweet_json = '''
{
    "created_at": "Sat Jul 25 22:47:40 +0000 2020",
    "id": 1287157598085513216,
    "id_str": "1287157598085513216",
    "text": "RT @RickAndRollBaby: I don’t wanna talk about the details of how I was arrested, due to legal reasons. But I feel it’s important to share t…",
    "source": "<a href=\\"https://mobile.twitter.com\\" rel=\\"nofollow\\">Twitter Web App</a>",
    "truncated": false,
    "in_reply_to_status_id": null,
    "in_reply_to_status_id_str": null,
    "in_reply_to_user_id": null,
    "in_reply_to_user_id_str": null,
    "in_reply_to_screen_name": null,
    "user": {
        "id": 1274978511342592000,
        "id_str": "1274978511342592000",
        "name": "NotTheOnlyOne.org",
        "screen_name": "NTOO_Org",
        "location": null,
        "url": "http://nottheonlyone.org",
        "description": "Capturing, curating and sharing stories and data about racism",
        "translator_type": "none",
        "protected": false,
        "verified": false,
        "followers_count": 21,
        "friends_count": 45,
        "listed_count": 0,
        "favourites_count": 2111,
        "statuses_count": 2398,
        "created_at": "Mon Jun 22 08:12:33 +0000 2020",
        "utc_offset": null,
        "time_zone": null,
        "geo_enabled": false,
        "lang": null,
        "contributors_enabled": false,
        "is_translator": false,
        "profile_background_color": "F5F8FA",
        "profile_background_image_url": "",
        "profile_background_image_url_https": "",
        "profile_background_tile": false,
        "profile_link_color": "1DA1F2",
        "profile_sidebar_border_color": "C0DEED",
        "profile_sidebar_fill_color": "DDEEF6",
        "profile_text_color": "333333",
        "profile_use_background_image": true,
        "profile_image_url": "http://pbs.twimg.com/profile_images/1275016997319798784/AzXQDID6_normal.jpg",
        "profile_image_url_https": "https://pbs.twimg.com/profile_images/1275016997319798784/AzXQDID6_normal.jpg",
        "profile_banner_url": "https://pbs.twimg.com/profile_banners/1274978511342592000/1592822655",
        "default_profile": true,
        "default_profile_image": false,
        "following": null,
        "follow_request_sent": null,
        "notifications": null
    },
    "geo": null,
    "coordinates": null,
    "place": null,
    "contributors": null,
    "retweeted_status": {
        "created_at": "Sat Jul 18 23:49:59 +0000 2020",
        "id": 1284636567076831232,
        "id_str": "1284636567076831232",
        "text": "I don’t wanna talk about the details of how I was arrested, due to legal reasons. But I feel it’s important to shar… https://t.co/CMG20YkvnG",
        "source": "<a href=\\"http://twitter.com/download/iphone\\" rel=\\"nofollow\\">Twitter for iPhone</a>",
        "truncated": true,
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "in_reply_to_screen_name": null,
        "user": {
            "id": 1267482620671164416,
            "id_str": "1267482620671164416",
            "name": "Himbos for Abolition",
            "screen_name": "RickAndRollBaby",
            "location": "Chicago, IL",
            "url": "https://www.gofundme.com/f/DisplacedBlackYouthInChicago",
            "description": "#BlackTransLivesMatter #CPACNow. he/him :)) #JusticeForMiracle donate to her Cash app: $yunvmimi. & Support Displaced Black Youth to get housing, link below!",
            "translator_type": "none",
            "protected": false,
            "verified": false,
            "followers_count": 1496,
            "friends_count": 195,
            "listed_count": 2,
            "favourites_count": 1632,
            "statuses_count": 899,
            "created_at": "Mon Jun 01 15:46:49 +0000 2020",
            "utc_offset": null,
            "time_zone": null,
            "geo_enabled": false,
            "lang": null,
            "contributors_enabled": false,
            "is_translator": false,
            "profile_background_color": "F5F8FA",
            "profile_background_image_url": "",
            "profile_background_image_url_https": "",
            "profile_background_tile": false,
            "profile_link_color": "1DA1F2",
            "profile_sidebar_border_color": "C0DEED",
            "profile_sidebar_fill_color": "DDEEF6",
            "profile_text_color": "333333",
            "profile_use_background_image": true,
            "profile_image_url": "http://pbs.twimg.com/profile_images/1283531617932390401/gijzqHiT_normal.jpg",
            "profile_image_url_https": "https://pbs.twimg.com/profile_images/1283531617932390401/gijzqHiT_normal.jpg",
            "profile_banner_url": "https://pbs.twimg.com/profile_banners/1267482620671164416/1595186631",
            "default_profile": true,
            "default_profile_image": false,
            "following": null,
            "follow_request_sent": null,
            "notifications": null
        },
        "geo": null,
        "coordinates": null,
        "place": null,
        "contributors": null,
        "is_quote_status": false,
        "extended_tweet": {
            "full_text": "I don’t wanna talk about the details of how I was arrested, due to legal reasons. But I feel it’s important to share that I’m safe, free, and happy, and that the arrest didn’t result in any charges being made. The process was terrifying, and the effects of the traumas...",
            "display_text_range": [
                0,
                284
            ],
            "entities": {
                "hashtags": [],
                "urls": [],
                "user_mentions": [],
                "symbols": []
            }
        },
        "quote_count": 0,
        "reply_count": 0,
        "retweet_count": 7,
        "favorite_count": 64,
        "entities": {
            "hashtags": [],
            "urls": [
                {
                    "url": "https://t.co/CMG20YkvnG",
                    "expanded_url": "https://twitter.com/i/web/status/1284636567076831232",
                    "display_url": "twitter.com/i/web/status/1…",
                    "indices": [
                        117,
                        140
                    ]
                }
            ],
            "user_mentions": [],
            "symbols": []
        },
        "favorited": false,
        "retweeted": false,
        "possibly_sensitive": false,
        "filter_level": "low",
        "lang": "en"
    },
    "is_quote_status": false,
    "quote_count": 0,
    "reply_count": 0,
    "retweet_count": 7,
    "favorite_count": 0,
    "entities": {
        "hashtags": [],
        "urls": [],
        "user_mentions": [
            {
                "screen_name": "RickAndRollBaby",
                "name": "Himbos for Abolition",
                "id": 1267482620671164416,
                "id_str": "1267482620671164416",
                "indices": [
                    3,
                    19
                ]
            }
        ],
        "symbols": []
    },
    "favorited": false,
    "retweeted": false,
    "filter_level": "low",
    "lang": "en",
    "timestamp_ms": "1595722060086"
}
'''


# Load the JSON data from the file
with open(file_path, 'r') as json_file:
    data = json.load(json_file)


csv_data = []

# Now you can work with the loaded data
# For example, you can access individual tweets like this:
for tweet in data:
    # Extract tweet data
    text, url, username = extract_tweet_data(tweet)

	
    csv_data_row = { 
		"text" : text,
		"url" : url,
		"username" : username
	       }

    csv_data.append(csv_data_row)

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(csv_data)

print(len(csv_data))

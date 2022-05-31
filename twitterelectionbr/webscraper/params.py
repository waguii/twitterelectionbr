#Consts

DOWNLOAD_FOLDER = "/home/wagui/code/waguii/twitterelectionbr/raw_data/"

USER_COLUMNS = [
    "username", "displayname", "description", "verified", "created",
    "followers_count", "friends_count", "location", "protected", "profile_img"
]

TWEET_COLUMNS = [
    "url", "date", "content", "id", "reply_count", "retweet_count",
    "like_count", "quote_count", "lang"
]

DF_COLUMNS = TWEET_COLUMNS + USER_COLUMNS

FORMAT_DATETIME = "%Y-%m-%d %H:%M:%S"
FORMAT_DATE = "%Y-%m-%d"

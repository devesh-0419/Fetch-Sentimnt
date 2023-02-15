from googleapiclient.discovery import build


import keys

def FetchCommentsFromYoutube(VideoId):


    Resource = build('youtube', 'v3', developerKey=keys.YoutubeApiKey)

    Request = Resource.commentThreads().list(
    part="snippet", videoId=VideoId, maxResults=120)

    Response = Request.execute()

    for item in Response["items"]:
        item_info = item["snippet"]
        topLevelComment = item_info["topLevelComment"]
        comment_info = topLevelComment["snippet"]
        print("Comment Text:", comment_info["textDisplay"])
        print("Comment Date: ", comment_info['publishedAt'])
        print("\n")

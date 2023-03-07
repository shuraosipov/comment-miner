import os
from googleapiclient.discovery import build

api_key = os.environ["YOUTUBE_API_KEY"]


def get_all_comments(video_id):
    comments = []
    youtube = build("youtube", "v3", developerKey=api_key)

    # First, retrieve the top-level comments for the video
    results = (
        youtube.commentThreads()
        .list(part="snippet", videoId=video_id, textFormat="plainText", maxResults=100)
        .execute()
    )

    # Loop through each comment thread and extract the comment text and replies
    while results:
        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
            # Check if the comment has any replies
            if item["snippet"]["totalReplyCount"] > 0:
                reply_results = (
                    youtube.comments()
                    .list(
                        part="snippet",
                        parentId=item["snippet"]["topLevelComment"]["id"],
                        textFormat="plainText",
                        maxResults=100,
                    )
                    .execute()
                )
                # Loop through each reply and extract the reply text
                for reply_item in reply_results["items"]:
                    reply = reply_item["snippet"]["textDisplay"]
                    comments.append(reply)
        # Check if there are more results to retrieve
        if "nextPageToken" in results:
            results = (
                youtube.commentThreads()
                .list(
                    part="snippet",
                    videoId=video_id,
                    textFormat="plainText",
                    maxResults=100,
                    pageToken=results["nextPageToken"],
                )
                .execute()
            )
        else:
            break
    return comments


# Ginni Rometty: IBM CEO on Leadership, Power, and Adversity | Lex Fridman Podcast #362
video_id = "XiCxj-bXu5M"

comments = get_all_comments(video_id)
print(comments)
print(len(comments))

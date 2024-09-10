import os
import sys
import logging

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import googleapiclient.errors
from config import API_SERVICE_NAME, API_VERSION
from src.auth import get_authenticated_service

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_input():
    old_phrase = input("Enter the phrase you want to replace: ")
    new_phrase = input("Enter the new phrase to replace it with: ")
    return old_phrase, new_phrase

def update_video_titles(youtube, old_phrase, new_phrase):
    try:
        channels_response = youtube.channels().list(
            mine=True,
            part="contentDetails"
        ).execute()

        for channel in channels_response["items"]:
            uploads_list_id = channel["contentDetails"]["relatedPlaylists"]["uploads"]
            
            logging.info(f"Processing videos in list {uploads_list_id}")

            next_page_token = None
            while True:
                playlistitems_response = youtube.playlistItems().list(
                    playlistId=uploads_list_id,
                    part="snippet",
                    maxResults=50,
                    pageToken=next_page_token
                ).execute()

                for playlist_item in playlistitems_response["items"]:
                    title = playlist_item["snippet"]["title"]
                    video_id = playlist_item["snippet"]["resourceId"]["videoId"]
                    
                    if old_phrase.lower() in title.lower():
                        new_title = title.replace(old_phrase, new_phrase)
                        logging.info(f"Updating video title: {title} -> {new_title}")
                        
                        try:
                            # Fetch the video details to get the category ID
                            video_response = youtube.videos().list(
                                part="snippet",
                                id=video_id
                            ).execute()
                            
                            if video_response["items"]:
                                category_id = video_response["items"][0]["snippet"]["categoryId"]
                                
                                youtube.videos().update(
                                    part="snippet",
                                    body={
                                        "id": video_id,
                                        "snippet": {
                                            "title": new_title,
                                            "categoryId": category_id
                                        }
                                    }
                                ).execute()
                                logging.info(f"Successfully updated video: {video_id}")
                            else:
                                logging.warning(f"Could not fetch details for video: {video_id}")
                        except googleapiclient.errors.HttpError as e:
                            logging.error(f"An error occurred while updating video {video_id}: {e}")

                next_page_token = playlistitems_response.get("nextPageToken")
                if not next_page_token:
                    break

    except googleapiclient.errors.HttpError as e:
        logging.error(f"An HTTP error occurred: {e}")

def main():
    youtube = get_authenticated_service()
    old_phrase, new_phrase = get_user_input()
    update_video_titles(youtube, old_phrase, new_phrase)

if __name__ == "__main__":
    main()
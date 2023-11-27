import os
import argparse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Setting up command-line arguments
parser = argparse.ArgumentParser(description='Upload a video to YouTube.')
parser.add_argument('video_file', help='Path to the video file')
parser.add_argument('--title', default='Default Title', help='Title of the video')
parser.add_argument('--description', default='Uploaded by youtube-cli-uploader', help='Description of the video')
parser.add_argument('--category', default='22', help='Category ID of the video')
parser.add_argument('--privacy', default='private', help='Privacy status of the video')

args = parser.parse_args()

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, ["https://www.googleapis.com/auth/youtube.upload"])
    credentials = flow.run_console()
    youtube = build(api_service_name, api_version, credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
          "snippet": {
            "categoryId": args.category,
            "description": args.description,
            "title": args.title
          },
          "status": {
            "privacyStatus": args.privacy
          }
        },
        media_body=MediaFileUpload(args.video_file)
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()

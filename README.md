
# youtube-cli-uploader

Python CLI tool for uploading videos to YouTube with ease. Supports specifying video metadata (title, description, category, privacy) via command-line arguments.

## Setup

### Prerequisites
- Python 3.x
- Google account with access to YouTube Data API

### Installation
Clone the repository:
   ```bash
   git clone https://github.com/vladbobu/youtube-cli-uploader.git
   ```


### Google API Credentials
1. Set up your OAuth 2.0 credentials at the [Google Developers Console](https://console.developers.google.com/).
2. Download your `client_secrets.json` file and place it in the root directory.

## Usage
Run the script using the following format:
```bash
python upload_video.py <path-to-video> --title "Your Video Title" --description "Your Video Description" --category "22" --privacy "public"
```

### Command-Line Arguments
- `video_file`: Path to the video file (required)
- `--title`: Title of the video (optional)
- `--description`: Description of the video (optional)
- `--category`: Category ID of the video (optional)
- `--privacy`: Privacy status of the video (optional)

## License
[MIT License](LICENSE)

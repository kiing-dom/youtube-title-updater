# YouTube Title Updater

This project provides a script to mass edit YouTube video titles using the YouTube Data API. It's designed to update video titles from "Road to Employment" to "Road to SWE".
`note this will clear your videos' descriptions and tags`

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube-title-updater.git
   cd youtube-title-updater
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up Google Cloud project and enable YouTube Data API v3.

5. Create OAuth 2.0 credentials and download the client configuration.

6. Rename the downloaded file to `client_secrets.json` and place it in the project root.

7. Copy `.env.example` to `.env` and update with your configuration.

## Usage

Run the script:

```
python src/youtube_updater.py
```

## Testing

Run tests:

```
python -m pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
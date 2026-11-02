# Y-o-u-a-u-t-o

A Python-based automation project for generating YouTube content using AI-written scripts, text-to-speech narration, and video rendering. The repository is structured as an end-to-end prototype for creating engaging Shorts and long-form video ideas, with a GitHub Actions workflow that can trigger the pipeline on a schedule.

## What this project does

This project generates:

- AI-written YouTube scripts using Gemini
- Voiceover audio using Google Text-to-Speech
- Video clips from scripts using MoviePy
- A foundation for YouTube uploads using the YouTube Data API

The main workflow is:

1. Generate a script with the Gemini API
2. Convert the script to spoken audio
3. Render a video with captions and a dark background
4. Upload the final video to YouTube (scaffolded and ready to complete)

## Repository layout

- `script_gen.py` — creates a script prompt for either Shorts or long-form content using Gemini
- `video_gen.py` — converts the script to a video with text overlay and voice narration
- `uploader.py` — contains the YouTube upload integration scaffold
- `requirements.txt` — required Python packages
- `.github/workflows/auto_upload.yml` — GitHub Actions automation for running the pipeline
- `text` — project notes / rough file tree description

## Core functionality

### 1) Script generation

The `generate_script()` function in `script_gen.py` creates a script prompt based on `video_type`:

- `short` mode: a 50-word viral YouTube Short script
- default/other mode: a longer Reddit-style story or mystery script

It uses the Google GenAI SDK:

```python
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)
```

### 2) Video generation

The `create_video()` function in `video_gen.py`:

- converts script text to speech with `gTTS`
- creates an audio clip
- sizes the video for either Shorts (`1080x1920`) or landscape (`1920x1080`)
- creates a dark background and adds a large text caption overlay
- writes the rendered video to an MP4 file using MoviePy

### 3) YouTube upload

`uploader.py` is set up as an upload helper and mentions the Google YouTube Data API v3 and OAuth setup. The code is intentionally minimal and appears to be a starting point for integrating authenticated uploads.

## Automation

The repository includes a scheduled GitHub Actions workflow:

- file: `.github/workflows/auto_upload.yml`
- trigger: daily cron schedule + manual dispatch
- environment: Ubuntu + Python 3.10
- actions:
  - checkout repository
  - install dependencies
  - run the video pipeline

The workflow currently has the video generation and uploader steps commented out, suggesting the project is in a prototype or partial-automation stage.

## Prerequisites

Before running the project, install dependencies:

```bash
pip install -r requirements.txt
```

Required environment variables:

```bash
export GEMINI_API_KEY="your-google-gemini-key"
```

For YouTube upload integration, additional Google OAuth / YouTube API setup would be required.

## Usage

### Generate a script

```bash
python script_gen.py
```

### Render a video

```bash
python video_gen.py
```

### Upload to YouTube

```bash
python uploader.py
```

## Notes

This repository appears to be an experimental automation project for AI-generated storytelling and content production. It demonstrates a useful pipeline for automating script generation and video creation, but the YouTube upload functionality still requires the full OAuth and API implementation to be completed.

## Dependencies

The project uses:

- `google-genai`
- `requests`
- `moviepy`
- `gTTS`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `google-api-python-client`

## License

This repository includes an MIT-style license file. See `LICENSE` for details.

## Summary

Y-o-u-a-u-t-o is a small Python content automation project built around AI-generated YouTube scripts and video rendering. It is ideal for experimenting with automated storytelling, voiceover generation, and workflow scheduling for content production pipelines.

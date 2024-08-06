# YouTube Video Summarizer

A Streamlit app that takes a YouTube video URL, extracts the video's transcript, and generates a concise summary using the Hugging Face Transformers library. This tool is ideal for quickly understanding the content of long YouTube videos without watching them in their entirety.

## Features

- **User-friendly Interface**: Enter the YouTube video URL in a text box and get a summary with a single click.
- **Automatic Transcript Extraction**: Utilizes the YouTube Transcript API to fetch the video transcript.
- **Summarization with Transformers**: Leverages the powerful Transformers library from Hugging Face to generate meaningful summaries.
- **Streamlit Integration**: The app is built with Streamlit, providing an intuitive and interactive user experience.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/youtube-video-summarizer.git
    cd youtube-video-summarizer
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your Hugging Face token:

    - Create a file named `config.py` in the same directory as `app.py`.
    - Add the following line to `config.py`:

        ```python
        HUGGING_FACE_TOKEN = 'your_hugging_face_token'
        ```

5. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the app in your web browser (usually at `http://localhost:8501`).
2. Enter the YouTube video URL in the provided text box.
3. Enter your Hugging Face token.
4. Click the "Submit" button.
5. Wait for the app to fetch the transcript and generate the summary.
6. Read the summarized content displayed below.

## Requirements

- Python 3.6 or higher
- Streamlit
- Transformers library
- YouTube Transcript API

## Contributing

Contributions are welcome! If you have any ideas for improvements or encounter any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

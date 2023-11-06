# Sentiment Analysis with RoBERTa Model and Streamlit



This project is a Sentiment Analysis tool that uses the RoBERTa model for natural language processing and a Streamlit-based frontend. It was developed during an internship hackathon and is designed to analyze the sentiment of text input.

## Prerequisites

- Conda: Make sure you have Conda installed on your system. If you don't have it, you can install it by following the instructions here: [Conda Installation Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Acknowledgments](#acknowledgments)

## Introduction
Sentiment analysis is a natural language processing task that involves determining the emotional tone of a piece of text, such as positive, negative, or neutral. In this project, we use the RoBERTa model, a variant of the BERT model, for sentiment analysis. The model is fine-tuned to classify the sentiment of text data.

The frontend is built using Streamlit, a popular Python library for creating web applications with minimal code. Users can input text, and the application will provide sentiment analysis results, indicating the sentiment as positive, negative, or neutral.

## Installation
To set up this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <https://github.com/AbhishekPaul08/Sentiment_Analysis.git>
   cd sentiment-analysis-roberta
   ```

2. Create a Conda environment and install the required dependencies from the provided `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the Conda environment:
   ```bash
   conda activate sentiment-analysis-roberta
   ```

4. Download the RoBERTa model weights and save them in the `models` directory. You can use the Hugging Face Transformers library to obtain the RoBERTa model weights.

5. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   or use 
   ```bash
   streamlit run  "C:\Users\asp00\Downloads\Sentiment_analysis\app.py"
   ```

Now, the Sentiment Analysis application should be accessible in your web browser.

## Usage
1. Open your web browser and navigate to the provided Streamlit application URL.

2. Enter the text you want to analyze in the input field.

3. Click the "Analyze Sentiment" button to initiate the sentiment analysis.

4. The application will display the sentiment of the entered text as either "Positive," "Negative," or "Neutral."

## Model
The RoBERTa model used in this project is a pre-trained model for natural language understanding. It has been fine-tuned on a sentiment analysis dataset to classify the sentiment of text. The model's weights can be obtained from the Hugging Face Transformers library or by training it on your own dataset.

## Acknowledgments
This project was developed during an internship hackathon and was made possible with the following resources and tools:

- [RoBERTa Model](https://huggingface.co/transformers/model_doc/roberta.html)
- [Streamlit](https://www.streamlit.io/)
- [Hugging Face Transformers Library](https://huggingface.co/transformers/)

Feel free to customize and extend this project to suit your specific needs or integrate it with other applications. If you have any questions or suggestions, please feel free to reach out to the project developers.

## Development

If you want to customize or extend this project, here's how the code is structured:

- `app.py`: The main Streamlit application that contains the user interface and handles the sentiment analysis process.

- `requirements.txt`: A list of required Python packages and their versions.

- `run.txt`: Command to run the streamlit webapp.

Enjoy using this Sentiment Analysis tool with RoBERTa and Streamlit!

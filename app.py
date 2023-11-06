# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 00:56:34 2023

@author: asp00
"""

import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import numpy as np
from scipy.special import softmax

# Load the RoBERTa model and tokenizer (adjust the model name as needed)
model_name = f"cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def classify_sentiment(scores_dict):
    roberta_pos = scores_dict['roberta_pos']
    roberta_neg = scores_dict['roberta_neg']
    roberta_neu = scores_dict['roberta_neu']

    if roberta_pos > roberta_neg and roberta_pos > roberta_neu:
        return 'Positive'
    elif roberta_neg > roberta_pos and roberta_neg > roberta_neu:
        return 'Negative'
    else:
        return 'Neutral'

def classify_sentiment_and_scores(sentence):
    encoded_text = tokenizer(sentence, return_tensors='pt')
    output = model(**encoded_text)
    scores = output.logits[0].detach().numpy()
    scores = softmax(scores)

    scores_dict = {
        'roberta_neg': scores[0],
        'roberta_neu': scores[1],
        'roberta_pos': scores[2]
    }

    sentiment = classify_sentiment(scores_dict)

    return scores_dict, sentiment

def main():
    st.title("Sentiment Analysis")
    st.write("Enter a text, and we'll classify its sentiment.")
    col1, col2,  = st.columns(2)
    # Input text from the user 
    with col1:
        user_input = st.text_area("Enter the text:")
    with col1:
        if st.button("Classify Sentiment"):
            if user_input:
                scores, sentiment = classify_sentiment_and_scores(user_input)
               
                st.write("Sentiment Class:", sentiment)
                
    with col2:
        # Load and display a GIF from a file on your local machine
        #gif_path = 'C:/Users/asp0/0Downloads/011/sentiment.gif'
        #st.image(gif_path, use_container_width=True)
        
        #gif_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fdata-flair.training%2Fblogs%2Fpython-sentiment-analysis%2F&psig=AOvVaw3twYGS_y_MuNGPwUOO6AtU&ust=1699074281930000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPjD0o6Hp4IDFQAAAAAdAAAAABAc '
        #st.image(gif_url)
        
        image_url = "https://content.altexsoft.com/media/2018/09/sentiment-score.jpeg "
       # st.image(image_url, caption="Image from URL", use_column_width=True)
       
        st.image(image_url, caption="sentiments", width=300)

if __name__ == "__main__":
    main()

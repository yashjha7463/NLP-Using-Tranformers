# NLP Task Processor

I completed a course on Cognitive AI, and the `hugging_face_transformers.ipynb` file is from that course. Inspired by the knowledge gained, I decided to implement my learning and create a Streamlit application for natural language processing tasks.

## Project Overview

This project utilizes state-of-the-art transformer models from Hugging Face to offer a range of natural language processing (NLP) tasks. The Streamlit-based application allows users to input text and select from various NLP tasks including sentiment analysis, text generation, named entity recognition, and text summarization.

## Files

- **`main.py`**: 
Import Necessary Tools: This file starts by importing a tool called pipeline from a library called transformers. Think of it like bringing in a set of special machines that can understand and process human language.

Create NLPProcessor Class: Here, we create a special class called NLPProcessor. Think of it as a factory that can make different types of language processing machines.

Initialize Models: Inside this class, we set up different types of language processing machines (like machines for understanding sentiment, generating text, recognizing names, and summarizing text). We tell each machine which "brain" it should use, which is actually a model pre-trained on lots of data.

Process Text Method: We create a method inside the NLPProcessor class that allows us to send some text to one of the machines we set up and get back the processed result. For example, if we send a piece of text to the sentiment analysis machine, it will tell us whether the text sounds positive, negative, or neutral.

Example Usage: At the end, there's an example showing how to use this NLPProcessor. We pick a task (like text generation), provide some text, and then see what the processor gives us back.

In summary , it Contains the main logic for initializing and utilizing transformer models for NLP tasks. It includes a class `NLPProcessor` that handles the initialization of transformer models and provides methods for processing text based on different NLP tasks.
  
- **`app.py`**:
Import Streamlit: This file starts by importing a tool called Streamlit, which helps us build interactive web apps.

Define Main Function: Here, we define a main function where the actual app logic will live.

Title and Sidebar: We set the title of our app and create a sidebar where users can choose which type of language processing they want to do (like sentiment analysis or text generation).

Text Input: We add a space where users can type in the text they want to process.

Processing Options: Depending on what task the user chooses (like text generation), we might ask for additional information, like the maximum length of generated text.

Process Button: We add a button that users can click to start the processing.

Processing Logic: When the button is clicked, we use the NLPProcessor from main.py to process the text based on the chosen task. Then, we display the result to the user.

Main Function Call: Finally, we call the main function to start the app when the script is run.

In summary, it Implements the Streamlit user interface for the NLP Task Processor. It provides options for users to input text and select the desired NLP task. Upon processing, it interacts with the `NLPProcessor` class from `main.py` to perform the selected task and displays the results.

## Usage

To run the Streamlit app, use the following command:
`streamlit run app.py`

Once the app is running, open your web browser and navigate to the provided URL to access the NLP Task Processor. Input your text and select the desired NLP task, then click the "Process" button to see the results.

## Requirements

Ensure you have the necessary Python libraries installed. You can install them using the following command:
`pip install -r requirements.txt`


## Acknowledgements

- The transformer models used in this project are from the Hugging Face model hub.
- Inspiration and initial code structure for this project were obtained from the Cognitive AI course.


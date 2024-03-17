import streamlit as st
from main import NLPProcessor


@st.cache(allow_output_mutation=True)
def load_nlp_processor():
    return NLPProcessor()

def main():
    st.title("NLP Task Processor")
    task = st.sidebar.selectbox("Select NLP Task", ["Sentiment Analysis", "Text Generation", "Name Entity Recognition", "Text Summarization"])
    text_input = st.text_area("Enter Text")
    
    if task == "Text Generation":
        max_length = st.number_input("Max Length", min_value=1, value=30)
        num_return_sequences = st.number_input("Number of Sequences", min_value=1, value=2)
    
    if st.button("Process"):
        processor = NLPProcessor()
        task_mapping = {
            "Sentiment Analysis": "sentiment-analysis",
            "Text Generation": "text-generation",
            "Name Entity Recognition": "ner",
            "Text Summarization": "summarization"
        }
        task_name = task_mapping.get(task)
        if task_name:
            if task_name == "text-generation":
                result = processor.process_text(task_name, text_input, max_length, num_return_sequences)
            else:
                result = processor.process_text(task_name, text_input)
            st.write(result)
        else:
            st.write("Invalid task selected")

if __name__ == "__main__":
    main()
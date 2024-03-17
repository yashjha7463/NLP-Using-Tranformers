from transformers import pipeline

class NLPProcessor:
    def __init__(self):
        self.classifiers = {
            "sentiment-analysis": pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english"),
            "text-generation": pipeline("text-generation", model="gpt2"),
            "ner": pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True),
            "summarization": pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        }

    def process_text(self, task, text, max_length=None, num_return_sequences=None):
        classifier = self.classifiers.get(task)
        if classifier:
            if task == "text-generation":
                return classifier(text, max_length=max_length, num_return_sequences=num_return_sequences)
            else:
                return classifier(text)
        else:
            return "Invalid task specified"

if __name__ == "__main__":
    processor = NLPProcessor()
    # Example usage
    task = "text-generation"
    text = "This course will teach you"
    max_length = 30
    num_return_sequences = 2
    result = processor.process_text(task, text, max_length, num_return_sequences)
    print(result)
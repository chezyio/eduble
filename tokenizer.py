

import re
import nltk
from nltk.tokenize import sent_tokenize
from summarizer import Summarizer

summarizer = Summarizer()


# Download NLTK resources (run only once)
nltk.download('punkt')


# Function to extract and display sentences from .srt file (excluding timestamps and numbers)
def extract_and_display_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        subtitle_content = file.read()

    # Use regular expressions to remove timestamps and numbers
    subtitle_content = re.sub(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+\n', '', subtitle_content)
    subtitle_content = re.sub(r'\d+\n', '', subtitle_content)

    # Split the content into subtitles based on the empty lines
    subtitles = subtitle_content.split('\n\n')

    # Extract sentences from each subtitle
    sentences = []
    for subtitle in subtitles:
        # Use NLTK's sentence tokenizer to extract sentences
        subtitle_sentences = sent_tokenize(subtitle)
        sentences.extend(subtitle_sentences)

    # Display the extracted sentences
    for i, sentence in enumerate(sentences, start=1):
        print(f"{sentence.strip()}")
    
    return sentences

# Example usage, change user path
file_path = 'output_transcript.srt'
extracted = extract_and_display_sentences(file_path)



model = Summarizer()
optimal = model.calculate_optimal_k(str(extracted), k_max=10)
result = model(str(extracted), num_sentences=optimal)

full = ''.join(result)
print(full)


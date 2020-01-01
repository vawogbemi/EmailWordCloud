import re, string, unicodedata
import nltk
nltk.download('punkt')

import contractions
#import inflect

from wordcloud import WordCloud 
from bs4 import BeautifulSoup

from nltk import word_tokenize, sent_tokenize
from nylas import APIClient


#Function Definitions

#Noise Removal 
def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def replace_contractions(text):
    """Replace contractions in string of text"""
    return contractions.fix(text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = replace_contractions(text)
    return text

# Main
nylas = APIClient(
    "6ihfb5rh4uw0iwgops0qj2v57",
    "9d2373w0eu8w4r1y7vjbljurm",
    "NUmEnEHQoFEnbTKtdw91F5D2sGEyCO"
)


for message in nylas.messages.where(limit=1):

    text = denoise_text(message.body)
    text = nltk.word_tokenize(text)


wc = WordCloud()
img = wc.generate_from_text(' '.join(text))
img.to_file('wordcloud.jpeg') # example of something you can do with the img

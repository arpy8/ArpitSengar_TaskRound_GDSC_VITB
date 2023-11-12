import random
from nltk.util import ngrams
import streamlit as st


st.set_page_config(page_title="Shakespeare’s Sonnets", page_icon="📔")

shakespeare_sonnets = open("Data/Sonnets.txt", "r").readlines()
shakespeare_text = [text.rstrip("\n") for text in shakespeare_sonnets] 

ngram_model = {}
n=2

for sonnet in shakespeare_text:
    words = sonnet.split()
    ngrams_list = list(ngrams(words, 2))
    for ngram in ngrams_list:
        prefix = " ".join(ngram[:-1])
        suffix = ngram[-1]
        if prefix in ngram_model:
            ngram_model[prefix].append(suffix)
        else:
            ngram_model[prefix] = [suffix]


def generate_sonnet(starting_word, length):
    sonnet = starting_word
    current_word = starting_word
    for _ in range(length):
        next_word = random.choice(ngram_model.get(current_word, ["."]))
        if next_word == ".":
            pass
        else:
            sonnet += " " + next_word
        current_word = " ".join(sonnet.split()[-n+1:])
    return sonnet


starting_word = "shall I compare"


def create_sonnet(n):
    st.write("### Shall I compare")
    for _ in range(n): 
        st.write(generate_sonnet(starting_word, 100).strip("shall I compare ").title())


st.write("# Shakespeare’s Sonnets")

lines = st.number_input("Number of lines", min_value=0, max_value=50, step=1, value=random.randint(0,15))
left, right = st.columns((7,1))

with left:
    st.empty()
with right:
    submit = st.button("Submit")

if lines:
    create_sonnet(lines)
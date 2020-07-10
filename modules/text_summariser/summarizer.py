import math
import nltk.data
import string
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

sentences_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def frequencies(tokenized_sentences):
    wordcount = defaultdict(int)
    for sentence in tokenized_sentences:
        for word in sentence:
            wordcount[word] += 1
    return wordcount


def calculate_tf(word_frequencies):
    word_tfs = {}
    for word in word_frequencies:
        word_tfs[word] = 1 + math.log(word_frequencies[word])
    return word_tfs


def calculate_score(sentence, word_tfs):
    score = 0
    for word in remove_stopwords(sentence):
        score += word_tfs[word]
    return score


def remove_stopwords(tokens):
    return [token for token in tokens if
            token not in stopwords.words('english') and token not in string.punctuation]


def summarize(text, sentence_number=5):
    sentences = sentences_detector.tokenize(text.strip())
    tokenized_sentences = [remove_stopwords(word_tokenize(sentence)) for sentence in sentences]

    word_frequencies = frequencies(tokenized_sentences)
    word_tfs = calculate_tf(word_frequencies)

    scored_sentences = [(ind, calculate_score(p, word_tfs)) for ind, p in enumerate(tokenized_sentences)]
    sorted_scored_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)
    selected_sentences = sorted(sorted_scored_sentences[0:sentence_number], key=lambda x: x[0])

    summary = [sentences[i] for i in [ind for ind, score in selected_sentences]]
    result = '\n'.join(summary)
    output_text_file_name = r'/home/saurabh/PycharmProjects/audio_summariser/resources/summarised_text/result.txt'
    text_file = open(output_text_file_name, "wt")
    text_file.write(result)
    text_file.close()
    print(result)



file_name = r'/home/saurabh/PycharmProjects/audio_summariser/resources/punctuated_text/punct_text.txt'
file = open(file_name)
text = file.read()
file.close()
summarize(text, sentence_number=6)

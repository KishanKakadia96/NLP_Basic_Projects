#cleaning tasks
import re
import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec

Paragraph = """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial 
intelligence concerned with the interactions between computers and human language, in particular how to program 
computers to process and analyze large amounts of natural language data. The goal is a computer capable of 
"understanding" the contents of documents, including the contextual nuances of the language within them. The 
technology can then accurately extract information and insights contained in the documents as well as categorize and 
organize the documents themselves. Challenges in natural language processing frequently involve speech recognition, 
natural-language understanding, and natural-language generation. """

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]', ' ', Paragraph)
text = re.sub(r'\s+', ' ', text)
text = text.lower()
text = re.sub(r'\d', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Preparing the dataset
sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]

# Training the Word2Vec model
model = Word2Vec(sentences, min_count=1)

words = model.wv.index_to_key

# Finding Word Vectors
vector = model.wv['amounts']
#print(vector)

# Most similar words
similar = model.wv.most_similar('contents')
print(similar)
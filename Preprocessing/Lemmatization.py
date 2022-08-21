import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

from Bag_of_Words import sentences

Paragraph = """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial 
intelligence concerned with the interactions between computers and human language, in particular how to program 
computers to process and analyze large amounts of natural language data. The goal is a computer capable of 
"understanding" the contents of documents, including the contextual nuances of the language within them. The 
technology can then accurately extract information and insights contained in the documents as well as categorize and 
organize the documents themselves. Challenges in natural language processing frequently involve speech recognition, 
natural-language understanding, and natural-language generation. """

sentences = nltk.sent_tokenize(Paragraph)
lemmatizer = WordNetLemmatizer()

#Lemmatization

for i in range(len(sentences)):
    words = nltk.word_to_sentence(sentences[i])
    words = [lemmatizer.lemmatize(words) for word in words if word not in set(stopwords.words('english')) ]
    sentences[i] = ' '.join(words)


#cleaning tasks
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer



Paragraph = """Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial 
intelligence concerned with the interactions between computers and human language, in particular how to program 
computers to process and analyze large amounts of natural language data. The goal is a computer capable of 
"understanding" the contents of documents, including the contextual nuances of the language within them. The 
technology can then accurately extract information and insights contained in the documents as well as categorize and 
organize the documents themselves. Challenges in natural language processing frequently involve speech recognition, 
natural-language understanding, and natural-language generation. """

ps = PorterStemmer()
wordnet = WordNetLemmatizer()
sentences = nltk.sent_tokenize(Paragraph)
corpus = []
for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(w) for w in review if not w in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
print(corpus)

#creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features= 1500)
X=vectorizer.fit_transform(corpus).toarray()
print(X)





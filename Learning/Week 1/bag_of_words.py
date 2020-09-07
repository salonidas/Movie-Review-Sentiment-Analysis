import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('Movie-Review-Sentiment-Analysis\movie_data.csv')
df.head()

#converting raw data to tf-idf format
#convert to sparse feature vector
#using bag-of-words model from NLP

count = CountVectorizer()

data_doc = np.array(['The sun is shining',
                     'The weather is sweet',
                     'The sun is shining, the weather is sweet, and one and one is two'])

bow = count.fit_transform(data_doc)
print(count.vocabulary_)
print(bow.toarray())

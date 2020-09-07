from sklearn.feature_extraction.text import TfidfTransformer

np.set_printoptions(precision=2)

tfidf = TfidfTransformer(use_idf=True, norm='l2', smooth_idf=True)
print(tfidf.fit_transform(bow).toarray())

df.loc[0, 'review'][-50:]

import re
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) +\
        ' '.join(emoticons).replace('-', '')
    return text
   
preprocessor(df.loc[0, 'review'][-50:])

preprocessor("<p>Test ;) :) :-) String :(</p>")

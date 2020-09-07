from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()

#function to tokenise text to spilt sentences into words
def tokenizer(text):
    return text.split()
    
#stemming function
def stemming(text):
    return [porter.stem(word) for word in text.split()]
    
tokenizer('The organizer loves organizing events for the organization')
stemming('The organizer loves organizing events for the organization')

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

sw = stopwords.words('english')
[w for w in stemming('The organizer loves organizing events for the organization') if w not in sw]


from nltk.corpus import stopwords
import pandas as pd



stop = stopwords.words('english')

df = pd.read_csv("../data/orginazation_label.csv", encoding='latin1', low_memory=False)
print(df)

pos_tweets = [('I love this car', 'positive'),
    ('This view is amazing', 'positive'),
    ('I feel great this morning', 'positive'),
    ('I am so excited about the concert', 'positive'),
    ('He is my best friend', 'positive')]


# Exclude stopwords with Python's list comprehension and pandas.DataFrame.apply.
df['Tweet_without_stopwords'] = df['word'].apply(lambda x: ' '.join([Word for Word in x.split() if Word not in (stop)]))
print(df)
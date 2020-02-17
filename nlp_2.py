from pathlib import Path
from textblob import TextBlob
from textblob import Word

blob=TextBlob(Path('RomeoAndJuliet.txt').read_text())

blob.words.count('Joy')

happy=Word('happy')

#print(happy.definitions)

print(happy.synsets)

synonyms=set()

for synset in happy.synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

print(synonyms)

from nltk.corpus import stopwords
stops=stopwords.word("english")


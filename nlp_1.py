from textblob import TextBlob

text='Today is a beautiful day. Tomorrow looks like bad weather.'

blob=TextBlob(text)

#print(blob)

#print(blob.sentences) #a list includes both sentences

#print(blob.words) #a list includes all the words

#print(blob.tags) # a list includes all the words and what kind of words they are

#print(blob.noun_phrases) # ~ all the none phrases

#print(round(blob.sentiment.polarity,3))

#print(round(blob.sentiment.subjectivity,3))

#for sentence in blob.sentences:
    #print(round(sentence.sentiment.polarity,3))
    #print(round(sentence.sentiment.subjectivity,3))

#from textblob.sentiments import NaiveBayesAnalyzer

#blob=TextBlob(text,analyzer=NaiveBayesAnalyzer())

#print(blob.sentiment)

#for sentence in blob.sentences:
    #print(sentence.sentiment)

#print(blob.detect_language())

#spanish=blob.translate(to='es')
#print(spanish)

#german=blob.translate(to='de')
#print(german)

#print(spanish.translate()) ---translate back to EN

from textblob import Word
#word=Word('theyr')
#print(word.spellcheck())
#new_word=word.correct()
#print(new_word)

sentence=TextBlob("This sentense has missplled wrds.")
new_sentence=sentence.correct
print(new_sentence)
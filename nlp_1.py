from textblob import TextBlob

text='Today is a beautiful day. Tomorrow looks like bad weather.'

blob=TextBlob(text)

print(blob)

#print(blob.sentences) #a list includes both sentences

#print(blob.words) #a list includes all the words

#print(blob.tags) # a list includes all the words and what kind of words they are

print(blob.noun_phrases) # ~ all the none phrases

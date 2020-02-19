from textblob import TextBlob
import nltk

#nltk.download("stopwords") --- download only required once

from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

stops = stopwords.words("english")

#blob = TextBlob("Today is a beautiful day.")
#print([word for word in blob.words if word not in stops])

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

items = blob.word_counts.items()
#print(items)

items_no_stops = [item for item in items if item[0] not in stops]
#print(items_no_stops)

from operator import itemgetter

sorted_items = sorted(items_no_stops,key=itemgetter(1),reverse=True)
top20=sorted_items[:21]

#print(top20)

df=pd.DataFrame(top20,columns=["words","count"])

print(df)

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import imageio

df.plot.bar(x='word',y='count',rot=0,legend=False,color=['y','c','m','b','g','r'])

plt.gcf().tight_layout()
#plt.show()

""" text=Path('RomeoAndJuliet.txt').read_text()

mask_image=imageio.imread('mask_heart.png')
wordcloud=WordCloud(colormap='prism',mask=mask_image,background_color='white')
wordcloud=wordcloud.generate(text)

wordcloud=wordcloud.to_file('RomeoAndJulietHeart.png')
plt.imshow(wordcloud)
print('done') """
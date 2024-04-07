import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
import sys,os
os.chdir(sys.path[0])

#read the text
text=open('dinna.txt',mode='r',encoding='utf-8').read()
stopwords=STOPWORDS

wc=WordCloud(
        background_color="black",
        stopwords=stopwords,
        height=600,
        width=500
    )
wc.generate(text)
wc.to_file('output.png')

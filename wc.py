import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
text = open('gofund.txt').read() 
text = re.sub('\n', '', text)
text = text.rstrip().lstrip()
print(text)
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='black', colormap='Pastel1', collocations=False, 
        stopwords = STOPWORDS).generate(text)
wordcloud.to_file("wc.png")

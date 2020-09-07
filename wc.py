import wikipedia
import re
import matplotlib.pyplot as plt
def print_wc(wc):
    plt.figure(figsize=(40,30))
    plt.imshow(wc)

wiki = wikipedia.page('Web scraping')
text = wiki.content
text = re.sub(r'==.*?==+', '', text)
text = re.sub('\n', '', text)
text = text.rstrip().lstrip()
print(text)




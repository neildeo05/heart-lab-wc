import urllib2
import time
import re
from bs4 import BeautifulSoup
def takeLink(link):
    page = urllib2.urlopen(link)
    s = BeautifulSoup(page)
    cl="o-campaign-story mt-three-halves o-campaign-story--is-open"

    with open('words.txt', 'w') as fp:

        fp.write(str(s.findAll('div', attrs = {
            'class': 'o-campaign-story mt-three-halves'
            })[0]) + '\n')



f = open('gm.html').read()
soup = BeautifulSoup(f)



for link in soup.findAll('a', attrs = {'class':'campaign-tile-img--contain js-lazy'}): 
    print(link['href'])
    takeLink(link['href'])


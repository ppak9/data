from urllib import response
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter

def clean_wordlist(wordlist):
 
    clean_list = []
    for word in wordlist:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/.,0123456789"
 
        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')
 
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

def create_dictionary(clean_list):
    word_count = {}
 
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    c = Counter(word_count)
 
    # returns the most occurring elements
    top = c.most_common(40)
    print(top)

url = 'https://www.trustpilot.com/review/cazoo.co.uk?search=subscription&stars=1'
response = requests.get(url)

if response.status_code == 200:

    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    wordlist = []
    result = soup.find_all('p')   
    for i in result:
        word = i.text
        words = word.split()
        for each_word in words:
            wordlist.append(each_word)

    clean_wordlist(wordlist)
    
else:
    print(response.status_code)


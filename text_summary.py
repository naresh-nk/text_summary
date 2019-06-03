import urllib.request
from requests_html import HTMLSession
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest

from string import punctuation
from collections import defaultdict

def get_article_text(url, tag):
	'''
	Extracts text of a specific 'html tag' from web page(url)
	Example:

	  article_url = 'https://en.wikipedia.org/wiki/Editorial'
	  tag = "#mw-content-text > div > p"
	  text = get_article_text(article_url, tag)

	'''
	session = HTMLSession()
	page = session.get(url)
	text = ' '.join(map(lambda p: p.text, page.html.find(tag)))

	return str(text)

#Text preprocessing
##Remove stop words

def remove_stop_words(text):
	'''
	This text preprocessing function is to remove english stop words from the text.
	
	Example:
	   
	   text = "This is a sample text"
	   clean_text = remove_stop_words(text)
	'''

	words = word_tokenize(text.lower())
	#stop_words = set(stopwords.words('english') + list(punctuation))
	stop_words = stopwords.words('english') + list(punctuation) + list(['’', '“','”', '—'])
	text_without_stop_words = [word for word in words if word not in stop_words]

	return text_without_stop_words

def get_top_sentences(number_of_sentences, text):
	'''
	This function will return the top n sentences from the given text
	based on highest count or words in text using frequency distribution method.

	Example:
    
	   top_sentences = get_top_sentences(4, text)
	   for s in top_sentences:
         print(s,'\n')

	'''

	sentences = sent_tokenize(text)
	assert number_of_sentences <= len(sentences)

	#Freq distribution
	text = remove_stop_words(text)
	freq = FreqDist(text)

	#initialize a defaultdict object
	ranking = defaultdict(int)
	for i, sentence in enumerate(sentences):
		for word in word_tokenize(sentence.lower()):
			if word in freq:
				ranking[i] += freq[word]

	top_sentences = [sentences[j] for j in sorted(nlargest(number_of_sentences, ranking, key=ranking.get))]

	return top_sentences

if __name__ == '__main__':
	'''
    Complete example:
	
	'''
	article_url = 'https://www.nytimes.com/2019/06/02/opinion/vaccines-peter-hotez.html'
	#tag = "#mw-content-text > div > p"
	tag = '#story'
	text = get_article_text(article_url, tag)
	print('\nComplete Text: \n',text)
	print('\n', 'Summary Text: ', '\n')

	top_sentences = get_top_sentences(4, text)
	for s in top_sentences:
		print(s)

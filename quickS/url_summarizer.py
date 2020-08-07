from bs4 import BeautifulSoup
from text_summarizer import FrequencySummarizer
import requests
import sys
import re
import os
import sys
import pdfkit


def search_google(topic):
    base_url = 'https://www.google.com/search?q='
    response = requests.get(base_url + topic)
    if not response.ok:
        raise RuntimeError('error making request to {}'.format(base_url + topic))
    return response.content

def get_url(topic):
    urls_seen = []
    html_doc = search_google(topic)
    soup = BeautifulSoup(html_doc, 'html.parser')
    for i, link in enumerate(soup.find_all('a')):
        url = re.findall('/url\?q=(.+)&sa=U', link.get('href'))
        if url and url not in urls_seen:
            urls_seen.append(url[0])
            try:
                print("")
                print(url[0] +"\n" + summarizeURL(url[0], 4))
            except Exception:
                print("")



def get_topics(file_path):
    with open(file_path) as f:
        topics = [topic.strip() for topic in f]
    return topics

def getTextFromURL(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, "html.parser")
	text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return text

def summarizeURL(url, total_pars):
	url_text = getTextFromURL(url).replace(u"Â", u"").replace(u"â", u"")

	fs = FrequencySummarizer()
	final_summary = fs.summarize(url_text.replace("\n"," "), total_pars)
	return " ".join(final_summary)
def main(arguments):

    '''
    First argument should be the path to the list of requirements
    Second arugment should be the path to save the directories in (defaults to current directory)
    '''


    path = '.'
    if len(arguments) not in (2,3):
        raise OSError('Incorrect input to run program. The first argument should be the path to a list of requirments, \
            the second optional argument should the path to save the directories in (default is current directory)')
    topics = get_topics(arguments[1])
    if len(arguments) == 3:
        path = arguments[2]

    #print(get_url("grimes"))



    for topic in topics:
        print("------------------------" + topic + "----------------------------")
        get_url(topic)


        #summarizeURL(get_url(topics), 4)
        #for i in range(len(urls)):
            #print(urls[i])

    print('\nFinished')

main(sys.argv)
#url = raw_input("Enter a URL\n")
#final_summary = summarizeURL('https://en.wikipedia.org/wiki/Edgar_Allan_Poe', 5)
#print (final_summary)

A  script I made that automatically summarizes webpages using a nlp python library. 
It will Google each topic(that you input into topics.txt) and automatically summarize websites from the first page of results in Google. 

It is not perfect and some pages will have errors, but it could help save time when pages need to quickly be summarized for research purposes or something along the lines of that. 

How to Use
In the command line:

$ python url_summarizer.py topics.txt 

Formating the Topics
Save the requirements in a text file, with one topic on each line.

Dependencies
pdfkit
bs4
nltk
heapq

import pdftotext
import requests
import wget
import re

def getName(url):
	return url.split('/')[-1]
def downloadPdf(url):
	name = getName(url)
	print url,name
	wget.download(url,'Results/'+name)

def readPdf(name):
	# Load your PDF
	with open(name,"rb") as f:
	    pdf = pdftotext.PDF(f)

	# How many pages?
	print(len(pdf))

	# # Iterate over all the pages
	# for page in pdf:
	#     print(page)
	# Read all the text into one string
	print("\n\n".join(pdf))

def getPdfNames(url):
	html=requests.get(url)
	html=html.content
	html=html.replace('\n','')
	html=html.replace('<a href=\"#content\">','')
	html=html.replace('/contests/','')
	# print html
	# print '-'*500
	matches = re.findall(r'<a href="(.*?)"',html)
	matches = [i for i in matches if 'Results' in i]
	matches = list(dict.fromkeys(matches))
	matches = sorted(matches)	
	# for i in matches:
	# 	print i
	return matches


url='https://www.cemc.uwaterloo.ca/contests/past_contests.html'
paths = getPdfNames(url)
# for i in paths:
# 	downloadPdf('https://www.cemc.uwaterloo.ca/contests/'+i)
names = map(lambda url: 'Results/'+url,map(getName,paths))
for i in names:
	if 'CxMC' in i:
		readPdf(i)
		print i
		
#O god how am I gonna parse this?



# Gauss
# Pascal
# Cayley
# Fermat


# Fryer
# Galois
# Hypatia
# Euclid

# CxMC

# BCC

# CCC

# CCO
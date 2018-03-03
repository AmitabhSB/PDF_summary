##PDFMINER PAGE Count
##from pdfminer.pdfparser import PDFParser
##from pdfminer.pdfdocument import PDFDocument
##from pdfminer.pdfpage import PDFPage
##from pdfminer.pdfinterp import resolve1
##
##file = open('patent.pdf', 'rb')
##parser = PDFParser(file)
##document = PDFDocument(parser)
##
### This will give you the count of pages
##count= (resolve1(document.catalog['Pages'])['Count'])
##print (count)
##

##
##import PyPDF2 
##import textract
##from nltk.tokenize import word_tokenize
##from nltk.corpus import stopwords
##
###write a for-loop to open many files -- leave a comment if you'd #like to learn how
##filename = 'patent.pdf' 
###open allows you to read the file
##pdfFileObj = open(filename,'rb')
###The pdfReader variable is a readable object that will be parsed
##pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
###discerning the number of pages will allow us to parse through all #the pages
##num_pages = pdfReader.numPages
##count = 0
##text = ""
###The while loop will read each page
##while count < num_pages:
##    pageObj = pdfReader.getPage(count)
##    count +=1
##    text += pageObj.extractText()
###This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
##if text != "":
##   text = text
###If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
##else:
##   text = textract.process(fileurl, method='tesseract', language='eng')
### Now we have a text variable which contains all the text derived #from our PDF file. Type print(text) to see what it contains. It #likely contains a lot of spaces, possibly junk such as '\n' etc.
### Now, we will clean our text variable, and return it as a list of keywords.
### Calling convert function and writing each chapter to the .txt file
##file2='patent1.txt'
##txtOutputFile = open(file2, 'w')
##txtOutputFile.write(text)
##txtOutputFile.close()
######
#####The word_tokenize() function will break our text phrases into #individual words
####tokens = word_tokenize(text)
#####we'll create a new list which contains punctuation we wish to clean
####punctuations = ['(',')',';',':','[',']',',']
#####We initialize the stopwords variable which is a list of words like #"The", "I", "and", etc. that don't hold much value as keywords
####stop_words = stopwords.words('english')
#####We create a list comprehension which only returns a list of words #that are NOT IN stop_words and NOT IN punctuations.
####keywords = [word for word in tokens if not word in stop_words and  not word in string.punctuation]


##PDFMINER
##from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
##from pdfminer.converter import TextConverter
##from pdfminer.layout import LAParams
##from pdfminer.pdfpage import PDFPage
##from cStringIO import StringIO
##
##def convert_pdf_to_txt(path):
##    rsrcmgr = PDFResourceManager()
##    retstr = StringIO()
##    codec = 'utf-8'
##    laparams = LAParams()
##    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
##    fp = file(path, 'rb')
##    interpreter = PDFPageInterpreter(rsrcmgr, device)
##    password = ""
##    maxpages = 0
##    caching = True
##    pagenos=set()
##
##    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
##        interpreter.process_page(page)
##
##    text = retstr.getvalue()
##
##    fp.close()
##    device.close()
##    retstr.close()
##    return text

##
##import pyPdf
##import PyPDF2
##from itertools import islice
##
##def getPDFContent(path):
## content = ""
## 
###PATH OF THE PDF FILE
## p = file("patent.pdf", "rb")
## pdf = pyPdf.PdfFileReader(p)
## num_pages = pdf.numPages
## for i in range(0, num_pages):
##     content += pdf.getPage(i).extractText()
##     content = " ".join(content.replace(u"\xa0", " ").replace(". .",".").replace(u"??","").strip().split())
## return content
## 
###OPEN THE TEXT FILE
##f= open('test.txt','w')
## 
###CALL THE FUNCTION AND PASS THE PDF FILE
##pdfl = getPDFContent("patent.pdf").encode("ascii", "ignore")
##f.write(pdfl)
##f.close()
##with open('Text_Files\Patent.txt', 'r') as fr:
##    print ('...')
##    for line in fr:
##        if line == 'ABSTRACT \n':
##            print line+''.join(islice(fr, 8))
##fr.close()

import re

with open('tes.txt') as infile, open('test2.txt', 'w') as outfile:
    copy= False
    for line in infile:
        if line.startswith('ABSTRACT \n'):
            copy = True
        elif line.startswith('BACKGROUND OF THE INVENTION \n'):
            copy = False
        elif copy:
            outfile.write(line)
            

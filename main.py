# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
#from sumy.summarizers.luhn import LuhnSummarizer
#from sumy.summarizers.text_rank import TextRankSummarizer
#from sumy.summarizers.lex_rank import LexRankSummarizer
#from sumy.summarizers.sum_basic import SumBasicSummarizer
#from sumy.summarizers.kl import KLSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
import PyPDF2
import os
import time
import shutil
import sys
import xlrd



# Helper class used to map pages numbers to bookmarks
class BookmarkToPageMap(PyPDF2.PdfFileReader):

    def getDestinationPageNumbers(self):
        def _setup_outline_page_ids(outline, _result=None):
            if _result is None:
                _result = {}
            for obj in outline:
                if isinstance(obj, PyPDF2.pdf.Destination):
                    _result[(id(obj), obj.title)] = obj.page.idnum
                elif isinstance(obj, list):
                    _setup_outline_page_ids(obj, _result)
            return _result

        def _setup_page_id_to_num(pages=None, _result=None, _num_pages=None):
            if _result is None:
                _result = {}
            if pages is None:
                _num_pages = []
                pages = self.trailer["/Root"].getObject()["/Pages"].getObject()
            t = pages["/Type"]
            if t == "/Pages":
                for page in pages["/Kids"]:
                    _result[page.idnum] = len(_num_pages)
                    _setup_page_id_to_num(page.getObject(), _result, _num_pages)
            elif t == "/Page":
                _num_pages.append(1)
            return _result

        outline_page_ids = _setup_outline_page_ids(self.getOutlines())
        page_id_to_page_numbers = _setup_page_id_to_num()

        result = {}
        for (_, title), page_idnum in outline_page_ids.items():
            result[title] = page_id_to_page_numbers.get(page_idnum, '???')
        return result

def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
  #  Check :  print ('converting......')
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

##########################  Main Program   ########################

#Set parameters
LANGUAGE = "English"
SENTENCES_COUNT = 30
sourcePDFFile = sys.argv[1]
outputPDFDir = sys.argv[2]
outputTXTDir = sys.argv[3]
outputSummaryDir = sys.argv[4]
outputNamePrefix = 'Split_Chapter'
targetPDFFile = 'temppdfsplitfile.pdf' # Temporary file

# Append backslash to output dir ofor pdf if necessary
if not outputPDFDir.endswith('\\'):
    outputPDFDir = outputPDFDir + '\\'

# Append backslash to output dir for txt if necessary
if not outputTXTDir.endswith('\\'):
    outputTXTDir = outputTXTDir + '\\'

# Append backslash to output dir ofor pdf if necessary
if not outputSummaryDir.endswith('\\'):
    outputSummaryDir = outputSummaryDir + '\\'

#Check and Verify if PDF is ready for splitting
while not os.path.exists(sourcePDFFile):
    print('Source PDF not found, sleeping...')
    #Sleep
    time.sleep(10)
    
if os.path.exists(sourcePDFFile):
    print('Found source PDF file')
    #Copy file to local working directory
    shutil.copy(sourcePDFFile, targetPDFFile)

    #Process file
    #Create object and Open File in Read Binary Mode
    pdfFileObj2 = open(targetPDFFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj2)
    pdfFileObj = BookmarkToPageMap(pdfFileObj2)

    #Get total pages
    numberOfPages = pdfReader.numPages

    i = 0
    newPageNum = 0
    prevPageNum = 0
    newPageName = ''
    prevPageName = ''

    for p,t in sorted([(v,k) for k,v in pdfFileObj.getDestinationPageNumbers().items()]):
        template = '%-5s  %s'
    #   To Check Page number and Title of the Chapter Uncomment the following lines
    ##  print (template % ('Page', 'Title'))
    ##  print (template % (p+1,t))
        
        newPageNum = p + 1
        newPageName = t

        if prevPageNum == 0 and prevPageName == '':
         #  First Page
            prevPageNum = newPageNum
            prevPageName = newPageName
        else:
           # Next Page
            pdfWriter = PyPDF2.PdfFileWriter()
            page_idx = 0 
            for i in range(prevPageNum, newPageNum):
                pdfPage = pdfReader.getPage(i-1)
                pdfWriter.insertPage(pdfPage, page_idx)
        #   Check : print('Added page to PDF file: ' + prevPageName + ' - Page #: ' + str(i))
                page_idx+=1

        #   Creating names of split files      
            pdfFileName = outputNamePrefix + str(str(prevPageName).replace(':','_')).replace('*','_') + '.pdf'
            txtFileName = outputNamePrefix + str(str(prevPageName).replace(':','_')).replace('*','_') + '.txt'

        #   Writing each chapter to the .pdf file 
            pdfOutputFile = open(outputPDFDir + pdfFileName, 'wb') 
            pdfWriter.write(pdfOutputFile)
            pdfOutputFile.close()
            
        #   Check : print('Created PDF file: ' + outputPDFDir + pdfFileName)

        #   Calling convert function and writing each chapter to the .txt file
            txtOutputFile = open(outputTXTDir + txtFileName, 'w')
            txtOutputFile.write(convert(outputPDFDir + pdfFileName))
            txtOutputFile.close()
        #   Check :print('Created TXT file: ' + outputTXTDir + txtFileName)
        
        #   for plain text files create Summary 
            parser = PlaintextParser.from_file(outputTXTDir + txtFileName, Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)
        #   Using LsaSummarizer to create summary
        ##  We can choose Different algorithms to create summary by using different algorithms 
            summarizer = LsaSummarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)
        #   Open file in append mode so that summary will be added at the bottom of file 
            summaryOutputFile = open(outputSummaryDir + 'SummaryFile' + str(time.strftime("%d_%m_%Y_%H_")) + '.txt','a')
            for sentence in summarizer(parser.document, SENTENCES_COUNT):
        #   Check : print (sentence)
                summaryOutputFile.write(str(sentence))

        #   To create Separation between Chapters
            summaryOutputFile.write('\n\n'+ 'Title : '+str(t)+'\n'+'\t')
            summaryOutputFile.close()
            
        #   Check : print('Created TXT file: ' + outputSummaryDir + 'SummaryFile.txt')
                     
        i = prevPageNum
        prevPageNum = newPageNum
        prevPageName = newPageName

    # Split the last page
    pdfWriter = PyPDF2.PdfFileWriter()
    page_idx = 0 
    for i in range(prevPageNum, numberOfPages + 1):
        pdfPage = pdfReader.getPage(i-1)
        pdfWriter.insertPage(pdfPage, page_idx)
    #   Check : print('Added page to PDF file: ' + prevPageName + ' - Page #: ' + str(i))
        page_idx+=1
       
    pdfFileName = outputNamePrefix + str(str(prevPageName).replace(':','_')).replace('*','_') + '.pdf'
    txtFileName = outputNamePrefix + str(str(prevPageName).replace(':','_')).replace('*','_') + '.txt'
    pdfOutputFile = open(outputPDFDir + pdfFileName, 'wb')
    txtOutputFile = open(outputTXTDir + txtFileName, 'w')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()
    # Check : print('Created PDF file: ' + outputPDFDir + pdfFileName)
    txtOutputFile.write(convert(outputPDFDir + pdfFileName))
    # Check : print('Created TXT file: ' + outputTXTDir + txtFileName)
    txtOutputFile.close()
    pdfFileObj2.close()

    # Delete temp file
    os.unlink(targetPDFFile)



    


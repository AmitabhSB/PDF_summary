##
##from pdfminer.layout import LAParams
##from pdfminer.converter import PDFPageAggregator
##from pdfminer.pdfparser import PDFParser
##from pdfminer.pdfdocument import PDFDocument
##from pdfminer.pdfpage import PDFPage
##from pdfminer.pdfpage import PDFTextExtractionNotAllowed
##from pdfminer.pdfinterp import PDFResourceManager
##from pdfminer.pdfinterp import PDFPageInterpreter
##from pdfminer.pdfdevice import PDFDevice
##
##from pdfminer.pdfparser import PDFParser
##from pdfminer.pdfdocument import PDFDocument
##import sys
##
### Open a PDF file.
##fp = open("/home/amitabh/Documents/PDF_Summary/pdf/US6122455.pdf", 'rb')
### Create a PDF parser object associated with the file object.
##parser = PDFParser(fp)
### Create a PDF document object that stores the document structure.
### Supply the password for initialization.
##document = PDFDocument(parser)
### Check if the document allows text extraction. If not, abort.
##if not document.is_extractable:
##    raise PDFTextExtractionNotAllowed
### Create a PDF resource manager object that stores shared resources.
##rsrcmgr = PDFResourceManager()
### Create a PDF device object.
##device = PDFDevice(rsrcmgr)
### Create a PDF interpreter object.
##interpreter = PDFPageInterpreter(rsrcmgr, device)
### Process each page contained in the document.
##for page in PDFPage.create_pages(document):
##    interpreter.process_page(page)
##    print page
### Set parameters for analysis.
##laparams = LAParams()
### Create a PDF page aggregator object.
##device = PDFPageAggregator(rsrcmgr, laparams=laparams)
##interpreter = PDFPageInterpreter(rsrcmgr, device)
##for page in PDFPage.create_pages(document):
##    interpreter.process_page(page)
##    # receive the LTPage object for the page.
##    layout = device.get_result()
##    print layout
##
### Get the outlines of the document.
##outlines = document.get_outlines()
##for (level,title,dest,a,se) in outlines:
##    print (level, title)

# importing required modules
import PyPDF2
 
# creating a pdf file object
pdfFileObj = open('/home/amitabh/Documents/PDF_Summary/pdf/US6122455.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
# creating a page object
pageObj = pdfReader.getPage(0)
 
# extracting text from page
print(pageObj.extractText())
 
# closing the pdf file object
pdfFileObj.close()

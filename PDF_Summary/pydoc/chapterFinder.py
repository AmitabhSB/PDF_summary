from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from PyPDF2 import PdfFileWriter, PdfFileReader

import re


f = open('sc.txt','w')    
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    print 'converting......'
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

def get_toc(pdf_path):
    infile = open(pdf_path, 'rb')
    parser = PDFParser(infile)
    document = PDFDocument(parser)
    pages = dict( (page.pageid, pageno) for (pageno,page)
                  in enumerate(PDFPage.create_pages(document)) )
    toc = list()
    for (level,title,dest,a,structelem) in document.get_outlines():
        toc.append((level, title,a))

    return toc


toc= get_toc('sc.pdf')
print toc
for i in toc:
    print i
f.write(convert('sc.pdf'))
f.close()
print 'done'

##
##import io
##from PIL import Image
##import pytesseract
##from wand.image import Image as wi
##
##def pdfImgToTxt(filename):
##        pdf = wi(filename=str(filename), resolution = 300)
##        pdfImage = pdf.convert('jpeg')
##        fname='sample.pdf'
##        pdfObj = open(fname,'wb')
##        imageBlobs = []
##
##        for img in pdfImage.sequence:
##                imgPage = wi(image = img)
##                imageBlobs.append(imgPage.make_blob('jpeg'))
##
##        recognized_text = []
##
##        for imgBlob in imageBlobs:
##                im = Image.open(io.BytesIO(imgBlob))
##                text = pytesseract.image_to_string(im, lang = 'eng')
##                recognized_text.append(text)
##                pdfObj.write(str(recognized_text))
##                
##        pdfObj.close()
##
##filepath=raw_input('Enter path to the file \n')
##name=raw_input('Enter file name \n')
##pdfImgToTxt(filepath+name)
##
##
##def convert(fname, pages=None):
##    infile = file(fname, 'rb')
##    content=""
##    parser =PDFParser(infile)
##    document=PDFDocument(parser)
##    # This will give you the count of pages
##    count= (resolve1(document.catalog['Pages'])['Count'])
##    if not pages:
##        pagenums = set()
##    else:
##        pagenums = count
##  #  Check :  print ('converting......')
##    codec = 'utf-8'
##    laparams = LAParams()
##    output = StringIO()
##    manager = PDFResourceManager()
##    converter = TextConverter(manager, output,codec=codec, laparams=laparams)
##    interpreter = PDFPageInterpreter(manager, converter)
##
##    for page in PDFPage.get_pages(infile, pagenums):
##        interpreter.process_page(page)
##        
##    infile.close()
##    converter.close()
##    text = output.getvalue()
##    output.close
##    return text
##
####
####
####from wand.image import Image
####from PIL import Image as PI
####import pyocr
####import pyocr.builders
####import io
####
####tool = pyocr.get_available_tools()[0]
####lang = tool.get_available_languages()[1]
####
####req_image = []
####final_text = []
####
####image_pdf = Image(filename="pat1.pdf", resolution=300)
####image_jpeg = image_pdf.convert('jpeg')
####
####for img in image_jpeg.sequence:
####    img_page = Image(image=img)
####    req_image.append(img_page.make_blob('jpeg'))
####
####for img in req_image: 
####    txt = tool.image_to_string(
####        PI.open(io.BytesIO(img)),
####        lang=lang,
####        builder=pyocr.builders.TextBuilder()
####    )
####    final_text.append(txt)
####
##
##
#### Using pypdfocr library
##
from pypdfocr.pypdfocr import PyPDFOCR

if __name__ == '__main__':
   converter = PyPDFOCR()
   converter.go(['pat2.pdf'])



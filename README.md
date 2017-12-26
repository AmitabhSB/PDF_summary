Reads a PDF file of any book and writes summary of each chapter in 1 page.

##PDF_Summary 

Assumption : 
The book is not a scanned pdf.
The book has bookmarks or has table of content page or the chapters are distinguishable.

Read more about Pdf : https://www.abbyy.com/en-eu/finereader/pdf-types/

Updated version can be found at https://github.com/AmitabhSB/PDF_summary

Installation  Requirements :

(Tested on Windows 10)

Make sure you have [Python](http://www.python.org/) 2.7/3.3+ and
[pip](https://crate.io/packages/pip/)
([Windows](http://docs.python-guide.org/en/latest/starting/install/win/),
[Linux](http://docs.python-guide.org/en/latest/starting/install/linux/))
 
1. Install Sumy :
	
For windows cmd :
>python -m pip install sumy

2. Install PdfMiner :

For windows cmd :
>python -m pip install pdfminer

3. Install PyPDF2 :
For windows cmd :
>python -m pip install PyPDF2
Running program from Command Prompt (windows)

Input Arguments :

main.py is a program written in python that takes input arguments and gives output Summary of every Chapter.

Running program from Command Prompt (windows)

Step 1 : Go into PDF_Summary folder where you will find “main.py” python file.

Step 2 : run command 

Example :
 C:\Users\AMITABH\Desktop\PDF_Summary>main.py 

Step 3 : Input Arguments :
1 Source PDF file with path 
	Example : C:\Users\AMITABH\Desktop\PDF_Summary\pdf\short _stories.pdf 
2 Path to the output directory 
	Example : C:\Users\AMITABH\Desktop\PDF_Summary
3 Choose Algorithm from the following to create Summary . Every Algorithm works differently so it may result different output.
Select Algorithm
 press 1 and enter for Luhn.
 press 2 and enter for Lsa.
 press 3 and enter for LexRank.
 press 4 and enter for TextRank.
 press 5 and enter for SumBasic.
 press 6 and enter for KLsum.
 press 0 and enter to exit.
0
Wrong Algorithm selected.

Note : You can read more about algorithms, References are given in Documentation
Default Algorithm used is Lsa


Step 4 : You can check a Summary is created in Summary folder with file name indicating algorithm used as prefix and time stamp as suffix.


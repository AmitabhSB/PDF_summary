# PDF_summary
A python 2.7 program that reads a PDF file of any book and write summary of each chapter in 1 page.

Reads a PDF file of any book and writes summary of each chapter in 1 page.

##PDF_Summary 

##Installation  Requirements :

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

##Input Arguments :

main.py is a program written in python that takes input arguments as : 

1 Source PDF file with path 
	Example : "C:\Users\AMITABH\Desktop\PDF_Summary\pdf\short _stories.pdf" 
2 Path to the directory where PDF split files of every chapter are saved in .pdf format .
	Example : "C:\Users\AMITABH\Desktop\PDF_Summary\pdf\pdf_split_files" 
 3 Path to the directory where PDF split files of every chapter are saved in .txt format .
	Example : "C:\Users\AMITABH\Desktop\PDF_Summary\Text_files"
4 Path to the directory where Saummary of all the chapters are saved in .txt format .
	Example : "C:/Users/AMITABH/Desktop/PDF_Summary/Summary//"

and gives output Summary of every Chapter.

## Running program from Command Prompt (windows)

Step 1 : Go into PDF_Summary folder where you will find “main.py” python file.

Step 2 : run command 

Example :
 C:\Users\AMITABH\Desktop\PDF_Summary>main.py  “C:\Users\AMITABH\Desktop\PDF_Summary\pdf\short _stories.pdf" "C:\Users\AMITABH\Desktop\PDF_Summary\pdf\pdf_split_files" "C:\Users\AMITABH\Desktop\PDF_Summary\Text_files" "C:/Users/AMITABH/Desktop/PDF_Summary/Summary"

Step 3 : You can check a Summary.txt file is created in Specified folder.




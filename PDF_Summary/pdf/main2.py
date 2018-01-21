import operator
import numpy as np
import matplotlib.pyplot as plt
import obo
import textract

path = raw_input('Enter the path of the pdf file (eg. C:/Games/abc.pdf)') 

#Processing PDF file into text.
text = textract.process(path).replace('\n', ' ')
#Making a list of words. Removing NonAlphaNumeric Characters.
fullwordlist = obo.stripNonAlphaNum(text)


#WorlList to FreqList
dictionary = obo.wordListToFreqDict(fullwordlist)
#Sorted WOrdList with freq
sorteddict = obo.sortFreqDict(dictionary)

myDictionary = sorteddict
#Creating a dictionary 
dick = {}
for some in myDictionary:
	dick[some[1]] = some[0]

d = {} 
sorted_x = sorted(dick.items(), key=operator.itemgetter(1))
#Printing Top 10 Words in the file.
print 'The top 10 words in the given file by frequency are as follows:'
for i in range(len(sorted_x)-10,len(sorted_x)):
	d[sorted_x[i][0]] = sorted_x[i][1]

sorted_y = sorted(d.items(), key=operator.itemgetter(1))
print sorted_y

#Plotting Histogram
X = np.arange(len(d))
plt.bar(X, d.values(),  width=1.0)
plt.xticks(X, d.keys(), rotation='vertical')
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
ymax = max(d.values()) + 1
plt.ylim(0, ymax)
plt.show()

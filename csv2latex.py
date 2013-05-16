import os, sys, csv
 
def makeRow(row, header=False, indices=0):
 
    if header:
        # Make header bold
        row = ['\\textbf{%s}' % x for x in row]
    else:
        # Make italic indices
        row = ['\\textit{%s}' % x for x in row[:indices]] + row[indices:]
 
    latexRow = row[0]
    for col in row[1:]:
        latexRow += ' & ' + col
    latexRow += ' \\\\ \\hline'
    return latexRow
 
def getAllign(count, allignment='l'):
    format = '|'
    for i in range(count):
        format += 'l|'
    return format
 
# index_cols = list of columns to be used as index
# cols: type([int]) or type([string])
def makeLatex(index_cols, cols, data, header=True):
    indices = len(index_cols)
    latex = []
    rows = range(len(data))
 
    for row in rows:
        latex.append([])
        maxCol = len(data[row])
        for idx in index_cols + cols:
            if idx < maxCol:
                latex[row].append(data[row][idx].replace('_', '\\_'))
    temp = [makeRow(latex[0],True)] if header else []
    temp += [makeRow(x,indices=indices) for x in latex[1:]]
 
    latex = temp
    format = getAllign(len(index_cols) + len(cols))
    print '\\begin{tabular}{ %s }' % format
    print '\\hline'
    for row in latex:
        print row
    print '\\end{tabular}'
 
def csv2array(input_file, delim=','):
    array = []
    with open(input_file, 'rUb') as f:
        reader = csv.reader(f, delimiter=delim)
        for row in reader:
            array.append(row)
    return array
 
location = '/Users/arvind/Downloads'
filename = 'm2.csv'
array = csv2array(os.path.join(location,filename))
makeLatex([0,1],range(2,6), array)
makeLatex([0,1],range(6,12), array)
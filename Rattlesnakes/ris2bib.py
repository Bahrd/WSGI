## RIS to BIB converter (from standard input to standard output) 
#  ver. 0.1 (only the most popular entries are handled)
#  See: http://www.bibtex.org/Format/ and https://www.bibtex.com/e/entry-types/ or
#       https://en.wikipedia.org/wiki/RIS_(file_format)
import re, sys
from datetime import datetime as dt

k2k = {  'TI': 'title',   'VL': 'volume', 'JO': 'journal', 'PB': 'publisher',
         'PP': 'address', 'ED': 'editor', 'IS': 'issue', 'SER': 'series',
         'DO': 'doi',     'UR': 'url', 'PY': 'year'}
types = {'JOUR': 'article', 'CONF': 'inproceedings', 'EDBOOK': 'booktitle', 
         'BOOK': 'book',    'CHAP': 'incollection'}
bib, id, type, short = {}, '', '', True

def flush(bib, ind = 4 * ' '):
    print(f'@{type}' + '{' + f'{id},')          # header
    for k in bib: 
        print(ind + k + ' = {' + bib[k] + '},') # body
    print('}')                                  # footer
    bib.clear(); return bib                     # call it a day

## Line-by-line translation (would that be easier with lex/yacc?)  
for line in sys.stdin: 
    kv = re.split('\s{2}-\s+', line.rstrip())
    match kv:
        case [k, v] if k in k2k:bib[k2k[k]] = v
        case ['TY', v]: type = types[v] if v in types else 'misc'
        case ['AB', v]: bib['abstract'] = re.match('[^\.]+\.', v).group(0) if short else v
        case ['SP', v]: bib['pages'] = v
        case ['EP', v]: bib['pages'] += ' - ' + v
        case ['ID', v]: id = v
        case ['AU', v]: 
            if 'author' in bib: bib['author'] += ' and ' + v
            else:               bib['author'] = v
        case ['ER  -']: bib = flush(bib)
        case _: pass
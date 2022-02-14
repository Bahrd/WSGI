## RIS to BIB converter (from standard input to standard output) 
#  ver. 0.1 (only the most popular entries are handled)
#  See: http://www.bibtex.org/Format/ and https://www.bibtex.com/e/entry-types/ or
#       https://en.wikipedia.org/wiki/RIS_(file_format)
import re, sys
from datetime import datetime as dt

k2k = {  'TI': 'title',   'VL': 'volume', 'JO': 'journal', 'PB': 'publisher',
         'PP': 'address', 'ED': 'editor', 'IS': 'issue', 'SER': 'series',
         'DO': 'doi',     'UR': 'url', 'PY': 'year', 'AB': 'abstract'}
types = {'JOUR': 'article', 'CONF': 'inproceedings', 'EDBOOK': 'booktitle', 
         'BOOK': 'book',    'CHAP': 'incollection'}
bib, id, type = {}, '', ''

def flush(bib, ind = 4 * ' '):
    print(f'@{type}' + '{' + f'{id},')           # header:   '@type{id.'
    for key, value in bib.items(): 
        print(ind + key + ' = {' + value + '},') # body:     'entry = {value},'
    print('}')                                   # footer:   ','    
    bib.clear(); return bib                      # call it a day

## Line-by-line translation (would it be a bit easier with lex/yacc?)  
#  If the abstract is a bit lengthy, one can strip it to the first sequence:
#  'case ['AB', v]: bib['abstract'] = re.match('[^\.]+\.', v).group(0)'

for line in sys.stdin: 
    match re.split('\s{2}-\s+', line.rstrip()):     # Only if sys.version_info >= (3, 10)
        # the standard one-line items conversion
        case [k, v] if k in k2k: bib[k2k[k]] = v

        # all these items need a special handling
        case ['TY', v]: type = types[v] if v in types else 'misc'
        case ['SP', v]: bib['pages'] = v
        case ['EP', v]: bib['pages'] += ' - ' + v
        case ['ID', v]: id = v
        case ['AU', v]: 
            if 'author' in bib: bib['author'] += ' and ' + v
            else:               bib['author'] = v
        case ['ER  -']: bib = flush(bib)

        # all the remaining ones are just ignored
        case _: pass
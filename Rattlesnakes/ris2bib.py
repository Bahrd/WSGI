## RIS to BIB converter (from standard input to standard output) 
#  ver. 0.π (only the most popular entries are handled)
#  See: http://www.bibtex.org/Format/ and https://www.bibtex.com/e/entry-types/ or
#       https://en.wikipedia.org/wiki/RIS_(file_format)
import re, sys
from datetime import datetime as dt

# names of BibTeX item fields
k2k = {  'TI': 'title',   'VL': 'volume', 'JO': 'journal', 'PB': 'publisher',
         'PP': 'address', 'ED': 'editor', 'IS': 'issue', 'SER': 'series',
         'DO': 'doi',     'UR': 'url', 'PY': 'year', 'AB': 'abstract'}
# types of BibTeX items
types = {'JOUR': 'article', 'CONF': 'inproceedings', 'EDBOOK': 'booktitle', 
         'BOOK': 'book',    'CHAP': 'incollection', 'RPRT':	'report'}
          # bibitem fields, value used when there is no ID, default bibitem type
default = {}, 'NN', 'misc' 

b, i, t = default
def flush(b, w = 4 * ' '):
    print(f'@{t}' + '{' + i + ',')       # header:  '@type{id.'
    for k, v in b.items(): 
        print(w + k + ' = {' + v + '},') # body:    'entry = {value},'
    print('}')                           # footer:  ','    
    b.clear()                            # Call it a day!

## Line-by-line translation (would that be easier with a lex/yacc combo?)  
#  If the abstract is a bit lengthy, one can extract the first sequence instead:
#  'case ['AB', v]: bib['abstract'] = re.match('[^\.]+\.', v).group(0)'

for line in sys.stdin: 
    match re.split('\s{2}-\s+', line.rstrip()):     # Only if sys.version_info >= (3, 10)
        # The standard one-line field conversion
        case [k, v] if k in k2k: b[k2k[k]] = v

        # The fields that need a special handling
        case ['TY', v]  if v in types: t = types[v] 
        case ['SP', v]: b['pages'] = v
        case ['EP', v]: b['pages'] += ' - ' + v
        case ['ID', v]: i = v
        case ['AU', v]: 
            if 'author' in b: b['author'] += ' and ' + v
            else:             b['author'] = v
        case ['ER  -']: 
            flush(b)
            b, i, t = default
        # All the remaining fields are ignored
        case _: pass
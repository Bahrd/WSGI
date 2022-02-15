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
## Initialization tuple: 
#  dictionary of bibitem fields
#  placeholder in case of the lack of ID field
#  default bibitem type
default = {}, 'NN', 'misc' 

b, i, t = default
def flush(w = 4 * ' '):                  # 'w' is an indentation parameter
    print(f'@{t}' + '{' + i + ',')       # header:  '@type{id.'
    for k, v in b.items(): 
        print(w + k + ' = {' + v + '},') # body:    'entry = {value},'
    print('}')                           # footer:  ','    
    b.clear()                            # Call it a day!

## Line-by-line translation (no need for a lex/yacc combo?)  
for line in sys.stdin: 
    match re.split('\s{2}-\s+', line.rstrip()):     # Only if sys.version_info >= (3, 10)
        # The standard one-to-one line field conversions
        case [k, v] if k in k2k: b[k2k[k]] = v

        # The fields that need a special handling
        case ['TY', v]  if v in types: t = types[v] 
        case ['ID', v]: i = v
        case ['AU', v]: 
            if 'author' in b: b['author'] += ' and ' + v
            else:             b['author'] = v
        case ['SP', v]: b['pages'] = v
        case ['EP', v]: b['pages'] += ' - ' + v
        case ['ER  -']: flush(); b, i, t = default
        # The remaining fields are ignored (in this version)
        case _: pass
#  ------
#  * If the abstract is a bit lengthy, one can extract the first sequence instead:
#    'case ['AB', v]: bib['abstract'] = re.match('[^\.]+\.', v).group(0)'
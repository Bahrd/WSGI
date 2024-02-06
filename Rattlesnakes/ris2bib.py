## RIS to BIB converter (from standard input to standard output) 
#  ver. 0.π (only the most popular entries are handled)
#  See: http://www.bibtex.org/Format/ and https://www.bibtex.com/e/entry-types/ or
#       https://en.wikipedia.org/wiki/RIS_(file_format)
from sys import stdin
from re import split, match

# Selected RIS entries and their BibTeX counterparts
k2k = {  'TI': 'title',   'VL': 'volume', 'JO': 'journal', 'PB': 'publisher',
         'PP': 'address', 'ED': 'editor', 'IS': 'issue', 'SER': 'series',
         'DO': 'doi',     'UR': 'url', 'PY': 'year', 'AB': 'abstract'}
# Types of BibTeX items
types = {'JOUR': 'article', 'CONF': 'inproceedings', 'EDBOOK': 'booktitle', 
         'BOOK': 'book',    'CHAP': 'incollection', 'RPRT':	'report'}
## Initialization tuple: 
#  + dictionary of bibitem fields
#  + placeholder in case of the lack of ID field
#  + default bibitem type
default = 'NN', 'misc'
b, (i, t) = {}, default

def flush(b, w = 4 * ' '):               # 'w' is an indentation
    print(f'@{t}' + '{' + i + ',')       # header:  '@type{id.'
    for k, v in b.items(): 
        print(w + k + ' = {' + v + '},') # body:    'entry = {value},'
    print('}')                           # footer:  ','    
    b.clear()                            # Call it a day!

## Line-by-line translation (no need for a lex/yacc combo?)  
for line in stdin: 
    match split('\\s{2}-\\s+', line.rstrip()):  
        # The standard one-to-one line field conversions
        case [k, v] if k in k2k: b[k2k[k]] = v

        # The fields with a bit more elaborated semantics
        case ['TY', v]  if v in types: t = types[v] 
        case ['ID', v]: i = v
        case ['AU', v]: 
            if 'author' in b: b['author'] += ' and ' + v
            else:             b['author'] = v
        case ['SP', v]: b['pages'] = v
        case ['EP', v]: b['pages'] += ' - ' + v
        case ['ER  -']: flush(b); i, t = default
        # The 'ignoramus et ignorabimus' fields
        case _: pass
#  ------
#  * If the abstract is a bit lengthy, one can extract the first sequence instead (insert the line below as the first):
#    'case ['AB', v]: b['abstract'] = match('[^\\.]+\\.', v).group(0)'

#  ** The commands 'chcp 65001' and 'Get-Content -Encoding UTF8 bla-bla.ris | python ris2bib.py' are sometimes useful.
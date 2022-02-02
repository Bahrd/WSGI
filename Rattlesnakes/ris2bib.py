## RIS to BIB converter (from standard input to standard output)
#  Cf. https://www.bruot.org/ris2bib/
#      http://www.bibtex.org/Format/

import re, sys
from datetime import datetime as dt

short, bibitem, authors = True, {}, []
def author_handler(author): 
    global authors
    authors.append(author)
    bibtex_authors = ''
    if(len(authors) > 1):
        bibtex_authors += authors[0]
        for author in authors[1:]:
            bibtex_authors += ' and ' + author 
    else:
        bibtex_authors += author
    return bibtex_authors

pages = ''
def pages_handler(page, key):
    global pages
    if(key == 'SP'):
        pages += page + '-'
    else:
        pages += page
    return pages

item_type, typeid = {'JOUR': 'article', 
                     'CONF': 'inproceedings', 
                     'BOOK': 'book',
                     'CHAP': 'incollection'}, ''
def typeid_handler(type_id, key, short = short):
    global typeid
    if(key == 'TY'):typeid = item_type[type_id] + '{'
    else:           typeid += type_id[:4] + ':' + type_id[-4:] if(short) else type_id
    return typeid

abstract_handler = lambda abstract, short = True: re.match('[^\.]+\.', abstract).group(0) if(short) else abstract 
em_brace = lambda tag: '{' + tag + '}'
# Basics...
handler = {'ID': lambda id:         '@' + typeid_handler(id, 'ID'),
           'TY': lambda type:             typeid_handler(type, 'TY'),
                
           'TI': lambda title:      'title     = ' + em_brace(title),
           'AU': lambda author:     'author    = ' + em_brace(author_handler(author)),
           'JO': lambda journal:    'journal   = ' + em_brace(journal),
           'VL': lambda volume:     'volume    = ' + em_brace(volume),
           'IS': lambda issue:      'issue     = ' + em_brace(issue),
           'SP': lambda start_page: 'pages     = ' + em_brace(pages_handler(start_page, "SP")),
           'EP': lambda end_page:   'pages     = ' + em_brace(pages_handler(end_page, "EP")),
           'PY': lambda year:       'year      = ' + em_brace(year),
           'PB': lambda publisher:  'publisher = ' + em_brace(publisher),
           'PP': lambda address:    'address   = ' + em_brace(address),
           'ED': lambda editor:     'editor    = ' + em_brace(editor)}
# ... and extras
handler.update({'AB': lambda abstract:   'abstract  = ' + em_brace(abstract_handler(abstract)),
                'UR': lambda url:        'url       = ' + em_brace(url),
                'DO': lambda doi:        'doi       = ' + em_brace(doi)})

## Line-by-line translation (would that be easier with lex/yacc?)  
for line in sys.stdin: 
    key_value = re.split('\s{2}-\s+', line.rstrip())
    if(len(key_value) > 1):  
        key, value = key_value
        try: bibitem[key] = handler[key](value)
        except KeyError: continue

## A bit of output massaging (hand-crafting)
if "ID" in bibitem: print(f'{bibitem["ID"]},'), bibitem.pop('ID')
else:               print(f'@{bibitem["TY"]}ID:{dt.now().strftime("%f")},')
#  Seed and chaff separation...
bibitem.pop('SP'), bibitem.pop('TY')
# ... and the plain rest...
for item in bibitem: print(f'\t{bibitem[item]},')
# ... ♫ to the end of file! ♫
print('}')
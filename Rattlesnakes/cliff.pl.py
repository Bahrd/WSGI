from sys import stdin
from regex import sub

## Line-by-line translation (no need for a lex/yacc combo?)  
with open(r'.\bib\izi.pl.tex', mode = "w", encoding = "utf-8") as tex:
    for line in stdin:
        newline = sub(r'\\l ', 'ł', line)
        newline = sub(r'\\k\{e\}', 'ę', newline)
        newline = sub(r'\\k\{a\}', 'ą', newline)
        newline = sub(r'\\\'\{z\}', 'ź', newline)
        newline = sub(r'\\\'\{o\}', 'ó', newline)
        newline = sub(r'\\\'\{c\}', 'ć', newline)
        newline = sub(r'\\\'\{n\}', 'ń', newline)
        newline = sub(r'\\\.\{z\}', 'ż', newline)
        tex.write(newline)
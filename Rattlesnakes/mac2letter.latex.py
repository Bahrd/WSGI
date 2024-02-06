from sys import stdin, stdout
from re import sub

## A LaTeX-macro-to-Polish-letter converter (e.g. \k{a} -> ą)
#  Don't forget to add:
#  \usepackage[T1]{fontenc}
#  \usepackage[utf8]{inputenc}
#  to the preamble of your LaTeX document

#  Usage: cat [input_file] | [python_path] mac2letter.latex.py > [output_file]

# https://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python
stdout.reconfigure(encoding = 'utf-8')

# The dictionary of Polish characters in LaTeX
# a.k.a. backslash counting...
patterns = (r'\\[lL]\ ', r'\\[lL]\{\}', r'\\k\{[aeAE]\}',
            r'\\\'\{[szoncSZONC]\}',    r'\\\.\{zZ\}')
codebook = {r'\'{S}': 'Ś', r'\'{O}': 'Ó', r'\'{C}': 'Ć', r'\'{N}': 'Ń', r'\'{Z}': 'Ź',
            r'\'{s}': 'ś', r'\'{o}': 'ó', r'\'{n}': 'ń', r'\'{c}': 'ć', r'\'{z}': 'ź',
            r'\k{e}': 'ę', r'\k{a}': 'ą', r'\k{E}': 'Ę', r'\k{A}': 'Ą',
            r'\.{z}': 'ż', r'\.{Z}': 'Ż',
            r'\l ': 'ł', r'\L ': 'Ł', r'\l{}': 'ł', r'\L{}': 'Ł'}

for line in stdin:
    for pattern in patterns:
        line = sub(pattern, lambda txt: codebook[txt.group(0)], line)
    print(line, end = '')

''' #For those who prefer writing to a file: remember seeting encoding to utf-8
    with open([full_path], mode = "w", encoding = "utf-8") as tex:
        for line in stdin:
            ...
            tex.write(newline)
'''
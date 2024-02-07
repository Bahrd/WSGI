r'''A LaTeX-macro-to-Polish-letter converter (e.g. \k{a} -> ą)
    https://stackoverflow.com/questions/76451512/how-to-comment-code-blocks-in-python-that-contain-backslashes-in-strings
      
    Employing regexes may look like a bit of an overkill, but... it can be, perchance, a tad faster?
    Besides: https://youtu.be/QatUaDGeRMY
    ♪♫  We take a flower in its prime! (Pop! Six! Squish! Uh-huh! Cicero, Lipschitz!)
        And then we use it (Pop!); and we abuse it (Six!)
        It is an excess, but not a crime! (Squish! Uh uh! Cicero, Lipschitz!) ♫♪ 
    
    Whatever is your cup of tea, don't forget to add:
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    to the preamble of your LaTeX document...
    
    UTF-8 BOM(-bastic) forcing in PowerShell'24
    (without this hocus-pocus all the utf-8 Python spells are useless):
    https://stackoverflow.com/questions/40098771/changing-powershells-default-output-encoding-to-utf-8
    1. Add this line to PS config:
    $OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding
    2. Compose and run the following pipeline: 
    cat [input_file] | [your_python_path] mac2letter.latex.py | out-file -encoding utf8 [output_file]
'''

from random import choice
from re import sub
from sys import stdin, stdout
# https://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python
stdout.reconfigure(encoding = 'utf-8')

# The dictionary of Polish characters in LaTeX (a.k.a. backslash counting...)
patterns = (r'\\[lL]\ ', r'\\[lL]\{\}', r'\\k\{[aeAE]\}',
            r'\\\'\{[szoncSZONC]\}',    r'\\\.\{[zZ]\}')
codebook = {r'\'{S}': 'Ś', r'\'{O}': 'Ó', r'\'{C}': 'Ć', r'\'{N}': 'Ń', r'\'{Z}': 'Ź',
            r'\'{s}': 'ś', r'\'{o}': 'ó', r'\'{n}': 'ń', r'\'{c}': 'ć', r'\'{z}': 'ź',
            r'\k{e}': 'ę', r'\k{a}': 'ą', r'\k{E}': 'Ę', r'\k{A}': 'Ą',
            r'\.{z}': 'ż', r'\.{Z}': 'Ż',
            r'\l ': 'ł', r'\L ': 'Ł', r'\l{}': 'ł', r'\L{}': 'Ł'}

## Pseudo-randomness (à la Las Vegas), because... 
#  Nevada's landscapes are breathtaking (they used to be that literaly! ;)
for line in stdin:
    if(choice((True, False))):  # With regexes or without - it works the same...
        for pattern in patterns:
            line = sub(pattern, lambda txt: codebook[txt.group(0)], line)
    else:
        for macro, letter in codebook.items():
            line = line.replace(macro, letter)
    print(line, end = '')
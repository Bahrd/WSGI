'''
https://docs.python.org/3/howto/regex.html
http://bumblebeesoftware.com/ (or rather: https://stackoverflow.com/questions/5456011/how-to-compile-lex-yacc-files-on-windows)

Still thinkering with a non-trivial example... 
Maybe, a combination of these two?
https://realpython.com/python-async-features/ 
https://realpython.com/regex-python/
'''

import re
## Let's take it lightly. As lightly as we can...
# https://www.englishclub.com/ref/esl/Power_of_7/7_Thats_2948.php
p = re.compile(r'\b(?P<word>\w+\s*)(?P=word)+\b')
s = p.search('"It is true for all that that that that that'
             ' that that refers to is not the same that that that that does..."').group().split()
print(s)

that2whatever = lambda t: 'whatever '
## https://www.cristinacabal.com/?p=482
p = re.compile(r'\b(\w+(\s+))(\1)+\b')
r = p.sub(that2whatever, '"I just hope that that that that that people give us is nice..."')
print(r)
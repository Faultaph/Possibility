import sys
from functions import cleanandlexer

if len(sys.argv) < 2:
    print('Error: Missing argument for source code')
    sys.exit()

try:
    sourcecode = open(sys.argv[1], 'r')
except:
    print('Error: invalid target path for source code')
    sys.exit()
    
script = sourcecode.read()
print(script,end='')
print('\n==================')
script = cleanandlexer(script)
print(script)

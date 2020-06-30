import sys

if len(sys.argv) < 2:
    print('Error: Missing argument for source code')
    sys.exit()

sourcecode = open(sys.argv[1], 'r')
script = sourcecode.read()
print(script)

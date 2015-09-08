#!/usr/bin/env python3

import sys

code = False
for line in sys.stdin:
    if line.startswith('```'):
        if code:
            print('\n', '// ', line, sep='', end='')
        else:
            print('// ', line, '\n', sep='', end='')
        code = not code
    else:
        print('// ' if not code else '', line, sep='', end='')

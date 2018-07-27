#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Usage: generate_csv.py [options] OUTPUT_FILE

  --sep=SEP                  Specify separator
  --eol=EOL                  Specify end of line character
  --quote=QUOTE              Specify character quoting fields
  --encoding=ENCODING        Specify encoding
  --newline=NEWLINE          Specify newline character in a field
  -v                         Verbose mode
  -h, --help                 Print this help and exit
  --version                  Display program version
"""
from docopt import docopt
import csv

def get_endline_char(key):
    return {'win': '\r\n', 'unix': '\n', 'macos': '\r'}.get(key) or 'no'


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    if arguments.get('-v'):
        print(arguments)

    with open(arguments['OUTPUT_FILE'], 'wb') as csvfile:
        kw = {
            'quoting': csv.QUOTE_ALL
        }
        if arguments.get('--sep'):
            kw['delimiter'] = arguments.get('--sep')
        if arguments.get('--quote'):
            kw['quotechar'] = arguments.get('--quote')
        if arguments.get('--eol'):
            kw['lineterminator'] = get_endline_char(arguments.get('--eol'))

        writer = csv.writer(csvfile, **kw)

        newline = get_endline_char(arguments.get('--newline'))
        encoding = arguments.get('--encoding') or 'utf-8'
        for i in range(10):
            row = [u'Line {0}'.format(i), u'Field 1', u'Field 2 with {0} newline'.format(newline), u'Field àéèôùï 3']
            writer.writerow([elt.encode(encoding) for elt in row])

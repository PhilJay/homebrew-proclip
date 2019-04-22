#!/usr/bin/env python3

import argparse
import sys

from Database import Database
from Interpreter import Interpreter

if __name__ == '__main__':
    argv = sys.argv
    argv = argv[1:]  # first element of args is always the file name
    length = len(argv)
    db = Database()

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', action='store_true', help='Lists all currently stored entries')
    parser.add_argument('-s', '--store', nargs=2, help='Stores a new entry with (alias, content)')
    parser.add_argument('-r', '--remove', nargs=1, help='Removes the entry with the specified alias')
    parser.add_argument('--removeAll', action='store_true', help='Removes all entries')
    parser.add_argument('-c', '--copy', nargs=1, help='Copies the entry with the provided name to the clipboard')
    parser.add_argument('-e', '--execute', nargs=1, help='Executes the entry with the provided alias')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enables debug print')

    namespace = parser.parse_args()
    args = vars(namespace)
    args = dict((k, v) for k, v in args.items() if v is not None)

    interpreter = Interpreter(db, namespace, args)
    interpreter.interpret()

    db.close()

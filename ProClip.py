#!/usr/bin/env python

from Interpreter import Interpreter
from ClipCopy import ClipCopy
import sys, argparse, os

if __name__ == '__main__':

    argv = sys.argv
    argv = argv[1:]  # first element of args is always the file name
    length = len(argv)

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', nargs='*')
    parser.add_argument('-p', nargs='*')
    parser.add_argument('-r', nargs='*')
    parser.add_argument('-g', nargs='*')
    parser.add_argument('-c', nargs='*')
    parser.add_argument('-e', nargs='*')

    args = vars(parser.parse_args())
    args = dict((k, v) for k, v in args.items() if v is not None)
    # print(args)

    interpreter = Interpreter()
    (entry, execute, copy) = interpreter.interpret(args)

    if entry is not None:
        if execute:
            print("Executing...")
            os.system(entry.content)
        if copy:
            print("Copying to clipboard...")
            copy = ClipCopy()
            copy.copy2clipboard(entry.content)

#!/usr/bin/python

# Auto pep8: autopep8 --in-place --aggressive --aggressive

import sys

tipo = str(sys.argv[1])

lines = ""


def prompt_user():
    global lines
    global tipo
    print 'Type Intro to end.'
    while (True):
        line = raw_input('> ')
        if line == '':
            print lines
            lines = ""
            # sys.exit()
        if tipo == "c":
            lines += "echo codificar('" + line + "').'<br>';\n"
        else:
            lines += "echo " + tipo + "('" + line + "').'<br>';\n"

if __name__ == "__main__":
    prompt_user()

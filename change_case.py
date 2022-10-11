#! /usr/bin/python3
import sys
import getopt
import subprocess

def to_lower(expression: str) -> str:
    return expression.lower()

def to_upper(expression: str) -> str: 
    return expression.upper()

def capitalize(expression: str) -> str:
    return expression.capitalize()

def main(argv: list) -> str:
    argsv = argv[1:]

    options = "u:l:c:"
    long_opts = ["upper=", "lower=", "capitalize="]

    opts, args = getopt.getopt(argsv, options, long_opts)
    # print(opts, args)

    for opt, arg in opts:
        if  opt in ("-l", "--lower"):
            # print (to_lower(arg))
            #print()
            subprocess.run("xsel", universal_newlines=True, input=to_lower(arg))
        if  opt in ("-u", "--upper"):
            #print(to_upper(arg))
            subprocess.run("xsel", universal_newlines=True, input=to_upper(arg))
        if  opt in ("-c", "--capitalize"):
            #print(capitalize(arg))
            subprocess.run("xsel", universal_newlines=True, input=capitalize(arg))

                            
if __name__ == "__main__":
    main(sys.argv)
    
    

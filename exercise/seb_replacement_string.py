"""
This module contains a code for exercises 14-1 related to:
Think Python, 2nd Edition
Chapter 14: Files

Takes as arguments a pattern string, a replacementstring, and two filenames;
it should read the first file and write the contents into the
second file (creating it if necessary).
"""

import string

def sed(filename_in, filename_out, pattern, replacement):
    """
    Write to output file after replacing

    filename_in: string, name of the input file
    filename_out: string, name of the output file
    pattern: string is replaced
    replacement: replacement string
    """
    
    try:
        fin = open(filename_in, 'r')
        fout = open(filename_out, 'w')

        for line in fin:
            fout.write(line.replace(pattern, replacement))

        fout.close()
        
    except:
        print("An error occurred, please check again...")

sed('text_input', 'text_output.txt', 'et', 'zzzzz')

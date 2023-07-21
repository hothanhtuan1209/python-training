"""
This module contains a code for exercises 14-3 related to:
Think Python, 2nd Edition
Chapter 14: Files

Write a program that searches a directory and all of its subdirectories,
recur sively, and returns a list of complete paths for all files with a
given suffix (like .mp3).
"""

import os
import hashlib
import subprocess

def find_files_with_suffix(directory, suffix):
    """
    Recursively find all files with a given suffix in the specified directory and its subdirectories.

    directory: string, path to the directory to search
    suffix: string, the file suffix to look for

    returns: list of complete paths to the found files
    """
    
    files = []
    
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(suffix):
                files.append(os.path.join(root, filename))
    
    return files

def compute_checksum(filename):
    """
    Compute the checksum (MD5 hash) of a file.

    filename: string, path to the file

    returns: string, the MD5 hash of the file
    """
    
    hash_md5 = hashlib.md5()
   
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    
    return hash_md5.hexdigest()

def find_duplicates(directory, suffix):
    """
    Find duplicate files with a given suffix in the specified directory and its subdirectories.

    directory: string, path to the directory to search
    suffix: string, the file suffix to look for

    returns: dictionary
    """
    
    files = find_files_with_suffix(directory, suffix)
    checksum_to_files = {}
    duplicates = {}

    for file in files:
        checksum = compute_checksum(file)
        if checksum in checksum_to_files:
            checksum_to_files[checksum].append(file)
        else:
            checksum_to_files[checksum] = [file]

    for checksum, file_list in checksum_to_files.items():
        if len(file_list) > 1:
            duplicates[checksum] = file_list

    return duplicates

def check_duplicates(duplicates):
    """
    Check if the files with the same checksum are really
    duplicates using the Unix command diff.

    duplicates: dictionary
    """
    for checksum, file_list in duplicates.items():
        print(f"Duplicate files with checksum {checksum}:")
        for file in file_list:
            print(file)
        print("Checking for differences...")
        for i in range(len(file_list)):
            for j in range(i + 1, len(file_list)):
                subprocess.run(['diff', file_list[i], file_list[j]])

def main():
    directory_to_search = 'path/mp3/files'
    suffix_to_find = '.mp3'
    duplicates = find_duplicates(directory_to_search, suffix_to_find)
    check_duplicates(duplicates)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import argparse
import os
import random


def parse_args():
    description = 'Tool that randomly shuffles paragraphs of input file'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--file', dest='filepath', required=True,
                        help='input filepath', metavar='FILE')

    return parser.parse_args()


def shuffle_paragraphs(text):
    # Split text by paragraphs
    splitted_text = text.split('\n\n')
    # Shuffle paragraphs
    random.shuffle(splitted_text)

    return '\n\n'.join(splitted_text)


if __name__ == '__main__':
    args = parse_args()
    filepath = args.filepath

    # Check whether specified path is file
    # if not, print error message and exit
    if not os.path.isfile(filepath):
        print(f"Error: '{filepath}' file.")
        exit(1)

    with open(filepath, 'r') as file:
        shuffled_text = shuffle_paragraphs(file.read())
        print(shuffled_text)

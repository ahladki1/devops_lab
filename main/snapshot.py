#!/usr/bin/env python

from main.modules import task1
import argparse


def main():
    print("SNAPSHOTER")
    parser = argparse.ArgumentParser(description='Options for the file')
    parser.add_argument('type', type=str, help='Type for the file')
    task1.do_snapshot(parser.parse_args().type)


if __name__ == "__main__":
    main()

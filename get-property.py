#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse, sys
import yaml
from os.path import join

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to yaml file")
    parser.add_argument("property", help="yaml property")
    parser.add_argument("--default", help="fallback result")
    args = parser.parse_args()

if __name__ == "__main__":
    set_args()

    meta_file = yaml.load(open(args.path, 'r'))
    try:
        print(meta_file[args.property])
    except KeyError:
        if args.default:
            print(args.default)
        else:
            print(args.property + ' does not exists.', file=sys.stderr)
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse, sys
import yaml

def set_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to yaml file")
    parser.add_argument("property", help="yaml property")
    parser.add_argument("--default", help="fallback result")
    args = parser.parse_args()

def error(message):
    print('ERROR: ' + message, file=sys.stderr)
    exit(1)

def property(yaml, key, optional=False, default=None):
    value = yaml[key] if key in yaml else None
    if value is None:
        if optional:
            return default
        else:
            error(key + ' must be defined.')
    return value

if __name__ == "__main__":
    set_args()

    meta_file = yaml.load(open(args.path, 'r'))

    value = property(meta_file, key=args.property, optional=True, default=args.default)

    if value != None:
        print(value)
    else:
        print(args.property + ' does not exists.', file=sys.stderr)
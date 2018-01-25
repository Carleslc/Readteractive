#!/usr/bin/python3
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

def error(message, prefix='ERROR'):
    print('%s: %s' % (prefix, message), file=sys.stderr)
    exit(1)

def property(yaml, key, file, optional=False, default=None):
    try:
        value = yaml[key] if key in yaml else None
        if value is None:
            if optional:
                return default
            else:
                error(key + ' must be defined.')
        return value
    except TypeError as e:
        error(str(e), 'YAML SYNTAX ERROR [Key %s at %s]' % (key, file))

def load(file):
    try:
        return yaml.load(file)
    except (TypeError, yaml.scanner.ScannerError) as e:
        error(str(e), 'YAML SYNTAX ERROR')

if __name__ == "__main__":
    set_args()

    try:
        meta_file = load(open(args.path, 'r'))
    except FileNotFoundError:
        error('%s not found' % args.path)

    value = property(meta_file, key=args.property, file=args.path, optional=True, default=args.default)

    if value != None:
        print(value)
    else:
        print(args.property + ' does not exists.', file=sys.stderr)
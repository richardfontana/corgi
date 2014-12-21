#!/usr/bin/env python

import argparse

def get_arg_parser():
    parser = argparse.ArgumentParser(prog='corgi')

    parser.add_argument('-A', metavar='alias', nargs='+',
       dest='corgi_alias_queries', help="expand the given alias(es)")
    
    return parser


def main():
    args = get_arg_parser().parse_args()


if __name__ == '__main__':
    main()

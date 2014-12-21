#!/usr/bin/env python


import argparse


corgi_cfg = "config.yml"

alias_dict={}


def get_arg_parser():
    parser = argparse.ArgumentParser(prog='corgi')

    parser.add_argument('-A', metavar='alias', nargs='+',
                        dest='alias_queries', 
                        help="expand the given alias(es)")
    
    parser.add_argument('-a', metavar='file', nargs='+',
                        dest='attach_list',
                        help="attach file(s) to the message (end list with \'--\')")
    
    return parser


def lookup_alias(k):
    if k in alias_dict:
        return alias_dict[k]
    else:
        return k


def main():
    args = get_arg_parser().parse_args()
    alias_result = [lookup_alias(k) for k in args.alias_queries or []]
    for i in alias_result:
        print i
      

if __name__ == '__main__':
    main()

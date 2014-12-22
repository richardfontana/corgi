
import argparse
import email

from collections import namedtuple
from email import message

import idna


corgi_cfg = "config.yml"

alias_dict = {}


def get_arg_parser():

    parser = argparse.ArgumentParser(prog = 'corgi')

    parser.add_argument('-A', metavar='alias', nargs='+',
                        dest='alias_queries', 
                        help="expand the given alias(es)")
    
    parser.add_argument('-a', metavar='file', nargs='+',
                        dest='attach_list',
                        help="attach file(s) to the message (end list with \'--\')")
    
    return parser


def lookup_alias(k):
    if k in alias_dict:
        return idna.encode(alias_dict[k])
    else:
        return k


def main():
    args = get_arg_parser().parse_args()
    aq = args.alias_queries
    if aq:
        alias_result = [lookup_alias(k) for k in aq]
        for r in alias_result:
            print r
        return
    else:
        msg = message.Message()
        for a in args.attach_list:
            msg.attach(a)
    
      
if __name__ == '__main__':
    main()

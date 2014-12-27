

import argparse
import email
import mimetypes
import os

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


def norm_attach_path(a):
    if not os.path.isabs(a):
        a = os.path.abspath(a)
    return a


def main():
    args = get_arg_parser().parse_args()
    aq = args.alias_queries
    if aq:
        alias_result = [lookup_alias(k) for k in aq]
        for r in alias_result:
            print r
        return
    n_attach_list = [norm_attach_path(a) for a in args.attach_list]
    for path in n_attach_list:
        ctype, encoding = mimetypes.guess_type(path)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        fp = open(path)
        if maintype == 'text':
            fp = open(path)
            msg = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'image':
            fp = open(path, 'rb')
            msg = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == 'audio':
            fp = open(path, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(path, 'rb')
            msg = MIMEBase(maintype, subtype)
            msg.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(msg)
        # set filename parameter
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        outer.attach(msg)

if __name__ == '__main__':
    main()

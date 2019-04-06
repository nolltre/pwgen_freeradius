#!/usr/bin/python
import hashlib as h
import base64, sys, argparse

def generate_password(password, salt, func):
    p = bytearray(password, 'utf-8')
    s = bytearray(salt, 'utf-8')
    return base64.b64encode(func(p + s).digest() + s).decode('utf-8')

def main(argv):
    hashfunc = {
            'sha1': h.sha1,
            'sha224': h.sha224,
            'sha256': h.sha256,
            'sha384': h.sha384,
            'sha512': h.sha512
            }
    parser = argparse.ArgumentParser(description='Generates hashes for use in FreeRADIUS configuration files (default: SHA1)')
    parser.add_argument('password', metavar='password')
    parser.add_argument('salt', metavar='salt')
    parser.add_argument('--hash', default='sha1', help='one of: ' + ', '.join(list(hashfunc.keys())))

    c = parser.parse_args(argv[1:])

    print(generate_password(c.password, c.salt, hashfunc[c.hash]))

if __name__ == '__main__':
    main(sys.argv)

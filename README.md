# Password generator for FreeRADIUS
I couldn't find any utility to generate encrypted password to put into my [FreeRADIUS](http://freeradius.org/) installation and I didn't want to use `Cleartext-Password` even though it's just for my own home lab.

So, I wrote a small utility to generate encrypted hashes for use in the `authorize` configuration file.

```
usage: pwgen_freeradius.py [-h] [--hash HASH] password salt

Generates hashes for use in FreeRADIUS configuration files (default: SHA1)

positional arguments:
  password
  salt

optional arguments:
  -h, --help   show this help message and exit
  --hash HASH  one of: sha1, sha224, sha256, sha384, sha512
```

Lookup `man 5 rlm_pap` to see how to write the configuration attributes (i.e. `SSHA1-Password:`)

# Contribute
I am happy with the SHA hashes, but feel free to implement more and send me a pull request if you feel so inclined.

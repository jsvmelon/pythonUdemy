# with open("binary", mode='bw') as bin_write_file:
#     bin_write_file.write(bytes(range(17)))
#
# with open("binary", mode='br') as bin_read_file:
#     for b in bin_read_file:
#         print(b)

a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
d = 2998302  # 00 2D C0 1E

with open("binary2", mode="bw") as bin_write_file:
    bin_write_file.write(a.to_bytes(2, 'big'))
    bin_write_file.write(b.to_bytes(2, 'big'))
    bin_write_file.write(c.to_bytes(4, 'big'))
    bin_write_file.write(d.to_bytes(4, 'big'))
    bin_write_file.write(d.to_bytes(4, 'little'))

with open("binary2", mode="br") as bin_read_file:
    e = int.from_bytes(bin_read_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_read_file.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_read_file.read(4), 'big')
    print(g)
    h = int.from_bytes(bin_read_file.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_read_file.read(4), 'big')
    print(i)


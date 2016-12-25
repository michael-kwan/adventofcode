b = str(bin(3012210))
a = b[2]
b = b[3:]+a
print(int(b,2))
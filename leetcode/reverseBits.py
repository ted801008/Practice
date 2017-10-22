def reverseBits(x):
	result = int(bin(x)[2:].zfill(32)[::-1],2)
	return result

print(reverseBits(43261596))

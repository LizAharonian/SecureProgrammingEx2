from cloud import *


def bytes_xor(s1, s2):
	return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


def breakcloud(cloud):
	"""
	receives 'cloud', an object of type Cloud.
	creates a file with the name 'plain.txt' that stores the current text that is encrypted in the cloud.
	you can use only the Read/Write interfaces of Cloud (do not use its internal variables.)
	"""
	old_ct = ''
	aes_output = ''
	i = 0
	curr_byte = cloud.Write(i, b'\x00')
	while curr_byte != None:
		old_ct += curr_byte
		aes_output += cloud.Read(i)
		i += 1
		curr_byte = cloud.Write(i, b'\x00')

	xor = bytes_xor(old_ct, aes_output)

	with open("plain.txt", mode='wb+') as file:
		file.write(xor)
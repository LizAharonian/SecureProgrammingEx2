
# Consts
PLAINTEXT_FILE_NAME = "plain.txt"
ZERO_AS_BYTE = b'\x00'
EMPTY_STRING = ""


def breakcloud(cloud):
	"""
	receives 'cloud', an object of type Cloud.
	creates a file with the name 'plain.txt' that stores the current text that is encrypted in the cloud.
	you can use only the Read/Write interfaces of Cloud (do not use its internal variables.)
	"""
	original_aes_output_before_xor = EMPTY_STRING
	original_cipherText = EMPTY_STRING
	i = 0
	curr_byte = cloud.Write(i, ZERO_AS_BYTE)
	while curr_byte != None:
		original_cipherText += curr_byte
		original_aes_output_before_xor += cloud.Read(i)
		i += 1
		curr_byte = cloud.Write(i, ZERO_AS_BYTE)

	# Save the original plainText into the requested file
	with open(PLAINTEXT_FILE_NAME, mode="wb+") as file:
		# Operate the xor in order to reveal the original plainText
		file.write(xor(original_cipherText, original_aes_output_before_xor))


def xor(x, y):
	"""
	xor function.
	:param x: first element in the xor.
	:param y: second element in the xor.
	:return: x ^ y
	"""
	return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(x, y))
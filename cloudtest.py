

# Last modified: 2 May 2019



from cloud import *
from breakcloud import *

def testcloud():
	# testing your cloud functionality
	key = b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c'
	nonce = b'\x00\x00\x00\x00\x00\x00\x00\x00'
	cloud = Cloud('what.txt', key, nonce)
	r1 = cloud.Read(10)
	r2 = cloud.Read(20)
	v = '\x10'
	pos = 5
	r3 = cloud.Write(pos, v)
	r4 = cloud.Read(5)
	if r1 == '\xa1' and r2 == '\x32' and r3 == '\x29' and r4 == '\x50':
		print "success!"
	else:
		print "failed..."

def testbreaker():
	testfile = 'what.txt'
	cloud = Cloud(testfile)
	breakcloud(cloud)

	with open(testfile, mode='rb') as file:
		originalcontent = file.read()
		file.close()
		with open('plain.txt', mode='rb') as breakerresult:
			breakercontent = breakerresult.read()
			breakerresult.close()

			if originalcontent == breakercontent:
				print "success!"
				exit()
	print "failed..."


def main():
	testcloud()
	testbreaker()


if __name__ == '__main__':
	main()




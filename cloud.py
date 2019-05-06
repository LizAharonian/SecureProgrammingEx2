

# Last modified: 2 May 2019

# you don't have to use the packages below, it is only a suggestion. 
# do not use any other python module unless it is explicitly permitted by the instructor.
from Crypto.Util import Counter
import Crypto.Cipher.AES as AES
from Crypto.Random import get_random_bytes


class Cloud:
    """
    the cloud stores your content encrypted.
    you can add variables and methods to this class as you want.
    """
    def __init__(self, filename, key=get_random_bytes(32), nonce=get_random_bytes(8)):
        """
        Encrypt the content of 'filename' and store its ciphertext at self.ciphertext
        The encryption to use here is AES-CTR with 32 byte key.
        The counter should begin with zero.
        """
        # Initialize members
        self.key = key
        self.nonce = nonce

        with open(filename, mode='rb') as file:
            self.encryptGivenText(file.read())

    def encryptGivenText(self, text):
        self.pt = text
        countf = Counter.new(64, self.nonce)
        crypto = AES.new(self.key, AES.MODE_CTR, counter=countf)
        self.ciphertext = crypto.encrypt(text)

    def Read(self, position=0):
        """
        Returns one byte at 'position' from current self.ciphertext.
        position=0 returns the first byte of the ciphertext.
        """
        return self.ciphertext[position]
    def Write(self, position=0, newbyte='\x33'):
        """
        Replace the byte in 'position' from self.ciphertext with the encryption of 'newbyte'.
        Remember that you should encrypt 'newbyte' under the appropriate key (it depends on the position).
        Return the previous byte from self.ciphertext (before the re-write).
        """
        if position >= len(self.ciphertext):
            return None
        prev_byte = self.ciphertext[position]
        new_plainText = self.pt
        new_plainText[position] = newbyte
        self.encryptGivenText(new_plainText)
        return prev_byte



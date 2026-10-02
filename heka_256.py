''' Heka256r'''
''' by KryptoMagick (Karl Zander) '''
from random import shuffle

class HEKA256:
    def __init__(self):
        self.deck = list(range(512))
        
    def gen_rand_decks(self):
    	shuffle(self.deck)
    	
    def ksa(self):
         self.deck.append(self.deck.pop(0))
         self.deck.append(self.deck.pop(0))
         
         self.deck.insert(self.deck[1], self.deck.pop(0))
         
         return self.deck[self.deck[self.deck[0]]] % 256
         
    def encrypt_letter(self, letter):
        num = ord(letter)
        key = self.ksa()
        num = (num ^ key)
        return chr(num)
        
    def decrypt_letter(self, letter):
        num = ord(letter)
        key = self.ksa()
        num = (num ^ key)
        return chr(num)

    def encrypt(self, letters):
        ctxt = []
        for x in range(len(letters)):
            letter = self.encrypt_letter(letters[x])
            ctxt.append(letter)
        return "".join(ctxt)

    def decrypt(self, letters):
        ptxt = []
        for x in range(len(letters)):
            letter = self.decrypt_letter(letters[x])
            ptxt.append(letter)
        return "".join(ptxt)
        
heka = HEKA256()
heka.gen_rand_decks()
m = [chr(65)] * 100000
msg = "".join(m)
ctxt = heka.encrypt(msg)
print(ctxt)

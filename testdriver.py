import ciphers.myOwnStreamCipher as mosc
import ciphers.tools as tools
import ciphers.extendedVigenere as ev
import ciphers.playfair as pf

plaintext = "Where no counsel is, the people fall... but in the multitude of counsellors there is safety."
key = "Proverbs 11:14"

cipherstream = mosc.mosc_encrypt(plaintext, key)
print(cipherstream, "\n\n")
plainstream = mosc.mosc_decrypt(cipherstream, key)
print(plaintext)

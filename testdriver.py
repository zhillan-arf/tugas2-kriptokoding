import ciphers.myOwnStreamCipher as mosc
import ciphers.tools as tools
import ciphers.extendedVigenere as ev
import ciphers.playfair as pf

plaintext = "Where no counsel is, the people fall... (Proverbs 11:14)"
key = "11073"

plain1 = "V2hlcmUgbm8gY291bnNlbCBpcywgdGhlIHBlb3BsZSBmYWxsLi4uIChQcm92ZXJicyAxMToxNCk="


cipherstream = mosc.mosc_encrypt(plaintext, key)
print(cipherstream, "\n\n")
plainstream = mosc.mosc_decrypt(cipherstream, key)
print(plaintext)

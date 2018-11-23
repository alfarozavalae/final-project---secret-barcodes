######################################################################
# Author: Ela Jamali & Emely Alfaro Zavala
# Username: Jamalie & Alfarozavalae
#
# Assignment: Final Project
#
# Purpose: Our program will receive a ciphered message with different characters and will extract the the 12-digit
# codes found and check for a barcode, afterwards, using the urllib our program will access the web showing the item
# online.
####################################################################################
# Acknowledgements:

####################################################################################

import urllib

class CeasarCipher:
    """
    The CaesarCipher class represents and manipulates key, input file and the crypt type
    This class will import a file that needs to be encrypted or decrypted, with an integer representing the key
    it will decrypt or decrypt the given file
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"            # The alphabet, which will be used to do our shifts

    def __init__(self, input_file = "ciphertext.txt", key = 7, crypt_type = "decrypt"):
        """
        A constructor for the CaesarCipher class

        :param input_file: The file to be decrypted
        :param key: The amount each message/cipher needs shifted
        :param crypt_type: Either encrypt or decrypt
        """
        self.input_file = input_file                            # The file to be encrypted or decrypted
        self.key = key                                          # The amount each message/cipher will be shifted
        self.message = ""                                       # A placeholder for the message
        self.cipher = ""                                        # A placeholder for the cipher
        self.crypt_type = crypt_type                            # Either "encrypt" or "decrypt"
        self.import_file()                                      # Calls the import_file() method below

    def import_file(self):
        """
        Imports a file stored in the variable self.input_file

        :return: a string representing the contents of the file
        """
        f = open(self.input_file, "r")
        if self.crypt_type == "decrypt":
            self.cipher = f.read()                   # Set self.cipher to the file contents
        f.close()
        if __name__ == "__main__":
            print("File imported: {0}".format(self.input_file))

    def export_file(self, text_to_export, filename):
        """
        Exports a file called filename

        :param text_to_export: the string to be written to the exported file
        :param filename: a string representing the name of the file to be exported to
        """
        f = open(filename, "w")
        f.write(text_to_export)
        f.close()
        if __name__ == "__main__":
            print("File exported: {0}".format(filename))

    def decrypt(self):
        """
        Converts a ciphertext.txt into an original message by shifting each letter to the left by the key

        :return: a string representing the original message
        """
        # TODO Complete the decrypt method
        output = ""
        for i in self.cipher:
            if i.upper() in self.alphabet:
                new_letter = self.alphabet.find(i.upper())
                # we use the module to return the correct module after the inverse
                # when the index is negative it will go back to the end of the alphabet
                output += self.alphabet[new_letter - self.key % 36]
            else:
                output += i     # Adds non-alphabet characters directly
        if __name__ == "__main__":
            print("Your message has been decrypted")
        return output


    def online_search(self):
        """

        :return:
        """
    pass


def main():

    text1 = CeasarCipher("ciphertext.txt", 7, "decrypt")
    exporting = text1.decrypt()
    text1.export_file(exporting, "exporting_test")


main()

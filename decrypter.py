import os
import pyaes

# Open the encrypted archive
file_name = 'test.txt.ransomware'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# decrypt the data
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

# Remove the file
os.remove(file_name)

# Create new file
new_file = 'test.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted_data)
new_file.close()

import os
from Decryption import Decryption
BASE_URL = "Encrypted"
END_URL = "Decrypted"
DecrKernel = Decryption("key.jpg")
DecrKernel.set_config(BASE_URL,END_URL,"jpg")
i = 1
for file_name in os.listdir(BASE_URL):
    print i, file_name
    if file_name[0] == ".":
        continue
    DecrKernel.generate_decrypted_image(file_name, str(i))
    i += 1

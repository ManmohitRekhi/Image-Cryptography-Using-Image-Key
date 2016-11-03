import os
from Encryption import Encryption
BASE_URL = "Orignal"
END_URL = "Encrypted"
EncrKernel = Encryption("key.jpg")
EncrKernel.set_config(BASE_URL, END_URL, "tiff")
i = 1
for file_name in os.listdir(BASE_URL):
    print i
    EncrKernel.generate_encrypted_image(file_name)
    i += 1

def encrypt_decrypt_image(path, key, mode):
    try:
        # print path of image file and key
        print('The path of file : ', path)
        print(f'Key for {mode} : ', key)

        # open file for reading purpose
        with open(path, 'rb') as fin:
            # storing image data in variable "image"
            image = fin.read()

        # converting image into byte array to perform operation easily on numeric data
        image = bytearray(image)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key

        # opening file for writing purpose
        with open(path, 'wb') as fin:
            # writing data in image
            fin.write(image)

        print(f'{mode.capitalize()}ion Done...')

    except Exception as e:
        print('Error caught : ', e.__class__.__name__)

def main():
    # take path of image as input
    path = input(r'Enter path of Image : ')
    
    # taking key as input
    key = int(input('Enter Key for encryption/decryption of Image : '))
    
    # take mode as input
    mode = input('Enter mode (encrypt/decrypt) : ').strip().lower()
    
    if mode == 'encrypt' or mode == 'decrypt':
        encrypt_decrypt_image(path, key, mode)
    else:
        print('Invalid mode. Please enter "encrypt" or "decrypt".')

if __name__ == "__main__":
    main()

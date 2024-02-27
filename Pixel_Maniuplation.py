from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array for pixel manipulation
    img_array = np.array(img)
    
    # Apply XOR operation with the key to each pixel value
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the image to a NumPy array for pixel manipulation
    encrypted_array = np.array(encrypted_img)
    
    # Apply XOR operation with the key to each pixel value to decrypt
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'.")

if __name__ == "__main__":
    # User input for image file path
    image_path = input("Enter the path of the image file: ")
    
    # User input for encryption key
    encryption_key = int(input("Enter the encryption key (an integer): "))
    
    # Encrypt the image
    encrypt_image(image_path, encryption_key)
    
    # Provide the path to the encrypted image for decryption
    encrypted_image_path = "encrypted_image.png"
    
    # Decrypt the image
    decrypt_image(encrypted_image_path, encryption_key)

# Prodigy_CS_02
 Pixel Manipulation for Image Encryption
 
# Image Encryption Algorithm Readme

## Overview

This Python script provides a simple yet effective image encryption and decryption algorithm using pixel manipulation. The algorithm utilizes the Python Imaging Library (PIL) and NumPy for efficient handling of image data.

## Encryption Process

1. **Image Loading:**
   - The algorithm begins by loading the original image using the PIL library.

2. **NumPy Array Conversion:**
   - The loaded image is then converted into a NumPy array. This conversion facilitates pixel-level manipulation, enabling efficient processing.

3. **XOR Operation with Key:**
   - Each pixel value in the NumPy array undergoes an XOR operation with the provided encryption key. XORing introduces a bitwise manipulation that transforms the pixel values.

4. **Encrypted Array to Image:**
   - The resulting encrypted NumPy array is converted back into an image using PIL. This new image represents the encrypted version of the original image.

5. **Save Encrypted Image:**
   - The encrypted image is then saved as 'encrypted_image.png' in the same directory as the script.

## Decryption Process

1. **Encrypted Image Loading:**
   - The script starts by loading the encrypted image ('encrypted_image.png').

2. **NumPy Array Conversion:**
   - Similar to the encryption process, the loaded encrypted image is converted into a NumPy array.

3. **XOR Operation with Key for Decryption:**
   - Each pixel value in the encrypted NumPy array undergoes an XOR operation with the same encryption key. This reverses the encryption, decrypting the pixel values.

4. **Decrypted Array to Image:**
   - The decrypted NumPy array is converted back into an image using PIL, representing the original image.

5. **Save Decrypted Image:**
   - The decrypted image is saved as 'decrypted_image.png' in the same directory as the script.

## Usage

- The script can be run standalone, prompting the user to enter the path of the image file and an encryption key.
- The encrypted image is saved as 'encrypted_image.png' in the script's directory.
- The script then automatically decrypts the image using the provided key and saves it as 'decrypted_image.png'.

## Instructions for Use

1. **Run the Script:**
   - Execute the script in a Python environment.

2. **User Inputs:**
   - Enter the path of the image file when prompted.
   - Provide an encryption key (an integer) for the XOR operation.

3. **Encryption and Decryption:**
   - The script will encrypt the image, save the encrypted version, and then decrypt it, saving the decrypted version.

4. **Check Output:**
   - 'encrypted_image.png' and 'decrypted_image.png' will be generated in the script's directory.

## Example Usage

```bash
python image_encryption.py


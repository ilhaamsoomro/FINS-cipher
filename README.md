
### FINS-cipher

---

### Introduction:
This Django project provides a secure and user-friendly web interface for encrypting and decrypting text messages. Unlike traditional encryption methods, this project employs a custom passphrase-based encryption algorithm, adding an extra layer of security. The algorithm utilizes a substitution cipher with dynamically generated shifts based on the passphrase provided by the user.

### Features:
- Encryption and Decryption of text input.
- Custom passphrase for encryption, enhancing security.
- Dynamic shifting of characters based on the passphrase, making it resistant to frequency analysis attacks.
- User-friendly web interface for easy interaction.

### Setup Instructions:
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   ```
   
2. **Install Dependencies:**
   Navigate to the project directory and install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server:**
   Execute the following command to start the Django development server:
   ```bash
   python manage.py runserver
   ```
   The server will be accessible at `http://localhost:8000/`.

### Usage:
1. **Access the Web Interface:**
   Open your web browser and navigate to `http://localhost:8000/` to access the home page.

2. **Encryption:**
   - Enter the plaintext message to be encrypted in the input field.
   - Provide a passphrase for encryption. Choose a passphrase that is not easily guessable and hard to crack.
   - Click on the "Encrypt" button.
   - The encrypted text, also known as ciphertext, will be displayed on the result page.

3. **Decryption:**
   - Enter the ciphertext message to be decrypted in the input field.
   - Provide the same passphrase used for encryption.
   - Click on the "Decrypt" button.
   - The decrypted text, originally entered as plaintext, will be displayed on the result page.

### Encryption Algorithm:
- **Substitution Cipher:**
  - In this algorithm, each letter in the plaintext is substituted with another letter. The substitution is determined by a secret key or, in this case, a passphrase.
  - The key idea is to shift characters by a certain amount determined by the passphrase. This shift makes it difficult for attackers to decipher the text without the correct passphrase.
  - Non-alphabetic characters remain unchanged during encryption.

- **Dynamic Shifts:**
  - The strength of the encryption lies in the dynamic nature of the shifts. Instead of using a fixed shift value for all characters, a unique shift is generated for each character based on the passphrase.
  - This dynamic shifting adds complexity to the encryption process, making it more resistant to various cryptanalysis techniques.

### Implementation Details:
- **Django Views:**
  - `home`: Renders the home page template for user input.
  - `result`: Renders the result page template displaying the encrypted or decrypted text.
  - `process_fins`: Handles form submission for encryption and decryption.

### Contributing:
- Contributions to the project are welcome. You can contribute by submitting bug reports, feature requests, or pull requests.


### Author:
- **Ilhaam Ismail Soomro** - [GitHub Profile](https://github.com/ilhaamsoomro)


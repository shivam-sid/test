# CryptoSuite

CryptoSuite is a Python-based cryptography and encoding toolkit that provides a clean, simple, and modular way of working with different cryptographic operations. It is designed to serve as both a practical tool for real usage and as a learning resource for people exploring how encryption, encoding, and decoding mechanisms work. The project is still under development but already offers multiple features that make it useful for developers, students, and enthusiasts who want to quickly test or apply different cryptographic functions.

---

## Features

CryptoSuite comes with a variety of features that make it stand out from simple one-off scripts or basic encoders/decoders. The philosophy of the tool is to provide a system that can chain operations together into what are called **recipes**. These recipes are collections of steps that you can run sequentially, save for later use, or reload when you want to repeat the same process. This makes it powerful for tasks where you need more than one operation to reach the result.

### Recipe System
- You can create a sequence of operations (for example: convert text to Base64 → encode to HEX → apply a cipher).
- Each step is executed in order, and the output of one step becomes the input of the next.
- Recipes can be **saved** for future use, so you don’t need to manually rebuild them each time.
- Recipes can be **loaded** at any point, making the tool practical for repeated workflows.

### Base64 Encoding and Decoding
- Supports full Base64 encoding of any given text input.
- Supports decoding Base64 back into the original text or data.
- Extremely useful when dealing with data serialization, binary-to-text conversions, or when working with web-related encodings.

### HEX Encoding and Decoding
- Convert plain text into HEX representation with one click.
- Decode HEX strings back into their original representation.
- Helpful in debugging, working with binary protocols, or when analyzing encoded payloads.

### Cipher Operations
- The application includes basic cipher functionality.
- Provides a base for more advanced cipher integrations like AES, which are planned for future updates.
- Makes it possible to practice with classical cipher transformations and understand cryptography at a fundamental level.

### Graphical User Interface (GUI)
- CryptoSuite is not just a command-line utility; it comes with a **dark-themed GUI** that makes it easy to use.
- The GUI is split into **Encrypt/Encode** and **Decrypt/Decode** panels, each with its own input and output boxes.
- Dropdown menus allow you to select operations step by step and see results instantly.
- The result is automatically displayed in the output box, so you can copy it or use it for the next step.
- The GUI design allows you to add multiple operations to a recipe in one session.

### Save and Load Recipes
- A very important feature is the ability to save custom-built recipes into files.
- Once saved, a recipe can be reloaded at any point in the future to run the same operations again.
- This makes it particularly useful for penetration testers, security researchers, and students who repeatedly need to apply the same transformations on data.

### Extensibility
- The project is built in a modular way, meaning new operations (encoders, decoders, ciphers, hashes) can be easily added.
- Developers can contribute by creating their own modules and adding them to the existing system.

### Planned Advanced Features
Although the current version already supports Base64, HEX, and basic ciphers, several advanced features are being developed:
- **AES Encryption & Decryption** – Strong symmetric encryption for practical usage.
- **Auto-Detect Mode** – A smart mode that attempts to guess the type of encoding or encryption used on the input and suggests possible operations to decode it.
- **Hashing Support** – Integration of hashing algorithms like MD5, SHA-1, and SHA-256 for quick calculations.
- **Drag-and-Drop Recipe Editing** – A planned GUI improvement to allow rearranging the steps in recipes more easily.
- **Classic Ciphers** – Inclusion of historical cipher algorithms like Caesar, Vigenère, and substitution ciphers for educational usage.

---

## How It Works

When you run CryptoSuite, the application launches a graphical window where you can start building your workflow:

1. **Input Text** – Enter the plain text or encoded data that you want to work on.
2. **Select Operation** – Choose an operation such as “To Base64”, “From HEX”, or “Cipher Encode”.
3. **Chain Operations** – Add multiple steps to process the data further. Each step automatically takes the output of the previous one.
4. **Output** – The final result of your sequence is displayed in the output box.
5. **Save Recipe** – If you want to keep this exact sequence, you can save it as a recipe file.
6. **Load Recipe** – At any time in the future, load the recipe and apply the same operations without rebuilding it manually.

---

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/shivam-sid/cryptosuite.git
   cd cryptosuite
   ```

2. (Optional) Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

---

## Why Use CryptoSuite?

- **User Friendly**: The GUI is intuitive and eliminates the need to memorize commands.
- **Educational**: Perfect for students learning about cryptography and encoding methods.
- **Reusable**: The recipe feature allows automation of workflows.
- **Extensible**: Developers can add their own operations with minimal effort.
- **Practical**: Provides a quick way to encode, decode, or cipher text without needing multiple different tools.

---

## Future Vision

The long-term vision of CryptoSuite is to become a one-stop lightweight cryptography toolkit for both educational and practical usage. By combining multiple cryptographic operations into a single GUI-based system, it bridges the gap between learning tools and professional utilities. Planned additions like AES, hashing, and auto-detect will make it even more useful in everyday security-related workflows. Contributions from the community will also help expand the scope of supported operations, ensuring that CryptoSuite grows into a complete cryptographic suite.

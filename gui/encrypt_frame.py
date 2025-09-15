# File: gui/encrypt_frame.py

import customtkinter
import json
from tkinter import filedialog
from gui.base_frame import BaseFrame
from operations.encoders import to_base64
from operations.ciphers import caesar_cipher, atbash_cipher, rot13_cipher, vigenere_cipher, aes_encrypt, des_encrypt, triple_des_encrypt, blowfish_encrypt
from operations.hex import to_hex
from operations.text_converters import to_binary, to_morse
from operations.asymmetric_ciphers import rsa_encrypt
from operations.hashing_core import hash_md5, hash_sha1, hash_sha256, hash_sha512


class EncryptFrame(BaseFrame):
    def __init__(self, master, app, status_bar, **kwargs):
        # --- Set unique properties for this frame ---
        self.recipe_title = "Encryption Recipe"
        self.placeholder_text = "Click an operation to begin..."
        self.load_button_text = "📂 Load"
        self.load_button_width = 70

        super().__init__(master, app, status_bar, **kwargs)

    def execute_operation(self, operation_name, input_data, step_frame):
        if operation_name == "To Base64":
            return to_base64(input_data)
        elif operation_name == "To Hex":
            return to_hex(input_data)
        elif operation_name == "To Binary":
            return to_binary(input_data)
        elif operation_name == "Morse Code":
            return to_morse(input_data)
        elif operation_name == "Caesar Encrypt":
            try:
                shift = int(step_frame.param_entry.get())
                if not 1 <= shift <= 25:
                    return False, "Shift must be between 1 and 25."
                return caesar_cipher(input_data, shift, decrypt=False)
            except (ValueError, TypeError):
                return False, "Invalid shift value. Must be an integer."
            except AttributeError:
                return False, "Could not find shift parameter."
        elif operation_name == "Atbash Cipher":
            return atbash_cipher(input_data)
        elif operation_name == "ROT13 Cipher":
            return rot13_cipher(input_data)
        elif operation_name == "Vigenère Cipher":
            try:
                key = step_frame.param_entry.get()
                if not key:
                    return False, "Vigenère key cannot be empty."
                return vigenere_cipher(input_data, key, decrypt=False)
            except AttributeError:
                return False, "Could not find key parameter."
        elif operation_name == "AES Encrypt":
            try:
                key = step_frame.param_entry.get()
                return aes_encrypt(input_data, key)
            except AttributeError:
                return False, "Could not find key parameter."
        elif operation_name == "DES Encrypt":
            try:
                key = step_frame.param_entry.get()
                return des_encrypt(input_data, key)
            except AttributeError:
                return False, "Could not find key parameter."
        elif operation_name == "Triple DES Encrypt":
            try:
                key = step_frame.param_entry.get()
                return triple_des_encrypt(input_data, key)
            except AttributeError:
                return False, "Could not find key parameter."
        elif operation_name == "Blowfish Encrypt":
            try:
                key = step_frame.param_entry.get()
                return blowfish_encrypt(input_data, key)
            except AttributeError:
                return False, "Could not find key parameter."
        elif operation_name == "RSA Encrypt":
            try:
                public_key = step_frame.param_entry.get("1.0", "end-1c")
                if not public_key:
                    return False, "RSA public key cannot be empty."
                return rsa_encrypt(input_data, public_key)
            except AttributeError:
                return False, "Could not find key parameter."
        elif operation_name == "MD5":
            return hash_md5(input_data)
        elif operation_name == "SHA-1":
            return hash_sha1(input_data)
        elif operation_name == "SHA-256":
            return hash_sha256(input_data)
        elif operation_name == "SHA-512":
            return hash_sha512(input_data)
        else:
            return False, f"Unknown operation: {operation_name}"

    def create_operations_sidebar(self):
        sidebar_frame = customtkinter.CTkFrame(self)
        sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)
        sidebar_frame.grid_rowconfigure(1, weight=1)
        sidebar_frame.grid_columnconfigure(0, weight=1)

        customtkinter.CTkLabel(sidebar_frame, text="Operations",
                               font=customtkinter.CTkFont(size=18, weight="bold")).grid(row=0, column=0, padx=20,
                                                                                        pady=(10, 10))

        scrollable_frame = customtkinter.CTkScrollableFrame(sidebar_frame, fg_color="transparent", corner_radius=0)
        scrollable_frame.grid(row=1, column=0, sticky="nsew", pady=(10, 0))
        scrollable_frame.grid_columnconfigure(0, weight=1)

        # --- Utility Function for Separators ---
        def add_separator(row):
            separator = customtkinter.CTkFrame(scrollable_frame, height=1, fg_color="gray25")
            separator.grid(row=row, column=0, sticky="ew", padx=10, pady=10)
            return row + 1

        current_row = 0

        # --- Section: Encoders ---
        customtkinter.CTkLabel(scrollable_frame, text="Encoders", font=customtkinter.CTkFont(weight="bold")).grid(
            row=current_row, column=0, pady=(5, 2), padx=10, sticky="w")
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="To Base64", anchor="w",
                                command=lambda: self.add_recipe_step("To Base64")).grid(row=current_row, column=0,
                                                                                        sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="To Hex", anchor="w",
                                command=lambda: self.add_recipe_step("To Hex")).grid(row=current_row, column=0,
                                                                                     sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="To Binary", anchor="w",
                                command=lambda: self.add_recipe_step("To Binary")).grid(row=current_row, column=0,
                                                                                        sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="Morse Code", anchor="w",
                                command=lambda: self.add_recipe_step("Morse Code")).grid(row=current_row, column=0,
                                                                                         sticky="ew", padx=10, pady=2)
        current_row += 1
        current_row = add_separator(current_row)

        # --- Section: Classic Ciphers ---
        customtkinter.CTkLabel(scrollable_frame, text="Classic Ciphers",
                               font=customtkinter.CTkFont(weight="bold")).grid(row=current_row, column=0, pady=(5, 2),
                                                                               padx=10, sticky="w")
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="Caesar Encrypt", anchor="w",
                                command=lambda: self.add_recipe_step("Caesar Encrypt")).grid(row=current_row,
                                                                                             column=0,
                                                                                             sticky="ew", padx=10,
                                                                                             pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="Atbash Cipher", anchor="w",
                                command=lambda: self.add_recipe_step("Atbash Cipher")).grid(row=current_row,
                                                                                            column=0,
                                                                                            sticky="ew", padx=10,
                                                                                            pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="ROT13 Cipher", anchor="w",
                                command=lambda: self.add_recipe_step("ROT13 Cipher")).grid(row=current_row, column=0,
                                                                                           sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="Vigenère Cipher", anchor="w",
                                command=lambda: self.add_recipe_step("Vigenère Cipher")).grid(row=current_row, column=0,
                                                                                              sticky="ew", padx=10,
                                                                                              pady=2)
        current_row += 1
        current_row = add_separator(current_row)

        # --- Section: Symmetric Ciphers ---
        customtkinter.CTkLabel(scrollable_frame, text="Symmetric Ciphers",
                               font=customtkinter.CTkFont(weight="bold")).grid(row=current_row, column=0, pady=(5, 2),
                                                                               padx=10, sticky="w")
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="AES Encrypt", anchor="w",
                                command=lambda: self.add_recipe_step("AES Encrypt")).grid(row=current_row, column=0,
                                                                                          sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="DES Encrypt", anchor="w",
                                command=lambda: self.add_recipe_step("DES Encrypt")).grid(row=current_row, column=0,
                                                                                          sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="Triple DES Encrypt", anchor="w",
                                command=lambda: self.add_recipe_step("Triple DES Encrypt")).grid(row=current_row,
                                                                                                 column=0, sticky="ew",
                                                                                                 padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="Blowfish Encrypt", anchor="w",
                                command=lambda: self.add_recipe_step("Blowfish Encrypt")).grid(row=current_row,
                                                                                               column=0, sticky="ew",
                                                                                               padx=10, pady=2)
        current_row += 1
        current_row = add_separator(current_row)

        # --- Section: Asymmetric Ciphers ---
        customtkinter.CTkLabel(scrollable_frame, text="Asymmetric Ciphers",
                               font=customtkinter.CTkFont(weight="bold")).grid(row=current_row, column=0, pady=(5, 2),
                                                                               padx=10, sticky="w")
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="RSA Encrypt", anchor="w",
                                command=lambda: self.add_recipe_step("RSA Encrypt")).grid(row=current_row, column=0,
                                                                                          sticky="ew", padx=10, pady=2)
        current_row += 1
        current_row = add_separator(current_row)

        # --- Section: Hashing ---
        customtkinter.CTkLabel(scrollable_frame, text="Hashing", font=customtkinter.CTkFont(weight="bold")).grid(
            row=current_row, column=0, pady=(5, 2), padx=10, sticky="w")
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="MD5", anchor="w",
                                command=lambda: self.add_recipe_step("MD5")).grid(row=current_row, column=0,
                                                                                 sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="SHA-1", anchor="w",
                                command=lambda: self.add_recipe_step("SHA-1")).grid(row=current_row, column=0,
                                                                                    sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="SHA-256", anchor="w",
                                command=lambda: self.add_recipe_step("SHA-256")).grid(row=current_row, column=0,
                                                                                      sticky="ew", padx=10, pady=2)
        current_row += 1
        customtkinter.CTkButton(scrollable_frame, text="SHA-512", anchor="w",
                                command=lambda: self.add_recipe_step("SHA-512")).grid(row=current_row, column=0,
                                                                                      sticky="ew", padx=10, pady=2)
        current_row += 1

    def load_recipe(self):
        filepath = filedialog.askopenfilename(title="Load Recipe", filetypes=[("JSON files", "*.json")])
        if not filepath: return
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                recipe_data = json.load(f)
            self.clear_recipe()
            for step in recipe_data:
                operation_name = step.get("operation")
                args = step.get("args", {})
                if operation_name: self.add_recipe_step(operation_name, args=args)
            self.status_bar.configure(text=f"Recipe loaded!", text_color="gray70")
        except Exception as e:
            self.app.show_toast("File Error", f"Failed to load recipe: {e}", toast_type="error")
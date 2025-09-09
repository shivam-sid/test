# File: gui/settings_frame.py

import customtkinter


class SettingsFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="transparent")

        # Create a central frame for the settings content
        content_frame = customtkinter.CTkFrame(self)
        content_frame.pack(expand=True, padx=20, pady=20)

        # --- Appearance Mode Setting ---
        appearance_label = customtkinter.CTkLabel(content_frame, text="Appearance Mode",
                                                  font=customtkinter.CTkFont(size=16, weight="bold"))
        appearance_label.pack(pady=(10, 5), padx=20, anchor="w")

        self.appearance_menu = customtkinter.CTkOptionMenu(
            content_frame,
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode
        )
        self.appearance_menu.pack(fill="x", padx=20, pady=(0, 20))
        self.appearance_menu.set(customtkinter.get_appearance_mode())  # Set default value

    def change_appearance_mode(self, new_mode: str):
        """Changes the theme of the application."""
        customtkinter.set_appearance_mode(new_mode)
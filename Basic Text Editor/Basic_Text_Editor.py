import tkinter as tk
from tkinter import filedialog, font



    
class TextEditor:

    """This class opening the Basic Text Editor where you can open/save/save as file, you can use cut/copy/pase/undo/redo operations, there is dark/light mode
     you cant change the font/fontsize """
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")


        # Set the fixed size for the text editor
        self.root.geometry("1200x800")

        #Text widget setting
        self.text_widget = tk.Text(root, bg="white", fg="black", wrap=tk.WORD, undo = True, autoseparators = True)
        self.text_widget.pack(expand = 'yes', fill = 'both')

        #Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)


        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff= 0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)



        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_widget.edit_undo, accelerator="       (CTRL + Z)")
        self.edit_menu.add_command(label="Redo", command=self.text_widget.edit_redo, accelerator="       (CTRL + Y)")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut_text, accelerator="       (CTRL + X)")
        self.edit_menu.add_command(label="Copy", command=self.copy_text, accelerator="       (CTRL + C)")
        self.edit_menu.add_command(label="Paste", command=self.paste_text, accelerator="       (CTRL + V)")

         # Format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        # Font menu
        self.font_menu = tk.Menu(self.format_menu, tearoff=0)
        self.format_menu.add_cascade(label="Font", menu=self.font_menu)

        # Font family submenu
        self.font_family = font.families()
        self.selected_font = tk.StringVar(value=self.font_family[0])
        for font_name in self.font_family:
            self.font_menu.add_radiobutton(label=font_name, variable=self.selected_font, value=font_name, command=self.apply_font)

        # Font size submenu
        self.font_size_menu = tk.Menu(self.format_menu, tearoff=0)
        self.format_menu.add_cascade(label="Font Size", menu=self.font_size_menu)
        self.font_size_var = tk.IntVar(value=12)
        font_sizes = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
        for size in font_sizes:
            self.font_size_menu.add_radiobutton(label=str(size), variable=self.font_size_var, value=size, command=self.apply_font)

        # Initial font configuration
        self.current_font = font.Font(family=self.selected_font.get(), size=self.font_size_var.get())
        self.text_widget.config(font=self.current_font)




        # Color mode menu
        self.color_mode_menu = tk.Menu(self.format_menu, tearoff=0)
        self.format_menu.add_cascade(label="Color Mode", menu=self.color_mode_menu)
        self.color_mode_var = tk.StringVar(value="Light")
        self.color_mode_menu.add_radiobutton(label="Light", variable=self.color_mode_var, value="Light", command=self.toggle_color_mode)
        self.color_mode_menu.add_radiobutton(label="Dark", variable=self.color_mode_var, value="Dark", command=self.toggle_color_mode)

        # Set initial color scheme
        self.set_color_scheme("Light")


    def open_file(self):
        #Open file

        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_widget.delete("1.0", tk.END)
                    self.text_widget.insert(tk.END, content)
        except:
            print("Something went wrong when u tried to open the file")
    def save_file(self):
        #Save file

        try:
            if not hasattr(self, 'file_path') or not self.file_path:
                self.save_file_as()
            else:
                content = self.text_widget.get("1.0", tk.END)
                with open(self.file_path, "w") as file:
                    file.write(content)

        except:
            print("You cant save the file")

    def save_file_as(self):
        #Save file as
        try:

            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                self.file_path = file_path
                self.save_file()
        except:
            print("Something went wrong when you try to save the file")


    def apply_font(self):
        #Setting the Font
        self.current_font.configure(family=self.selected_font.get(), size=self.font_size_var.get())
        self.text_widget.config(font=self.current_font)

    def cut_text(self):
        #Cut operation
        try:
            self.text_widget.event_generate("<<Cut>>")
        except:
            "You cant cut"

    def copy_text(self):
        #Copy operation
        self.text_widget.event_generate("<<Copy>>")

    def paste_text(self):
        #Paste operation
        self.text_widget.event_generate("<<Paste>>")



    def toggle_color_mode(self):
        #Setting the theme
        selected_mode = self.color_mode_var.get()
        self.set_color_scheme(selected_mode)

    def set_color_scheme(self, mode):
        if mode == "Light":
            # Light mode color scheme
            self.root.configure(bg="white")
            self.text_widget.configure(bg="white", fg="black", insertbackground="black", selectbackground="#a6a6a6", selectforeground="white")
        elif mode == "Dark":
            # Dark mode color scheme
            self.root.configure(bg="#333333")
            self.text_widget.configure(bg="#333333", fg="white", insertbackground="white", selectbackground="#a6a6a6", selectforeground="white")


    
if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()
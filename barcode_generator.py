import tkinter as tk
from tkinter import filedialog, messagebox
import barcode
from barcode.writer import ImageWriter
import qrcode

class BarcodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Barcode Generator")

        self.label_type = tk.Label(master, text="Barcode Type:")
        self.label_type.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_type = tk.Entry(master)
        self.entry_type.grid(row=0, column=1, padx=10, pady=5)

        self.label_data = tk.Label(master, text="Data:")
        self.label_data.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_data = tk.Entry(master)
        self.entry_data.grid(row=1, column=1, padx=10, pady=5)

        self.label_filename = tk.Label(master, text="Save As:")
        self.label_filename.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_filename = tk.Entry(master)
        self.entry_filename.grid(row=2, column=1, padx=10, pady=5)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=2, column=2, padx=5, pady=5)

        self.generate_button = tk.Button(master, text="Generate Barcode", command=self.generate_barcode)
        self.generate_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Supported barcode types
        self.supported_barcode_types = ['ean13', 'code128', 'upca', 'qrcode']

    def browse_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            self.entry_filename.delete(0, tk.END)
            self.entry_filename.insert(0, filename)

    def generate_barcode(self):
        barcode_type = self.entry_type.get().lower()
        data = self.entry_data.get()
        filename = self.entry_filename.get()

        if not barcode_type or not data or not filename:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if barcode_type not in self.supported_barcode_types:
            messagebox.showerror("Error", "Unsupported barcode type.")
            return

        try:
            if barcode_type == 'qrcode':
                qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
                qr.add_data(data)
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color="white")
                img.save(filename)
            else:
                barcode_class = barcode.get_barcode_class(barcode_type)
                barcode_instance = barcode_class(data, writer=ImageWriter())
                barcode_instance.save(filename)
                
            messagebox.showinfo("Success", "Barcode generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = BarcodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

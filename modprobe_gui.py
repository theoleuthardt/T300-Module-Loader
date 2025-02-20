import tkinter as tk
import subprocess
from tkinter import messagebox

def load_module():
    try:
        subprocess.run(["sudo", "/usr/sbin/modprobe", "/var/lib/modules/hid-tmff-new.ko"], check=True)
        result = subprocess.run(["lsmod"], capture_output=True, text=True)
        if "hid_tmff_new" in result.stdout:
            messagebox.showinfo("Erfolg", "Modul erfolgreich geladen und überprüft!")
        else:
            messagebox.showwarning("Warnung", "Modul wurde geladen, aber nicht in lsmod gefunden!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Fehler", f"Fehler beim Laden des Moduls:\n{e}")

def unload_module():
    try:
        subprocess.run(["sudo", "/usr/sbin/rmmod", "hid_tmff_new"], check=True)
        result = subprocess.run(["lsmod"], capture_output=True, text=True)
        if "hid_tmff_new" in result.stdout:
            messagebox.showwarning("Warnung", "Modul wurde nciht entladen!")
        else:
            messagebox.showinfo("Erfolg", "Modul erfolgreich entladen und überprüft!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Fehler", f"Fehler beim Entladen des Moduls:\n{e}")

root = tk.Tk()
root.title("T300 Module Loader")
root.geometry("600x200")

tk.Button(root, text="Load Module", command=load_module, width=20).pack(pady=10)
tk.Button(root, text="Remove Module", command=unload_module, width=20).pack(pady=10)

root.mainloop()

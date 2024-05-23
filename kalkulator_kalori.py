import tkinter as tk
from tkinter import ttk
from styles import apply_styles

class KalkulatorKaloriGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kebutuhan Kalori")
        self.configure(bg='#1e1e1e')  # Set background color to dark grey
        self._berat = None
        self._tinggi = None
        self._usia = None
        self._jenis_kelamin = None
        self._tingkat_aktivitas = None
        apply_styles(self)  # Apply styles from the external file
        self.setup_gui()

    def setup_gui(self):
        # Judul
        judul = tk.Frame(self, bg='#1e1e1e', width=200, height=50)
        judul.grid(row=0, column=0, columnspan=10, sticky=tk.W, padx=20, pady=10)
        ttk.Label(judul, text="Hitung Kebutuhan Kalorimu!", font=('Arial', 20, 'bold'), foreground='#007acc', background='#1e1e1e').pack()

        # Gaya umum untuk semua label dan entry
        label_style = {'font': ('Arial', 10, 'bold'), 'foreground': '#007acc'}
        entry_style = {'font': ('Arial', 10)}

        # Gaya untuk Frame utama
        main_frame = ttk.Frame(self, padding="20", style='MainFrame.TFrame')
        main_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label dan Entry untuk Berat
        ttk.Label(main_frame, text="Berat (kg):", **label_style).grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        self.entry_berat = ttk.Entry(main_frame, **entry_style)
        self.entry_berat.grid(row=0, column=1, pady=5, padx=5)

        # Label dan Entry untuk Tinggi
        ttk.Label(main_frame, text="Tinggi (cm):", **label_style).grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
        self.entry_tinggi = ttk.Entry(main_frame, **entry_style)
        self.entry_tinggi.grid(row=1, column=1, pady=5, padx=5)

        # Label dan Entry untuk Usia
        ttk.Label(main_frame, text="Usia:", **label_style).grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
        self.entry_usia = ttk.Entry(main_frame, **entry_style)
        self.entry_usia.grid(row=2, column=1, pady=5, padx=5)

        # Label dan Radiobutton untuk Jenis Kelamin
        ttk.Label(main_frame, text="Jenis Kelamin:", **label_style).grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)
        self.jenis_kelamin = tk.IntVar()
        self.radio_laki_laki = ttk.Radiobutton(main_frame, text="Laki-laki", variable=self.jenis_kelamin, value=1, style='TRadiobutton')
        self.radio_laki_laki.grid(row=3, column=1, sticky=tk.W, pady=5, padx=5)
        self.radio_perempuan = ttk.Radiobutton(main_frame, text="Perempuan", variable=self.jenis_kelamin, value=2, style='TRadiobutton')
        self.radio_perempuan.grid(row=3, column=2, sticky=tk.W, pady=5, padx=0)

        # Label dan Combobox untuk Tingkat Aktivitas
        aktivitas_values = ["Sangat Aktif", "Aktif", "Sedang", "Cukup Aktif", "Kurang Aktif"]
        ttk.Label(main_frame, text="Tingkat Aktivitas:", **label_style).grid(row=4, column=0, sticky=tk.W, pady=5, padx=5)
        self.aktivitas = ttk.Combobox(main_frame, **entry_style, state='readonly')
        self.aktivitas.grid(row=4, column=1, pady=5, padx=5)

        # Mengisi nilai-nilai untuk Combobox menggunakan perulangan
        for aktivitas in aktivitas_values:
            self.aktivitas['values'] = (*self.aktivitas['values'], aktivitas)

        hitung_button = ttk.Button(main_frame, text="Hitung", command=self.hitung_kalori, style='TButton')
        hitung_button.grid(row=5, column=0, columnspan=10, pady=10)

        self.label_hasil = ttk.Label(main_frame, text="", font=('Arial', 12, 'bold'), foreground='#007acc', background='#1e1e1e')
        self.label_hasil.grid(row=6, column=0, columnspan=2, pady=10)

    def set_berat(self, value):
        self._berat = value

    def get_berat(self):
        return self._berat

    def set_tinggi(self, value):
        self._tinggi = value

    def get_tinggi(self):
        return self._tinggi

    def set_usia(self, value):
        self._usia = value

    def get_usia(self):
        return self._usia

    def set_jenis_kelamin(self, value):
        self._jenis_kelamin = value

    def get_jenis_kelamin(self):
        return self._jenis_kelamin

    def set_tingkat_aktivitas(self, value):
        self._tingkat_aktivitas = value

    def get_tingkat_aktivitas(self):
        return self._tingkat_aktivitas

    def hitung_kalori(self):
        self.set_berat(int(self.entry_berat.get()))
        self.set_tinggi(int(self.entry_tinggi.get()))
        self.set_usia(int(self.entry_usia.get()))
        self.set_jenis_kelamin(self.jenis_kelamin.get())
        self.set_tingkat_aktivitas(self.aktivitas.get())

        bmr = self.hitung_bmr()
        kebutuhan_kalori = self.hitung_kebutuhan_kalori(bmr)

        self.label_hasil.config(text="Kebutuhan Kalori Anda: {:.2f} kalori".format(kebutuhan_kalori))

    def hitung_bmr(self):
        if self.get_jenis_kelamin() == 1:  # Laki-laki
            bmr = (10 * self.get_berat()) + (6.25 * self.get_tinggi()) - (5 * self.get_usia()) + 5
        else:  # Perempuan
            bmr = (10 * self.get_berat()) + (6.25 * self.get_tinggi()) - (5 * self.get_usia()) - 161
        return bmr

    def hitung_kebutuhan_kalori(self, bmr):
        aktivitas = self.get_tingkat_aktivitas()
        if aktivitas == "Sangat Aktif":
            kebutuhan_kalori = bmr * 1.725
        elif aktivitas == "Aktif":
            kebutuhan_kalori = bmr * 1.55
        elif aktivitas == "Sedang":
            kebutuhan_kalori = bmr * 1.375
        elif aktivitas == "Cukup Aktif":
            kebutuhan_kalori = bmr * 1.2
        else:
            kebutuhan_kalori = bmr * 1.1
        return kebutuhan_kalori

if __name__ == "__main__":
    app = KalkulatorKaloriGUI()
    app.mainloop()

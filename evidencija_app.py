import tkinter as tk
class Učenik:
    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred

    def __str__(self):
        return (f'{self.ime} {self.prezime} {self.razred}')
Pero=Učenik('Pero', 'Perić', '4.a')
print(Pero)

class EvidencijaApp:
    def __init__(self, root):
        self.root= root
        # --- Struktura prozora ---
        self.root.title("Evidencija učenika")
        self.root.geometry("500x400")
        # --- Konfiguracija responzivnosti ---
        # Glavni prozor: daj "težinu" stupcu 0 i redu 1 (gdje je lista)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        
        self.učenici = []
        self.odabrani_Učenik_index=None
        # --- Okviri (Frames) za organizaciju ---
        # Okvir za formu (unos)
        unos_frame = tk.Frame(self.root, padx=10, pady=10)
        unos_frame.grid(row=0, column=0, sticky="EW") # Rasteže se horizontalno
        # Okvir za prikaz (lista)
        prikaz_frame = tk.Frame(self.root, padx=10, pady=10)
        prikaz_frame.grid(row=1, column=0, sticky="NSEW") # Rasteže se u svim smjerovima
        # Responzivnost unutar okvira za prikaz
        prikaz_frame.columnconfigure(0, weight=1)
        prikaz_frame.rowconfigure(0, weight=1)
        # --- Widgeti za unos ---
        # Ime
        tk.Label(unos_frame, text="Ime:").grid(row=0, column=0, padx=5, pady=5, sticky="W")
        self.ime_entry = tk.Entry(unos_frame)
        self.ime_entry.grid(row=0, column=1, padx=5, pady=5, sticky="EW")
        # Prezime
        tk.Label(unos_frame, text="Prezime:").grid(row=1, column=0, padx=5, pady=5, sticky="W")
        self.prezime_entry = tk.Entry(unos_frame)
        self.prezime_entry.grid(row=1, column=1, padx=5, pady=5, sticky="EW")
        # Razred
        tk.Label(unos_frame, text="Razred:").grid(row=2, column=0, padx=5, pady=5, sticky="W")
        self.razred_entry = tk.Entry(unos_frame)
        self.razred_entry.grid(row=2, column=1, padx=5, pady=5, sticky="EW")
        # Gumbi
        self.dodaj_gumb = tk.Button(unos_frame, text="Dodaj učenika", command=self.dodaj_učenika)
        self.dodaj_gumb.grid(row=3, column=0, padx=5, pady=10)
        self.spremi_gumb = tk.Button(unos_frame, text="Spremi izmjene", command=self.spremi_izmjene)
        
        self.spremi_gumb.grid(row=3, column=1, padx=5, pady=10, sticky="W")
        # --- Widgeti za prikaz (NOVO GRADIVO: Listbox) ---
        self.listbox = tk.Listbox(prikaz_frame)
        self.listbox.grid(row=0, column=0, sticky="NSEW")
        # Scrollbar za listbox
        scrollbar = tk.Scrollbar(prikaz_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")
        self.listbox.config(yscrollcommand=scrollbar.set)


    

        # Povezivanje događaja odabira s našom metodom
        self.listbox.bind('<<ListboxSelect>>', self.odaberi_učenika)
        self.info_label = tk.Label(prikaz_frame, anchor='w')
        self.info_label.grid(row=1, column=0, columnspan=2, sticky='EW', pady=(8,0))

    def dodaj_učenika(self):
        ime = self.ime_entry.get().strip()
        prezime = self.prezime_entry.get().strip()
        razred = self.razred_entry.get().strip()
        if not(ime and prezime and razred):
            return
        self.učenici.append(Učenik(ime, prezime, razred))
        self.osvježi_listu()
        self.očisti_polja()
        

    def osvježi_listu(self):
        # Brisanje postojećih stavki
        self.listbox.delete(0, tk.END)
        # Dodavanje novih stavki
        for u in self.učenici:
            self.listbox.insert(tk.END, str(Učenik))


    def odaberi_učenika(self, event):
        # Dohvaćanje indeksa odabrane stavke
        odabrani_Učenik_index = self.listbox.curselection()
        if not odabrani_Učenik_index: # Ako ništa nije odabrano, izađi
            return

        odabrani_učenik_index = odabrani_učenik_index[0]
        self.odabrani_učenik_index = odabrani_učenik_index
        Učenik = self.učenici[odabrani_učenik_index]

        u=self.učenici[odabrani_učenik_index]
        self.ime_entry.delete(0, tk.END)
        self.ime_entry.insert(0, Učenik.ime)
        self.prezime_entry.delete(0, tk.END)
        self.prezime_entry.insert(0, Učenik.prezime)
        self.razred_entry.delete(0, tk.END)
        self.razred_entry.insert(0, Učenik.razred)
        
        # Prikaz informacije o odabranom artiklu
        self.info_label.config(text=f"Odabrali ste: {Učenik}")
        

    def spremi_izmjene(self):
        if self.odabrani_učenik_index is None:
            return
        ime = self.ime_entry.get().strip()
        prezime = self.prezime_entry_get().strip()
        razred = self.razred_entry_get().strip()
        if not(ime and prezime and razred):
            return
        u = self.učenici[self.odrabrani_učenici_index]
        u.ime, u.prezime, u.razred = ime, prezime, razred
        self.osvježi_listu()
        self.očisti_listu()
        self.info_label(text='Izmjene su spremljene')
        self.odabrani_učenik_index=None

    def očisti_polja(self):
        self.ime_entry.delete(0, tk.END)
        self.prezime_entry.delete(0, tk.END)
        self.razred_entry.delete(0, tk.END)
        
# Pokretanje primjera
if __name__ == "__main__":
     root = tk.Tk()
     app = EvidencijaApp(root)
     root.mainloop()


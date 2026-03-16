import customtkinter as ctk
import datetime
from tkinter import messagebox, ttk
from database import Database
from logic import AlertSystem

class PharmacyGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.title("Smart Pharmacy System")
        self.geometry("900x600") # قمنا بتوسيع النافذة لعرض الجدول
        ctk.set_appearance_mode("dark")

        # تقسيم الواجهة لجزأين: يسار للإدخال ويمين للعرض
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- الجزء الأيسر: الإدخال ---
        self.input_frame = ctk.CTkFrame(self, width=300)
        self.input_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.label = ctk.CTkLabel(self.input_frame, text="Add Medicine", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.name_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Medicine Name")
        self.name_entry.pack(pady=10, padx=20, fill="x")

        self.price_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Price")
        self.price_entry.pack(pady=10, padx=20, fill="x")

        self.stock_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Stock Quantity")
        self.stock_entry.pack(pady=10, padx=20, fill="x")

        self.expiry_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Expiry (YYYY-MM-DD)")
        self.expiry_entry.pack(pady=10, padx=20, fill="x")

        self.add_btn = ctk.CTkButton(self.input_frame, text="Save Medicine", command=self.save_medicine, fg_color="green")
        self.add_btn.pack(pady=20, padx=20, fill="x")

        self.alert_btn = ctk.CTkButton(self.input_frame, text="Show Alerts", command=self.show_alerts)
        self.alert_btn.pack(pady=10, padx=20, fill="x")

        # --- الجزء الأيمن: جدول البيانات ---
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.table_label = ctk.CTkLabel(self.table_frame, text="Inventory Records", font=("Arial", 20, "bold"))
        self.table_label.pack(pady=10)

        # استخدام Treeview من tkinter لعرض الجدول بشكل كلاسيكي منظم
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=30)
        self.style.map("Treeview", background=[('selected', '#1f538d')])

        self.tree = ttk.Treeview(self.table_frame, columns=("ID", "Name", "Price", "Stock", "Expiry"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Expiry", text="Expiry Date")

        self.tree.column("ID", width=50)
        self.tree.column("Name", width=150)
        self.tree.column("Price", width=70)
        self.tree.column("Stock", width=70)
        self.tree.column("Expiry", width=100)

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)

        self.load_table_data()

    def load_table_data(self):
        # مسح الجدول القديم
        for row in self.tree.get_children():
            self.tree.delete(row)

        # سحب البيانات الجديدة من القاعدة
        data = self.db.get_all()
        for m in data:
            self.tree.insert("", "end", values=m)

    def save_medicine(self):
        m_id = str(int(datetime.datetime.now().timestamp()))
        name = self.name_entry.get()
        price = self.price_entry.get()
        stock = self.stock_entry.get()
        expiry = self.expiry_entry.get()

        if name and price and stock and expiry:
            try:
                if self.db.add_med(m_id, name, float(price), int(stock), expiry):
                    messagebox.showinfo("Success", "Medicine recorded!")
                    self.clear_entries()
                    self.load_table_data() # تحديث الجدول فوراً بعد الحفظ
            except ValueError:
                messagebox.showerror("Error", "Check price and stock format.")
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def clear_entries(self):
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.stock_entry.delete(0, 'end')
        self.expiry_entry.delete(0, 'end')

    def show_alerts(self):
        data = self.db.get_all()
        alerts = AlertSystem(data)
        low = alerts.check_low_stock()
        exp = alerts.check_expiring_soon()

        msg = f"Low Stock Items: {len(low)}\nItems Expiring Soon: {len(exp)}"
        messagebox.showinfo("Inventory Health", msg)
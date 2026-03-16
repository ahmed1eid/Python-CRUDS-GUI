import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("pharmacy.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                            CREATE TABLE IF NOT EXISTS medicines (
                                                                     id TEXT PRIMARY KEY,
                                                                     name TEXT,
                                                                     price REAL,
                                                                     stock INTEGER,
                                                                     expiry TEXT
                            )
                            """)
        self.conn.commit()

    def add_med(self, id, name, price, stock, expiry):
        try:
            # تأكد من إرسال expiry كنص (String)
            self.cursor.execute("INSERT INTO medicines VALUES (?, ?, ?, ?, ?)",
                                (str(id), str(name), float(price), int(stock), str(expiry)))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error adding: {e}")
            return False

    def get_all(self):
        self.cursor.execute("SELECT id, name, price, stock, expiry FROM medicines")
        return self.cursor.fetchall()
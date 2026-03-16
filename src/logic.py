import datetime

class AlertSystem:
    def __init__(self, db_data):
        self.data = db_data

    def check_low_stock(self, threshold=10):
        return [m[1] for m in self.data if m[3] <= threshold]

    def check_expiring_soon(self, days_limit=30):
        today = datetime.date.today()
        expiring = []
        for m in self.data:
            try:
                # التأكد من تحويل القيمة لنص قبل معالجتها
                date_str = str(m[4])
                exp_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                if (exp_date - today).days <= days_limit:
                    expiring.append(m[1])
            except (ValueError, TypeError):
                continue
        return expiring
# 🍽️ Eatzy – Restaurant Vendor Management System

Eatzy is a full-stack Django-based web application designed to manage restaurant vendors and enable users to browse restaurants, view menus, add food items to a cart, and place orders. The system supports **role-based access** for **Customers**, **Vendors**, and **Admins**, providing separate dashboards and workflows for each role.

---

## 🚀 Features

### 👤 User (Customer)
- User registration & login  
- Profile management  
- Browse restaurants  
- View restaurant menus  
- Add food items to cart  
- Update cart item quantities  
- Automatic bill calculation (subtotal, tax, delivery fee)

### 🏪 Vendor
- Vendor registration with restaurant details  
- Upload restaurant image and license  
- Vendor approval workflow  
- Vendor dashboard  
- Add, edit, and delete food menu items  
- Update vendor profile information  

### 🛠️ Admin (Extendable)
- Vendor approval control  
- Role-based dashboard logic  

---

## 🧱 Tech Stack

- Backend: Python, Django  
- Frontend: HTML, CSS, Bootstrap 5  
- Forms: Django Crispy Forms  
- Database: SQLite (PostgreSQL-ready)  
- Authentication: Django Auth & Sessions  

---

## 🗂️ Project Structure

Eatzy/
│
├── accounts/
├── venders/
├── cart/
├── templates/
├── static/
├── media/
├── db.sqlite3
└── manage.py

---

## 🧮 Cart Calculation Logic
- Subtotal = sum(price × quantity)  
- Tax = 12%  
- Delivery Fee = ₹5 per item  
- Grand Total = Subtotal + Tax + Delivery Fee  

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/eatzy.git
cd eatzy
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 📈 Future Enhancements
- Payment gateway  
- Order history  
- Admin approval panel  
- REST API  
- Cloud deployment  

---

## 👨‍💻 Author

Sachin Kumar Shah  
Email: sachin.k.shah13@gmail.com  
GitHub: https://github.com/sachinshah16  
LinkedIn: https://www.linkedin.com/in/sachin-shah16/

# Notes_App


This is a simple Note-Keeping Web App built using the Django framework. It allows users to register, log in, and perform full CRUD (Create, Read, Update, Delete) operations on their personal notes.

---

## 🚀 Features

- ✅ User Signup
- ✅ User Login & Logout (Authentication)
- ✅ Create Notes
- ✅ View All Notes
- ✅ Update Notes
- ✅ Delete Notes
- ✅ Access Control (Users can only see/manage their own notes)
- ✅ Class-Based Views (CBVs) for clean and maintainable code
- ✅ Django admin panel customization

---

## 🛠 Tech Stack

- **Backend**: Django
- **Frontend**: HTML + Django Templates
- **Database**: SQLite3 (default)
- **Authentication**: Django’s built-in `auth` system
- **Forms**: Django’s built-in `UserCreationForm` and `ModelForm`

---

## 🔐 Authentication System

- Only registered users can access the app features.
- Used `LoginRequiredMixin` to protect views.
- Redirects users to login page if not authenticated.

---

## 💾 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/note-keeping-app.git
   cd note-keeping-app
   
2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
      pip install -r requirements.txt

4. **Run Migrations**
   ```bash
      python manage.py migrate

5. **Create Superuser (Optional)**
   ```bash
      python manage.py createsuperuser


6. **Start the Development Server**
   ```bash
      python manage.py runserver
   
7. **Open in Browser**

    http://127.0.0.1:8000/

📁 App Structure
   ```bash
   note_keeping_app/
   ├── note/                  # Main Django app
   │   ├── templates/         # HTML templates
   │   ├── views.py           # Class-based views
   │   ├── models.py          # Note model
   │   └── forms.py           # User and Note forms
   ├── note_keeping_app/      # Project config
   ├── db.sqlite3             # Database
   └── manage.py
 ```
✅ What I Learned

    Django project structure

    Class-Based Views (ListView, CreateView, UpdateView, DeleteView, FormView)

    User authentication system

    URL routing (app-level and project-level)

    CSRF protection and form handling

    CRUD operations with Django ORM

📌 Next Steps

Add Django REST Framework API (for mobile or frontend use)

Add note tags or categories

Add search functionality

    Use TailwindCSS or Bootstrap for styling


🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
📄 License




# Django Practical Guide – Course Code

This repository contains my progress and practice code from the **Django Practical Guide** course.  
Each folder corresponds to a section of the course, with step-by-step projects covering templates, static files, models, admin, forms, sessions, class-based views, file uploads, and more.

---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/django-practical-guide.git
   cd django-practical-guide
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows (PowerShell):
     ```bash
     venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run a Django project**
   - Navigate to the desired section (e.g. `010_Forms`)  
   - Run:
     ```bash
     python manage.py runserver
     ```

---

## 📂 Repository Structure

| Folder | Description |
|--------|-------------|
| `002_setupProject` | Setting up the first Django project |
| `003_url_view_mapper/monthley_challenges` | Mapping URLs to views |
| `004_Templates_Static_Files/monthley_challenges` | Working with templates & static files |
| `005_Blog_The_Basic/src` | Basic blog project setup |
| `006_data_and_models/BOOK_STORE` | Working with models & databases |
| `007_Admin/BOOK_STORE` | Customizing the Django admin |
| `008_Relationships` | Defining model relationships |
| `009_Course_Project_Building_a_blog` | Blog project – adding comments |
| `010_Forms` | Creating and handling forms |
| `011_Class_Views` | Using class-based views |
| `012_File_Uploads` | Handling file uploads |
| `013_Session` | Working with sessions |
| `014_Course_Project_Building_a_Blog - Forms_Files_Sessions` | Blog project – advanced features |
| `016_Django_Summary_Quick_Introduction` | Final summary & best practices |

---

## 🛠 Features Covered
- Django project setup & configuration  
- URL mapping & views  
- Templates & static files  
- Models, migrations, and database relations  
- Django Admin customization  
- Forms & ModelForms  
- Sessions & authentication basics  
- Class-based views (CBVs)  
- File uploads & media handling  
- Building a blog project step by step  

---

## 📖 Useful Django Commands

- Start a new project:  
  ```bash
  django-admin startproject project_name
  ```

- Create a new app:  
  ```bash
  python manage.py startapp app_name
  ```

- Apply migrations:  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- Create superuser:  
  ```bash
  python manage.py createsuperuser
  ```

- Collect static files:  
  ```bash
  python manage.py collectstatic
  ```

- Run development server:  
  ```bash
  python manage.py runserver
  ```

---

## 👨‍💻 Author
- **Name**: Mohammed El-Idrissi  
- **GitHub**: [@ingemedical16](https://github.com/ingemedical16)  

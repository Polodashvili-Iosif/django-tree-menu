# django-tree-menu

![Workflow Status](https://github.com/Polodashvili-Iosif/django-tree-menu/actions/workflows/main.yml/badge.svg)

Reusable Django app for rendering tree-structured menus using a custom template tag. Supports multiple named menus, active item highlighting based on the current URL, and optimized for a single DB query per menu. Fully manageable via Django admin.

### Installation:

Cloning the repository:

```bash
git clone https://github.com/Polodashvili-Iosif/django-tree-menu.git
```

Navigate to the project directory:

```bash
cd django-tree-menu
```

Create and activate a virtual environment:

For Unix/MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run migrations, upload data and create an administrator:

```bash
cd menu_project
python manage.py migrate
python manage.py loaddata menu_data.json
python manage.py createsuperuser
```

### Usage:

Run development server:

```bash
python manage.py runserver
```
Open your browser and go to:

http://127.0.0.1:8000/

# djangoModels

This work, we created a new model called post that has the following attributes: Title, Text,Author, Created_date and published date.
steps followed:
1. go to models to py and create a new class called post wiith the above attributes. Ensure you use the correct variable type
2. then go to setting and inculde the app name (in this case, the app is called blog) under installed_apps = ['blog']
3. go to terminal and first create migration using python manage.py makemigrations
4. then type in the terminal again python manage.py migrate

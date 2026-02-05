# Django Templates - Class Notes

## 1. Introduction to Django Templates

* Django templates are used to separate **Python logic** from **HTML presentation**.
* Templates allow you to dynamically generate HTML pages.
* They support **variables**, **tags**, **filters**, and **template inheritance**.

## 2. Template Folder Structure

* By default, Django looks for templates inside a folder named `templates` in your app or project.

Example:

```
myapp/
    templates/
        myapp/
            home.html
            about.html
```

* Project-level templates can be placed in `projectname/templates/`.

## 3. Using Templates in Views

```python
from django.shortcuts import render

def home(request):
    context = {'name': 'Bisham', 'age': 20}
    return render(request, 'myapp/home.html', context)
```

* `render()` takes 3 arguments: `request`, `template_name`, and optional `context`.
* `context` is a dictionary passed to the template.

## 4. Template Variables

* Use `{{ variable_name }}` to display context variables.

Example (`home.html`):

```html
<h1>Welcome, {{ name }}!</h1>
<p>Your age is {{ age }}.</p>
```

## 5. Template Tags

* Control flow and logic in templates.
* Common tags:

  * `{% if %} ... {% endif %}`
  * `{% for item in list %} ... {% endfor %}`
  * `{% block %} ... {% endblock %}` (for inheritance)
  * `{% extends 'base.html' %}`
  * `{% include 'header.html' %}`

Example:

```html
{% if age >= 18 %}
<p>You are an adult.</p>
{% else %}
<p>You are a minor.</p>
{% endif %}

<ul>
{% for hobby in hobbies %}
  <li>{{ hobby }}</li>
{% endfor %}
</ul>
```

## 6. Template Filters

* Modify variables for display.
* Common filters:

  * `{{ name|upper }}` → uppercase
  * `{{ name|lower }}` → lowercase
  * `{{ price|floatformat:2 }}` → 2 decimal places
  * `{{ date|date:'D M Y' }}` → format date

## 7. Template Inheritance

* Allows **reusing common HTML structure**.

Example (`base.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>{% include 'header.html' %}</header>
    <main>{% block content %}{% endblock %}</main>
    <footer>{% include 'footer.html' %}</footer>
</body>
</html>
```

Example (`home.html`):

```html
{% extends 'base.html' %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome, {{ name }}</h1>
<p>Enjoy your stay!</p>
{% endblock %}
```

## 8. Including Static Files

* Static files (CSS, JS, images) are used in templates.
* Example:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'myapp/style.css' %}">
<img src="{% static 'myapp/logo.png' %}" alt="Logo">
```

## 9. Summary

* Templates separate **logic** from **presentation**.
* Use **variables** to display data.
* Use **tags** for control flow and logic.
* Use **filters** to format output.
* Use **inheritance** and **include** to reuse code.
* Load static files for styling and scripts.

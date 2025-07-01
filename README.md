# ProyectoCoder

Este es un proyecto desarrollado con [Django](https://www.djangoproject.com/) para la cursada de CoderHouse.

## Requisitos

- Python 3.11 o superior
- pip

## Instalación

1. **Clonar el repositorio**

   ```sh
   git clone <url-del-repo>
   cd primeraApp
   ```

2. **Crear y activar un entorno virtual (opcional pero recomendado)**

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias**

   ```sh
   pip install -r requirements.txt
   ```

## Configuración inicial

1. **Aplicar migraciones**

   ```sh
   python manage.py migrate
   ```

2. **Crear un superusuario (opcional, para acceder al admin)**

   ```sh
   python manage.py createsuperuser
   ```

3. **Levantar el servidor de desarrollo**

   ```sh
   python manage.py runserver
   ```

   El proyecto estará disponible en [http://127.0.0.1:8000/app/](http://127.0.0.1:8000/app/)

## Estructura del proyecto

- `AppCoder/`: Aplicación principal con modelos, vistas, formularios y urls.
- `ProyectoCoder/`: Configuración global del proyecto Django.
- `templates/`: Plantillas HTML.
- `static/`: Archivos estáticos (CSS, JS, imágenes).
- `requirements.txt`: Dependencias del proyecto.

## Comandos útiles

- Aplicar migraciones:  
  `python manage.py migrate`
- Crear nuevas migraciones:  
  `python manage.py makemigrations`
- Crear superusuario:  
  `python manage.py createsuperuser`
- Levantar el servidor:  
  `python manage.py runserver`

## Notas

- Para agregar nuevas apps, usar:  
  `python manage.py startapp nombre_app`
- Para acceder al panel de administración:  
  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---
CoderHouse · Django · Python
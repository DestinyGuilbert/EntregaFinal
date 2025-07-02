# Proyecto Django - Blog Personal

Este es un proyecto desarrollado con Django para gestión de usuarios y páginas tipo blog.

---

## Requisitos

- Python 3.11 o superior  
- pip  

---

## Instalación

1. Clonar el repositorio  
git clone <url-del-repo>
cd Roxanne_Colosia

2. Crear y activar un entorno virtual (opcional pero recomendado)  
En Linux/Mac: 
python -m venv .venv
source .venv/bin/activate  

En Windows:  
python -m venv .venv
.venv\Scripts\activate


3. Instalar dependencias  
pip install -r requirements.txt


---

## Configuración inicial

1. Aplicar migraciones  
python manage.py migrate

2. Crear un superusuario (opcional para acceder al admin)  
python manage.py createsuperuser


3. Levantar el servidor de desarrollo  
python manage.py runserver


4. El proyecto estará disponible en:  
`http://127.0.0.1:8000/`

---

## Estructura del proyecto

- `AppCoder/` : Aplicación principal con modelos, vistas, formularios y urls.  
- `Cuentas/` : Aplicación para manejo de usuarios y autenticación.  
- `Mensajes/` : Aplicación para mensajería interna entre usuarios.  
- `templates/` : Plantillas HTML con herencia.  
- `static/` : Archivos estáticos (CSS, JS, imágenes).  
- `media/` : Archivos subidos por usuarios (no subir al repositorio).  
- `requirements.txt` : Dependencias del proyecto.  

---

## Comandos útiles

- Aplicar migraciones:  
python manage.py migrate
- Crear migraciones nuevas:  
python manage.py makemigrations
- Crear superusuario:  
python manage.py createsuperuser
- Levantar servidor:  
python manage.py runserver
- Crear nueva app:  
python manage.py startapp nombre_app

---

## Notas

- No subir la base de datos (`db.sqlite3`) ni la carpeta `media/` al repositorio.  
- Usar el archivo `.gitignore` para excluirlos.  
- Formularios que manejan imágenes deben usar `enctype="multipart/form-data"`.  
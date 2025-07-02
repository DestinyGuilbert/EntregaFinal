# Proyecto Django - Blog Personal

Este es un proyecto desarrollado con Django para gestión de usuarios y páginas tipo blog.

---

## Requisitos

- Python 3.11 o superior  

---

## Instalación

1. Clonar el repositorio  
git clone <https://github.com/DestinyGuilbert/EntregaFinal>
cd Entrega Final

2. Instalar dependencias  
pip install -r requirements.txt

---

## Configuración inicial

1. Levantar el servidor de desarrollo  
python manage.py runserver


2. El proyecto estará disponible en:  
`http://127.0.0.1:8000/`

---

## Estructura del proyecto

- `AppCoder/` : Aplicación principal con modelos, vistas, formularios y urls.  
- `Cuentas/` : Aplicación para manejo de usuarios y autenticación.  
- `templates/` : Plantillas HTML con herencia.  
- `static/` : Archivos estáticos (CSS, JS, imágenes).  
- `media/` : Archivos subidos por usuarios (no subir al repositorio).  
- `requirements.txt` : Dependencias del proyecto.  

---

## Comandos útiles

- Crear superusuario:  
python manage.py createsuperuser

- Levantar servidor:  
python manage.py runserver

---
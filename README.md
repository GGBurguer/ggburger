# GGBurger - Sistema de Gestión

Sistema de gestión integral diseñado para el emprendimiento de comida rápida GGBurger. Esta plataforma centraliza la administración de pedidos, inventarios y operaciones utilizando Django.

## 🚀 Tecnologías y Herramientas

* Backend: Django 6.0.5
* Gestor de Proyectos: uv (Gestión de dependencias de alta velocidad)
* Base de Datos: SQLite (Desarrollo) / PostgreSQL (Soporte mediante psycopg2-binary)
* Contenerización: Docker (ver carpeta /docker)
* Gestión de Entorno: python-dotenv

## 📂 Estructura del Proyecto

El proyecto sigue una arquitectura organizada, separando la configuración central (core) de las aplicaciones específicas (apps):
```text
.
├── docker/             # Configuración de contenedores
├── manage.py           # Script de gestión de Django
├── pyproject.toml      # Configuración de uv
├── src/                # Código fuente
│   ├── apps/           # Aplicaciones modulares
│   └── core/           # Configuración del proyecto (settings, urls, etc.)
└── uv.lock             # Bloqueo de dependencias de alta precisión
```

## 🛠️ Instalación y Configuración

Este proyecto utiliza uv para la gestión de dependencias. Asegúrate de tenerlo instalado en tu sistema.

1. Clonar el repositorio:
```bash
git clone https://github.com/GGBurguer/ggburger
cd ggburger
```

2. Sincronizar dependencias:
```bash
uv sync
```

3. Variables de entorno:
   	Crea un archivo .env en la raíz y configura tus variables (como SECRET_KEY y configuración de base de datos).

4. Ejecutar migraciones:
```bash
uv run python manage.py migrate
```

5. Iniciar el servidor de desarrollo:
```bash
uv run python manage.py runserver
```

## 🐳 Docker (Opcional)

Para ejecutar el proyecto en contenedores, utiliza los archivos ubicados en la carpeta docker/. Asegúrate de tener Docker instalado y ejecuta:
```bash
docker compose up --build
```

## 📋 Dependencias Principales

* Django: 6.0.5
* psycopg2-binary: 2.9.12
* python-dotenv: 1.2.2

Ejecute:
```bash
uv add -r requirements/requirements-dev.txt
```

> [!IMPORTANT]
> Solamente debe ser empleado si la sincronización mediante UV falla; de otro modo, se recomienda siempre sincronizar en vez de utilizar el fichero de dependencias manualmente.

---
Desarrollado por AnalyticsDevs <3.
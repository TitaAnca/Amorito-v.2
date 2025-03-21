# Amorito-v.2

Comandos para subir los archivos
Todos los comandos se han de ejecutar en la terminal del visual

esenciales


git remote add origin <(https://github.com/TitaAnca/Amorito-v.2)>

git pull <https://github.com/TitaAnca/Amorito-v.2> main

1. git add <nombre del archivo "ejemplo.html">
2. git commit <ejemplo.html>
3. git push -u origin main


Amorito-v.2/
│
├── app/                 # Carpeta principal que contiene el código de la API
│   ├── __init__.py      # Inicializa la aplicación Flask/FastAPI
│   ├── config.py        # Archivo de configuración global
│   ├── controllers/     # Controladores que manejan las solicitudes
│   │   ├── userController.py
│   │   └── productController.py
│   ├── models/          # Modelos que interactúan con los archivos JSON
│   │   ├── userModel.py
│   │   └── productModel.py
│   ├── routes/          # Rutas de la API
│   │   ├── userRoutes.py
│   │   └── productRoutes.py
│   ├── middleware/      # Middleware para validaciones, autenticación, etc.
│   │   ├── authMiddleware.py
│   │   └── validateMiddleware.py
│   ├── services/        # Lógica de negocio
│   │   ├── userService.py
│   │   └── productService.py
│   └── utils/           # Utilidades, como funciones para leer y escribir archivos JSON
│       └── fileUtils.py
│
├── db/                  # Carpeta que contiene los archivos JSON (como base de datos)
│   ├── users.json       # Datos de usuarios
│   └── products.json    # Datos de productos
│
├── public/              # Archivos estáticos que serán servidos por la API
│   ├── images/          # Imágenes (por ejemplo, productos, perfiles, etc.)
│   ├── css/             # Hojas de estilo CSS
│   ├── js/              # Archivos JavaScript
│   └── index.html       # Si tienes una página HTML estática
│
├── tests/               # Pruebas unitarias para la API
│   ├── test_user.py
│   └── test_product.py
│
├── .gitignore           # Para ignorar archivos no necesarios en el repositorio
├── requirements.txt     # Listado de dependencias de Python
├── run.py               # Archivo para ejecutar la API
└── README.md            # Documentación del proyecto



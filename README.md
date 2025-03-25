# Amorito-v.2

Comandos para subir los archivos
Todos los comandos se han de ejecutar en la terminal del visual

esenciales


git remote add origin <(https://github.com/TitaAnca/Amorito-v.2)>

git pull <https://github.com/TitaAnca/Amorito-v.2> main

1. git add <nombre del archivo "ejemplo.html">
2. git commit -m <ejemplo.html>
3. git push -u origin main

-------------------------------------------------------------------------------------------

Amorito-v.2/
│
├── app/                     # Carpeta principal con el código de la API
│   ├── __init__.py          # Inicializa la aplicación Flask/FastAPI
│   ├── config.py            # Configuración global de la aplicación
│   ├── controllers/         # Controladores para manejar las solicitudes HTTP
│   │   ├── authController.py      # Controlador para el login, registro y autenticación
│   │   ├── userController.py      # Controlador para la gestión de usuarios
│   │   ├── matchController.py     # Controlador para las coincidencias de usuarios
│   │   └── messageController.py   # Controlador para los mensajes entre usuarios
│   ├── models/              # Modelos que representan las entidades principales
│   │   ├── userModel.py         # Modelo para el usuario
│   │   ├── matchModel.py        # Modelo para las coincidencias de usuarios
│   │   └── messageModel.py      # Modelo para los mensajes
│   ├── routes/              # Rutas para manejar las solicitudes API
│   │   ├── authRoutes.py        # Rutas de autenticación (login, registro)
│   │   ├── userRoutes.py        # Rutas para la gestión de usuarios
│   │   ├── matchRoutes.py       # Rutas para gestionar las coincidencias
│   │   └── messageRoutes.py     # Rutas para manejar los mensajes
│   ├── middleware/          # Middleware (ej. autenticación, validaciones)
│   │   ├── authMiddleware.py    # Middleware para manejar autenticación de JWT
│   │   └── validateMiddleware.py  # Middleware para validaciones comunes
│   ├── services/            # Lógica de negocio (interacción con modelos)
│   │   ├── authService.py       # Lógica de autenticación, registro y JWT
│   │   ├── userService.py       # Lógica para el manejo de perfiles de usuario
│   │   ├── matchService.py      # Lógica para la creación de coincidencias
│   │   └── messageService.py    # Lógica para el manejo de mensajes
│   └── utils/               # Utilidades generales y helpers
│       ├── fileUtils.py       # Funciones para manejo de archivos (subida de imágenes, etc.)
│       ├── tokenUtils.py      # Funciones para manejar JWT
│       └── validationUtils.py  # Funciones de validación de datos comunes
│
├── db/                      # Carpeta que contiene las "bases de datos" (JSON o base de datos relacional)
│   ├── users.json            # Información de usuarios (si usas JSON)
│   ├── matches.json          # Datos de las coincidencias entre usuarios
│   └── messages.json         # Mensajes enviados entre usuarios
│
├── public/                  # Archivos estáticos (imágenes, videos, etc.)
│   ├── images/              # Imágenes de perfil de los usuarios, fotos compartidas
│   ├── css/                 # Hojas de estilo CSS para la web (si usas plantillas)
│   ├── js/                  # Archivos JavaScript para la interacción en frontend
│   └── index.html           # Página HTML principal si la sirves desde la misma API
│
├── tests/                   # Pruebas unitarias de la API
│   ├── test_auth.py         # Pruebas para el login y autenticación
│   ├── test_user.py         # Pruebas para la gestión de usuarios
│   ├── test_match.py        # Pruebas para el emparejamiento de usuarios
│   └── test_message.py      # Pruebas para los mensajes entre usuarios
│
├── .gitignore               # Archivos y carpetas a ignorar en el control de versiones
├── requirements.txt         # Dependencias del proyecto en Python
├── run.py                   # Archivo para ejecutar la API
└── README.md                # Documentación del proyecto



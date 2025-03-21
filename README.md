# Amorito-v.2

Comandos para subir los archivos
Todos los comandos se han de ejecutar en la terminal del visual

esenciales


git remote add origin <(https://github.com/TitaAnca/Amorito-v.2)>

git pull <https://github.com/TitaAnca/Amorito-v.2> main

1. git add <nombre del archivo "ejemplo.html">
2. git commit <ejemplo.html>
3. git push -u origin main


my-api/
│
├── config/           # Archivos de configuración (DB, API keys, etc.)
│
├── controllers/      # Controladores, donde se definen las funciones de las rutas
│   ├── userController.js
│   ├── authController.js
│
├── models/           # Modelos de base de datos (si usas ORM como Sequelize, Mongoose, etc.)
│   ├── userModel.js
│   ├── productModel.js
│
├── routes/           # Definición de rutas (rutas de API)
│   ├── userRoutes.js
│   ├── authRoutes.js
│
├── middleware/       # Middleware (autenticación, validación, etc.)
│   ├── authMiddleware.js
│   ├── validateMiddleware.js
│
├── services/         # Lógica de negocio (si no está en el controlador)
│   ├── userService.js
│   ├── paymentService.js
│
├── utils/            # Utilidades (funciones reutilizables)
│   ├── logger.js
│   ├── helpers.js
│
├── public/           # Archivos estáticos (si los hay, como imágenes o documentos)
│
├── tests/            # Pruebas (unitarias, de integración, etc.)
│   ├── user.test.js
│   ├── auth.test.js
│
├── app.js            # Archivo principal de la API (punto de entrada)
├── package.json      # Dependencias y configuraciones del proyecto
└── README.md         # Documentación del proyecto


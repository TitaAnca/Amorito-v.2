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
├── config/               # Archivos de configuración
│   └── dbConfig.js       # Configuración general de la "base de datos" (archivos JSON)
│
├── controllers/          # Controladores que manejan la lógica de negocio
│   ├── userController.js
│   └── productController.js
│
├── models/               # Modelos que interactúan con los archivos JSON
│   ├── userModel.js      # Modelo de usuario (operaciones sobre el archivo JSON de usuarios)
│   └── productModel.js   # Modelo de producto
│
├── routes/               # Rutas de la API
│   ├── userRoutes.js
│   └── productRoutes.js
│
├── middleware/           # Middleware para validaciones y autenticación
│   ├── authMiddleware.js
│   └── validateMiddleware.js
│
├── services/             # Lógica de negocio más compleja
│   ├── userService.js
│   └── productService.js
│
├── utils/                # Funciones auxiliares, como un logger o manipuladores de archivos JSON
│   └── fileUtils.js      # Funciones para leer y escribir archivos JSON
│
├── public/               # Archivos estáticos (si los hay)
│
├── tests/                # Pruebas unitarias de la API
│   ├── user.test.js
│   └── product.test.js
│
├── db/                   # Carpeta que almacena los archivos JSON que simulan bases de datos
│   ├── users.json        # Archivo JSON que contiene todos los usuarios
│   └── products.json     # Archivo JSON que contiene los productos
│
├── app.js                # Archivo principal de la API
├── package.json          # Dependencias y configuraciones del proyecto
└── README.md             # Documentación del proyecto


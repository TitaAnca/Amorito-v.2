document.getElementById('registroForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Obtener los valores del formulario
    const id_usuario = document.getElementById('id_usuario').value;
    const nombre_usuario = document.getElementById('nombre_usuario').value;
    const contrasena = document.getElementById('contrasena').value;
    const edad = document.getElementById('edad').value;
    const genero = document.getElementById('genero').value;
    const orientacion_sexual = document.getElementById('orientacion_sexual').value;

    // Crear el objeto de datos
    const datos = {
        id_usuario,
        nombre_usuario,
        contrasena,
        edad,
        genero,
        orientacion_sexual
    };

    // Enviar los datos al backend usando Fetch API
    fetch('/auth/registrar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensaje);
        if (data.mensaje === "Usuario registrado exitosamente") {
            // Redirigir al login o a la página principal
            window.location.href = '/login.html';  // Redirigir a la página de login
        }
    })
    .catch(error => console.error('Error:', error));
});


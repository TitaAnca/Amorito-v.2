document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Evitar el comportamiento por defecto del formulario
    
    const id_usuario = document.getElementById('id_usuario').value;
    const contrasena = document.getElementById('contrasena').value;

    const datos = {
        id_usuario: id_usuario,
        contrasena: contrasena
    };

    // Hacer una solicitud POST para iniciar sesión
    fetch('/auth/iniciar-sesion', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(datos)
    })
    .then(response => {
        if (response.ok) {
            // Redirigir al usuario a su página de Matches personalizada
            window.location.href = `/matches/${id_usuario}`; 
        } else {
            return response.json().then(data => {
                alert(data.mensaje);  // Mostrar mensaje de error si el inicio de sesión falla
            });
        }
    })
    .catch(error => {
        alert('Error al iniciar sesión: ' + error);
    });
});

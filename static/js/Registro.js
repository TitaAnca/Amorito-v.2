document.getElementById('registroForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Crear un objeto FormData para enviar datos del formulario
    const formData = new FormData();

    // Obtener los valores del formulario
    formData.append('id_usuario', document.getElementById('id_usuario').value);
    formData.append('nombre_usuario', document.getElementById('nombre_usuario').value);
    formData.append('contrasena', document.getElementById('contrasena').value);
    formData.append('edad', document.getElementById('edad').value);
    formData.append('genero', document.getElementById('genero').value);
    formData.append('orientacion_sexual', document.getElementById('orientacion_sexual').value);
    formData.append('bio', document.getElementById('bio').value);

    // Obtener la foto de perfil (si existe)
    const foto = document.getElementById('foto_perfil').files[0];
    if (foto) {
        formData.append('foto_perfil', foto);
    }

    // Enviar los datos al backend usando Fetch API con FormData
    fetch('/auth/registrar', {
        method: 'POST',
        body: formData,  // FormData maneja todo el contenido, incluyendo archivos
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensaje);
        if (data.mensaje === "Usuario registrado correctamente") {
            // Redirigir al login o a la página principal
            window.location.href = '/inicio_sesion';  // Redirigir a la página de login
        }
    })
    .catch(error => console.error('Error:', error));
});

function vistaPrevia(event) {
    const input = event.target;
    const vistaPrevia = document.getElementById('vista-previa');
    
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            vistaPrevia.style.display = 'block';
            vistaPrevia.src = e.target.result;
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}


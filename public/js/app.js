document.addEventListener("DOMContentLoaded", () => {
    // Inicializar el perfil
    const perfilNombre = document.getElementById("perfil-nombre");
    const perfilBiografia = document.getElementById("perfil-biografia");
    const perfilEdad = document.getElementById("perfil-edad");
    const perfilImg = document.getElementById("perfil-img");

    const mensajeForm = document.getElementById("mensajeForm");
    const mensajeInput = document.getElementById("mensajeInput");
    const messagesContainer = document.getElementById("messages-container");

    const usuarioId = 1; // Simulamos que este es el ID del usuario logueado

    // Obtener el perfil desde la API o base de datos
    function cargarPerfil() {
        fetch(`/api/usuario/${usuarioId}`)
            .then(response => response.json())
            .then(data => {
                perfilNombre.textContent = data.nombre_usuario;
                perfilBiografia.textContent = data.biografia;
                perfilEdad.textContent = data.edad;
                perfilImg.src = data.imagen_url || 'images/profile.jpg'; // Si hay imagen, la usa, sino usa la predeterminada
            })
            .catch(error => console.error("Error al cargar el perfil", error));
    }

    // Cargar los mensajes
    function cargarMensajes() {
        fetch(`/api/mensajes/${usuarioId}`)
            .then(response => response.json())
            .then(data => {
                messagesContainer.innerHTML = '';
                data.forEach(mensaje => {
                    const divMensaje = document.createElement("div");
                    divMensaje.classList.add("message");
                    divMensaje.textContent = `${mensaje.remitente}: ${mensaje.texto}`;
                    messagesContainer.appendChild(divMensaje);
                });
            })
            .catch(error => console.error("Error al cargar los mensajes", error));
    }

    // Enviar mensaje
    mensajeForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const mensaje = {
            remitente: usuarioId,  // El ID del usuario logueado
            texto: mensajeInput.value
        };

        fetch("/api/enviar-mensaje", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(mensaje)
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensaje === "Mensaje enviado") {
                mensajeInput.value = ''; // Limpiar el campo de mensaje
                cargarMensajes(); // Volver a cargar los mensajes
            }
        })
        .catch(error => console.error("Error al enviar mensaje", error));
    });

    // Editar perfil
    document.getElementById("editarPerfilBtn").addEventListener("click", () => {
        const nuevoNombre = prompt("Nuevo nombre:", perfilNombre.textContent);
        const nuevaBiografia = prompt("Nueva biografía:", perfilBiografia.textContent);
        const nuevaEdad = prompt("Nueva edad:", perfilEdad.textContent);

        const perfilEditado = {
            id: usuarioId,
            nombre_usuario: nuevoNombre,
            biografia: nuevaBiografia,
            edad: nuevaEdad
        };

        fetch(`/api/editar-perfil/${usuarioId}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(perfilEditado)
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensaje === "Perfil actualizado") {
                cargarPerfil(); // Volver a cargar el perfil con los nuevos datos
            }
        })
        .catch(error => console.error("Error al editar perfil", error));
    });

    // Cargar datos al inicio
    cargarPerfil();
    cargarMensajes();
});

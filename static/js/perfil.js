document.addEventListener("DOMContentLoaded", () => {
    const editBtn = document.getElementById("edit-btn");
    const deleteBtn = document.getElementById("delete-btn");
    const editModal = document.getElementById("edit-modal");
    const closeEditModal = document.getElementById("close-edit-modal");
    const saveBtn = document.getElementById("save-btn");

    const username = document.getElementById("username");
    const handle = document.getElementById("handle");
    const location = document.getElementById("location");
    const memberDate = document.getElementById("member-date");
    const interests = document.getElementById("interests");

    const editUsername = document.getElementById("nombre_usuario");
    const editEdad = document.getElementById("edad");
    const editGenero = document.getElementById("genero");
    const editOrientacion = document.getElementById("orientacion_sexual");
    const editBio = document.getElementById("bio");
    const editFoto = document.getElementById("foto_perfil");

    // Mostrar el modal al hacer clic en editar
    editBtn.addEventListener("click", () => {
        editModal.style.display = "flex";
    });

    closeEditModal.addEventListener("click", () => {
        editModal.style.display = "none";
    });

    // Guardar los cambios
    saveBtn.addEventListener("click", async () => {
        const id_usuario = document.body.dataset.id;
        const nombre_usuario = editUsername.value.trim();
        const edad = parseInt(editEdad.value);
        const genero = editGenero.value;
        const orientacion = editOrientacion.value;
        const bio = editBio.value.trim();
        const foto = editFoto.files[0];

        // Validaciones
        if (!nombre_usuario) {
            alert("Por favor, ingresa un nombre de usuario.");
            return;
        }

        if (isNaN(edad) || edad < 18 || edad > 90) {
            alert("Por favor, ingresa una edad válida entre 18 y 90.");
            return;
        }

        if (!genero) {
            alert("Por favor, selecciona un género.");
            return;
        }

        if (!orientacion) {
            alert("Por favor, selecciona una orientación sexual.");
            return;
        }

        if (!bio) {
            alert("Por favor, ingresa una biografía.");
            return;
        }

        if (!foto) {
            alert("Por favor, selecciona una foto de perfil.");
            return;
        }

        // Crear FormData
        const formData = new FormData();
        formData.append("id_usuario", id_usuario);
        formData.append("nombre_usuario", nombre_usuario);
        formData.append("edad", edad);
        formData.append("genero", genero);
        formData.append("orientacion_sexual", orientacion);
        formData.append("bio", bio);
        formData.append("foto_perfil", foto);

        // Enviar al servidor
        const response = await fetch("/usuario/actualizar", {
            method: "PUT",
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            alert("Perfil actualizado correctamente");

            // Actualizar los datos del perfil
            username.innerText = nombre_usuario;
            location.innerText = edad;
            memberDate.innerText = genero;
            interests.innerText = orientacion;

            // Si se actualizó la biografía, también actualizarla en el perfil
            document.getElementById("bio").innerText = bio;

            // Si se cargó una nueva foto, actualizarla en el perfil
            const reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById("profile-pic").src = e.target.result;
            };
            reader.readAsDataURL(foto);

            // Cerrar el modal de edición
            editModal.style.display = "none";
        } else {
            alert("Error al actualizar perfil: " + data.mensaje);
        }
    });

    deleteBtn.addEventListener("click", async () => {
        const id_usuario = document.body.dataset.id;
        const confirmDelete = confirm("¿Estás seguro de que deseas eliminar tu cuenta?");
        if (confirmDelete) {
            const response = await fetch(`/usuario/eliminar/${id_usuario}`, {
                method: "DELETE",
            });

            const data = await response.json();

            if (response.ok) {
                alert("Cuenta eliminada correctamente");
                // Redirigir al usuario a la página de inicio o cerrar sesión
                window.location.href = "/";  // Redirige a la página de inicio
            } else {
                alert("Error al eliminar cuenta: " + data.mensaje);
            }
        }
    });
});

async function cargarPerfilUsuario() {
    fetch("/usuario/obtener/usuario123")  // Aquí pones el ID del usuario que se desea obtener
        .then(response => response.json())
        .then(perfil => {
            // Cargar los datos del usuario en la tarjeta de perfil
            document.getElementById("username").innerText = perfil.nombre_usuario;
            document.getElementById("handle").innerText = perfil.id_usuario;
            document.getElementById("location").innerText = perfil.edad;
            document.getElementById("member-date").innerText = perfil.genero;
            document.getElementById("interests").innerText = perfil.orientacion_sexual;

            // Actualizar la foto de perfil
            document.querySelector(".profile-image-container img").src = "/static" + perfil.foto_perfil.replace('static', '');
        })
        .catch(error => console.error("Error al obtener los datos del usuario:", error));

}

// Llamamos a la función al cargar la página
document.addEventListener("DOMContentLoaded", cargarPerfilUsuario);
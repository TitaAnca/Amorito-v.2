let perfiles = [];
let indiceActual = 0;
let idUsuario = document.body.getAttribute("data-id");  // Obtenemos el id_usuario desde el atributo data-id

// Cargar perfiles compatibles desde el backend
const cargarPerfiles = async () => {
    try {
        const res = await fetch(`/match/compatibles/${idUsuario}`);
        perfiles = await res.json();
        indiceActual = 0;
        mostrarPerfil();
    } catch (error) {
        console.error("Error cargando perfiles compatibles:", error);
    }
};

// Mostrar el perfil actual
const mostrarPerfil = () => {
    if (indiceActual < perfiles.length) {
        const perfil = perfiles[indiceActual];
        document.getElementById("name").textContent = perfil.nombre;
        document.getElementById("age").textContent = `Edad: ${perfil.edad}`;
        document.getElementById("bio").textContent = perfil.bio;
        document.querySelector(".card img").src = perfil.foto_perfil;
    } else {
        document.getElementById("profile-card").innerHTML = "<p>No hay más perfiles compatibles disponibles.</p>";
    }
};

// Handle para hacer un match
const manejarMatch = async () => {
    const perfil = perfiles[indiceActual];
    try {
        const res = await fetch('/match/crear_match', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                id_usuario1: idUsuario,
                id_usuario2: perfil.id_usuario
            })
        });

        const data = await res.json();

        if (res.ok) {
            alert(data.mensaje);
        } else {
            alert(data.error || "No se pudo hacer match.");
        }
    } catch (error) {
        alert("Error en el servidor.");
    }

    indiceActual++;
    mostrarPerfil();
};

const manejarRechazo = async () => {
    const perfil = perfiles[indiceActual];
    try {
        const res = await fetch('/match/rechazar_match', {
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                id_usuario1: idUsuario,
                id_usuario2: perfil.id_usuario
            })
        });

        const data = await res.json();

        if (res.ok) {
            alert(data.mensaje);  // Alerta con el mensaje de rechazo
        } else {
            alert(data.error || "No se pudo rechazar el perfil.");
        }
    } catch (error) {
        alert("Error en el servidor.");
    }

    // Avanzamos al siguiente perfil
    indiceActual++;
    mostrarPerfil();
};

// Inicializar la carga de perfiles cuando la página esté lista
document.addEventListener("DOMContentLoaded", cargarPerfiles);
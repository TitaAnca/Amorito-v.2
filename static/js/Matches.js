let perfiles = [];
let indiceActual = 0;
let idUsuario = document.body.getAttribute("data-id");

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

const handleMatch = async () => {
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

document.addEventListener("DOMContentLoaded", cargarPerfiles);
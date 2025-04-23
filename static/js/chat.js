document.addEventListener("DOMContentLoaded", () => {
    const idUsuario = document.body.dataset.id;
    let idReceptorActual = null;

    // Cargar matches al iniciar
    function cargarMatches(idUsuario) {
        fetch(`/match/matches/${idUsuario}`)
            .then(res => res.json())
            .then(data => {
                const matchesList = document.getElementById("matches-list");
                matchesList.innerHTML = "";

                if (data.length > 0) {
                    data.forEach(idMatch => {
                        const li = document.createElement("li");
                        li.textContent = idMatch;
                        li.dataset.id = idMatch;
                        li.classList.add("match-item");
                        matchesList.appendChild(li);
                    });
                } else {
                    const li = document.createElement("li");
                    li.textContent = "No tienes matches aún";
                    matchesList.appendChild(li);
                }
            })
            .catch(err => console.error("Error al cargar los matches", err));
    }

    // Cargar conversación
    function cargarConversacion(idUsuarioDestino) {
        if (!idUsuarioDestino) return;

        fetch(`/mensaje/conversacion/${idUsuario}/${idUsuarioDestino}`)
            .then(res => res.json())
            .then(data => {
                const mensajesDiv = document.getElementById("mensajes");
                mensajesDiv.innerHTML = "";

                data.forEach(mensaje => {
                    const mensajeDiv = document.createElement("div");
                    mensajeDiv.classList.add("mensaje");

                    // Alineación según emisor
                    if (mensaje.id_emisor === idUsuario) {
                        mensajeDiv.classList.add("mensaje-derecha");
                    } else {
                        mensajeDiv.classList.add("mensaje-izquierda");
                    }

                    mensajeDiv.innerHTML = `<span>${mensaje.contenido}</span>`;
                    mensajesDiv.appendChild(mensajeDiv);
                });
            })
            .catch(err => console.error("Error al cargar la conversación", err));
    }

    // Enviar mensaje
    function enviarMensaje() {
        const input = document.getElementById("mensaje-input");
        const contenido = input.value.trim();

        if (!contenido || !idReceptorActual) {
            alert("Selecciona un match y escribe un mensaje.");
            return;
        }

        fetch("/mensaje/enviar_mensaje", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: new URLSearchParams({
                id_emisor: idUsuario,
                id_receptor: idReceptorActual,
                contenido: contenido
            })
        })
        .then(res => {
            if (res.ok) {
                input.value = "";
                cargarConversacion(idReceptorActual);
            } else {
                throw new Error("Error al enviar mensaje");
            }
        })
        .catch(err => console.error(err));
    }

    // Enviar al presionar Enter
    const mensajeInput = document.getElementById("mensaje-input");
    mensajeInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            enviarMensaje();
        }
    });

    // Enviar con el botón
    const enviarBoton = document.getElementById("enviarBoton");
    enviarBoton.addEventListener("click", enviarMensaje);

    // Delegar clicks en los matches
    document.getElementById("matches-list").addEventListener("click", function (e) {
        if (e.target && e.target.matches(".match-item")) {
            idReceptorActual = e.target.dataset.id;
            document.getElementById("nombre-match").textContent = e.target.textContent;
            cargarConversacion(idReceptorActual);
        }
    });

    // Iniciar
    cargarMatches(idUsuario);
});


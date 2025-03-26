document.getElementById("registroForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = {
        nombre_usuario: document.getElementById("nombre_usuario").value,
        contrasena: document.getElementById("contrasena").value,
        biografia: document.getElementById("biografia").value,
        edad: document.getElementById("edad").value,
    };

    fetch("/api/registro", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensaje);
        if (data.mensaje === "Usuario creado exitosamente") {
            window.location.href = "app.html"; // Redirigir a la app
        }
    })
    .catch(error => console.error('Error:', error));
});

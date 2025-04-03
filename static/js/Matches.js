// Simulación de datos obtenidos de una base de datos
const profiles = [
    {
        name: "Juan Pérez",
        age: 28,
        bio: "Me encanta la música y los deportes.",
        photo: "https://via.placeholder.com/100?text=Juan"
    },
    {
        name: "María Gómez",
        age: 32,
        bio: "Amante de los libros y las caminatas al aire libre.",
        photo: "https://via.placeholder.com/100?text=Maria"
    }
];

let currentProfileIndex = 0;

// Función para mostrar el siguiente perfil
const loadProfile = () => {
    if (currentProfileIndex < profiles.length) {
        const profile = profiles[currentProfileIndex];
        document.getElementById("name").textContent = profile.name;
        document.getElementById("age").textContent = `Edad: ${profile.age}`;
        document.getElementById("bio").textContent = `Bio: ${profile.bio}`;
        document.querySelector(".card img").src = profile.photo;
    } else { 
        document.getElementById("profile-card").innerHTML = "<p>No hay más perfiles disponibles.</p>";
    }
};

// Funciones para manejar los botones
const handleMatch = () => {
    alert("¡Has hecho un match con este perfil!");
    currentProfileIndex++;
    loadProfile();
};

const handleReject = () => {
    alert("Has rechazado este perfil.");
    currentProfileIndex++;
    loadProfile();
};

// Cargar el primer perfil al inicio
loadProfile();
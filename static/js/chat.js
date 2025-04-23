const urlParams = new URLSearchParams(window.location.search);
const room = urlParams.get('room');
const nombreUsuario = urlParams.get('nombreUsuario');
const socket = io();

$('#room-name').text(room);

socket.emit('unirseSala', room, nombreUsuario);

socket.on('esperando', function (data) {
    $('#status-mensaje').text(data.mensaje);
});

socket.on('salaLista', function (data) {
    $('#status-mensaje').text(data.mensaje);
});

socket.on('recibirMensaje', function (data) {
    const mensajeClass = (data.usuario === nombreUsuario) ? 'mi-mensaje' : 'mensaje-otro';
    $('#mensajes').append(`<p class="${mensajeClass}"><strong>${data.usuario}:</strong> ${data.mensaje}</p>`);
});
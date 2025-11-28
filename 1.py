 This code should be in a .js file
window.MostrarModalDAAC = function(id) {
    idGiftUpdateDAAC = id;
    const indexDAAC = datosDAAC.findIndex((item) => item.id === id);
    const itemDAAC = datosDAAC[indexDAAC];
    document.getElementById('nombreInputDAAC').value = itemDAAC.nombre;
    document.getElementById('precioInputDAAC').value = itemDAAC.precio;
    document.getElementById('modalEditarDAAC').style.display = 'block';
};

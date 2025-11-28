window.MostrarModalDAAC = (id) => {
    idGiftUpdateDAAC = id;
    const indexDAAC = datosDAAC.findIndex((item) => item.id === id);
    document.querySelector("#gift-modalDAAC").value = datosDAAC[indexDAAC].gift;
    document.querySelector("#tipo-modalDAAC").value = datosDAAC[indexDAAC].tipo;
    document.querySelector("#tiempo-modalDAAC").value = datosDAAC[indexDAAC].tiempo;
    document.querySelector("#precio-modalDAAC").value = datosDAAC[indexDAAC].precio;
    document.querySelector("#imagen-modalDAAC").value = datosDAAC[indexDAAC].imagen;
    myModalDAAC.show();
};

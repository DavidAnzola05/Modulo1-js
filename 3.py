fetch('http://miservidor.com/api/giftsDAAC')
.then(response => response.json())
.then(datosDAAC => {
    renderizarTablaDAAC(datosDAAC);
})
.catch(error => console.error('Error:', error));

fetch('http://miservidor.com/api/giftsDAAC', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(nuevoGiftDAAC)
})
.then(response => response.json())
.then(dataDAAC => {
    console.log('Gift creado:', dataDAAC);
    cargarTablaDAAC();
});

fetch(`http://miservidor.com/api/giftsDAAC/${idDAAC}`, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(actualizarGiftDAAC)
})
.then(response => response.json())
.then(dataDAAC => {
    console.log('Gift actualizado:', dataDAAC);
    cargarTablaDAAC();
});

fetch(`http://miservidor.com/api/giftsDAAC/${idDAAC}`, {
    method: 'DELETE'
})
.then(response => response.json())
.then(dataDAAC => {
    console.log('Gift eliminado:', dataDAAC);
    cargarTablaDAAC();
});

const aplicacion = document.querySelector('.container-service')

const url = 'https://jsonplaceholder.typicode.com/users'

fetch(url)
    .then(res => res.json())
    .then(data => {
        data.forEach(usuario => {
            console.log(usuario.name)
            const p = document.createElement('p')
            p.innerHTML = usuario.name
            aplicacion.appendChild(p)
        });
    })
    .catch(err => console.log(err))
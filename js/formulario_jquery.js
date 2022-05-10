$("#formulario").validate({
    rules: {
        email: {
            required: true,
            email: true
        },
        password: {
            required: true
        },
        mensaje: {
            required: true,
            minlength: 5,
            maxlength: 200
        }
    }
})




$("#guardar").click(function() {

    if ($("#formulario").valid() == false) {
        return;
    }
    let email = $("#email").val()
    let password = $("#password").val()
    let mensaje = $("#mensaje").val()
    alert("registro creado con éxito")


})


$("#formulario2").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 5,
            maxlength: 200
        },
        apellido: {
            required: true,
            minlength: 5,
            maxlength: 200
        },
        usuario: {
            required: true,
            minlength: 5,
            maxlength: 200
        },
        pass: {
            required: true,
            minlength: 5,
            maxlength: 200
        },
        email: {
            required: true,
            email: true
        },
    }
})




$("#guardar2").click(function() {

    if ($("#formulario2").valid() == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let usuario = $("#usuario").val()
    let pass = $("#contrasenia").val()
    let email = $("#correo").val()
    alert("registro creado con éxito")


})
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
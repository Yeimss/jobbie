function registrarse() {
    this.CargaInicial = function () {
        registrarse.CargarDptos();
    };
    this.CargarDptos = function () {
            $.ajax({
                url: 'https://www.datos.gov.co/resource/xdk5-pm3f.json',
                type: "GET",
                dataType: "JSON",
                data: "",
                success: function (data) {
                    if (data.length != 0) {
                        let codigos=[];
                        $.each(data, function (i, dep) {

                            if(!codigos.includes(dep.c_digo_dane_del_departamento)){
                                codigos.push(dep.c_digo_dane_del_departamento);
                                $("<option value='" + dep.c_digo_dane_del_departamento + "'>" + dep.departamento + "</option>").appendTo("#departamento");
                            }
                        });
                    } else {
                        console.log("No se encontraron datos");
                    }
                }
        }); 
    };

    this.CargarMunicipios= function(depto){
        $("#municipios").empty();
        $.ajax({
            url: 'https://www.datos.gov.co/resource/xdk5-pm3f.json',
            type: "GET",
            dataType: "JSON",
            success: function (data) {
                    $.each(data, function (i, dep) {
                        if(dep.c_digo_dane_del_departamento==depto){
                            $("<option value='" + dep.c_digo_dane_del_municipio + "'>" + dep.municipio + "</option>").appendTo("#municipio");
                        }
                    });
            }
        });
    };
  }

var registrarse = new registrarse();

$(document).ready(function () {
    
    registrarse.CargarDptos();
    $('#departamento').on('change', function () {
        if (this.value !== "") {
            registrarse.CargarMunicipios(this.value);
        }
        $("#municipio").prop('disabled', false);
        $('#municipio').empty();
        objInformeCarteraAsignada.LimpiarSelectAgencias();
    });
    $("#password").blur(function () {
        if($("#password").val().length<8){
            $('#errorPassword').text("La contraseña debe tener por lo menos 8 caracteres");
            $("#btnRegistro").prop('disabled', true);
        }
        else{
            $("#btnRegistro").prop('disabled', false);
            $('#errorPassword').empty();

        }
    });
    $("#rePassword").blur(function () {
        if(($("#rePpassword").val()) != ($("#password").val())){
            $('#errorRePassword').text("Las contraseñas deben ser iguales");
            $("#btnRegistro").prop('disabled', true);
        }
        else{
            $('#errorRePassword').empty();
            $("#btnRegistro").prop('disabled', false);
        }
    });
    $("#correo").blur(function () {
        if($("#correo").val().includes("@") && $("#correo").val().includes(".")){
            $("#btnRegistro").prop('disabled', false);
            $('#errorCorreo').text("");
        }
        else{
            $('#errorCorreo').text("Por favor ingrese un correo valido");
            $("#btnRegistro").prop('disabled', true);
        }
    });
});
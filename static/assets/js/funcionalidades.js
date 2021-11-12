// Formatear fecha
function formatear_fecha(fecha) {
    año = fecha[0]
    dia = fecha[2]

    if(fecha[1] == 1){
        mes = "enero"
    }
    if(fecha[1] == 2){
        mes = "febrero"
    }
    if(fecha[1] == 3){
        mes = "marzo"
    }
    if(fecha[1] == 4){
        mes = "abril"
    }
    if(fecha[1] == 5){
        mes = "mayo"
    }
    if(fecha[1] == 6){
        mes = "julio"
    }
    if(fecha[1] == 7){
        mes = "junio"
    }
    if(fecha[1] == 8){
        mes = "agosto"
    }
    if(fecha[1] == 9){
        mes = "septiembre"
    }
    if(fecha[1] == 10){
        mes = "octubre"
    }
    if(fecha[1] == 11){
        mes = "noviembre"
    }
    if(fecha[1] == 12){
        mes = "diciembre"
    }

    return `${dia} de ${mes} de ${año}`

}
fecha_nacimiento = document.querySelector("#fechanacimiento").innerHTML.split('-')
fecha_formateada = formatear_fecha(fecha_nacimiento)
document.querySelector("#fechanacimiento").innerHTML = fecha_formateada
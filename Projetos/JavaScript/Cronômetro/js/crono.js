var sec = 0
var min = 0
var hor = 0
var interval 

/* ----- */
function twoDigits(digit){
    if (digit<10){
        return('0'+digit)
    } else {
        return(digit)
    }
}

function start(){
    console.log('Começou!')
    watch()
    interval = setInterval(watch, 1000)
}

function pause(){
    console.log('Pausou!')
    clearInterval(interval)
}

function restart(){
    window.alert('Reiniciou!')
    clearInterval(interval)
    sec=0
    min=0
    document.querySelector('.numeros').innerText ='00:00:00'
}

function watch(){
    sec ++
    if (sec == 60){
        min ++
        sec = 0
        if (min == 60){
            min = 0
            hor ++
        }
    }
    document.querySelector('.numeros').innerText =twoDigits(hor)+':'+twoDigits(min)+':'+twoDigits(sec)
}
document.querySelector('#check-box').addEventListener('click', () => {
    var body = document.querySelector('body')
    var labelInput = document.querySelector('.label-input')

    body.classList.toggle('darkmode')
    if(body.classList.contains('darkmode')){
        labelInput.innerText = 'Light Mode'
    }
    else{
        labelInput.innerText = 'Dark Mode'
    }
})
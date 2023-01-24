// ├── createBTN -> Seletor do <button> do formulário
// ├── tbodyTable -> Seletor do <tbody> da tabela
const createBTN = document.querySelector(".main_btn")
const tbodyTable = document.querySelector('.body-table')

function create_Note(task_id, note){
    /*
        ├── Salvando dados no localStorage.
        ├
        ├── Args:
            ├── task_id -> ID da lista;
            └── note -> Anotação do usuário.
    */
    localStorage.setItem(task_id, JSON.stringify(note))
    console.log('\033[1;32m [-][VALID] Inserido ao localStorage com sucesso! \033[m')
}

function delete_Note(task_id){
    /*
        ├── Deletando dados do localStorage.
        ├
        ├── Args:
            └── task_id -> ID da anotação.
        ├
        ├── Return:
            └── tr_line = Seletor da <tr> com o seu ID.
    */
   localStorage.removeItem(task_id)
   
   const tr_line = document.querySelector(`.tr_line${task_id}`)
   document.querySelector('.body-table').removeChild(tr_line)

   console.log('\033[1;35m [-][DELETE] Task deletada com sucesso! \033[m')
   console.log('\033[1;35m'+`    └── [DEL] -> [${task_id}]`+'\033[m')
}

function read_Note(){
    /*
        ├── Ler o contéudo do localStorage.
        ├
        ├── Return:
            ├── localStorage_set -> Pegar todos os dados [registrados] do localStorage
            ├── localStorage_keys -> ID's dos dados (keyItem)
            ├
            └── Variables:
                ├── task_id -> ID da anotação
                ├── jsonData -> Pegar o valor do localStorage pelo kyItem
                ├── obj_jsonData -> Retorna o objeto [ctd, qtd]
                ├
                ├── note -> Nota do localStorage [ctd]
                └── qtd_Select -> Quantidade do objeto localStorage [qtd]
    */

    const localStorage_set = {...localStorage}
    const localStorage_keys = Object.keys(localStorage_set)

    for(var c = 0; c<localStorage_keys.length;c++){
        const task_id = localStorage_keys[c]
        const jsonData = localStorage.getItem(task_id)
        const obj_jsonData = JSON.parse(jsonData)

        const note = obj_jsonData.ctd
        const qtd_Select = obj_jsonData.qtd

        newRoleTable(task_id, note, qtd_Select)
    }
    console.log('\033[1;34m [-][CHECK] Leitura do localStorage feita com sucesso! \033[m')
    console.log('\033[1;34m'+`    └── [READ] -> ${localStorage_set}`+'\033[m')
}

const newRoleTable = (task_id, note, qtd_Select) => {
    /*
        ├── Criar uma nova linha na tabela.
        ├
        ├── Args:
            ├── task_id -> ID selecionado pelo usuário;
            ├── note -> Anotação principal
            └── qtd_Select -> Quantidade
        ├
        ├── Return:
            ├── tbodyTable -> Seletor do <tbody> da tabela
            ├── content_TR -> Criar um elemento <tr>
                ├── content_TD_id -> Linhda do 'ID'
                ├── content_TD_note -> Linha de 'Anotção'
                ├── content_TD_qtd -> Linha de 'Quantidade'
                └── content_TD_button -> Linha do 'Botão'
                    ├── delete_button -> Botão
                    └── icon_trash -> Ícone de lixeira
    */

    const content_TR = document.createElement('tr')
    content_TR.classList.add(`tr_line${task_id}`)
    
    // ├── ID
    const content_TD_id = document.createElement('td')
    content_TD_id.textContent = task_id
    content_TR.appendChild(content_TD_id)

    // ├── Note
    const content_TD_note = document.createElement('td')
    content_TD_note.textContent = note
    content_TR.appendChild(content_TD_note)
    var click = 0

    content_TD_note.addEventListener('click', () => {
        if(click === 0){
            content_TD_note.style.color = "#32D94B"
            content_TD_note.style.textDecoration = "none"
            click = 1
        }
        else{
            content_TD_note.style.color = "#4D60EB"
            content_TD_note.style.textDecoration = "line-through"
            click = 0
        }
    })

    // ├── QTD
    const content_TD_qtd = document.createElement('td')
    content_TD_qtd.textContent = qtd_Select
    content_TR.appendChild(content_TD_qtd)

    // ├── Button
    const content_TD_button = document.createElement('td')

    const delete_button = document.createElement('button')
    const icon_trash = document.createElement('i')
    icon_trash.classList.add('bi')
    icon_trash.classList.add('bi-trash-fill')
    content_TR.appendChild(content_TD_button)
    content_TD_button.appendChild(delete_button)
    delete_button.appendChild(icon_trash)

    tbodyTable.appendChild(content_TR)

    delete_button.addEventListener('click', () => {
        delete_Note(task_id)
    })
}


createBTN.addEventListener('click', (e) => {
    /*
        ├── Função para adicionar conteúdo ao localStorage.
        ├
        ├── Return:
            ├── preventDefault() -> Impedir página de recarregar.
            ├── con_Select -> Valor da <textarea> (str)
            ├── taskID_Select -> Valor do <input type="text"> (str)
            └── qtd_Select -> Valor do <input type="number"> (int)
    */
    e.preventDefault()
    let con_Select = document.getElementById('i_conteudo').value
    let taskID_Select = document.querySelector('#i_taskID').value
    let qtd_Select = document.querySelector('#i_qtd')

    taskID_Select = taskID_Select.toLowerCase()

    if(con_Select === ""){
        window.alert("Preencha o campo de anotação.")
        console.log('\033[1;31m [-][INVALID] Não pode ser inserido... \033[m')

        // Colorir a borda da <textarea de vermelho>
        document.getElementById('i_conteudo').style.border = "1px solid red"

        // Alterar texto no botão
        createBTN.textContent = "Tente novamente"
    }

    else{
        if(parseInt(qtd_Select.value) === 0){
            qtd_Select = "Nenhuma quantidade"

            const noteContent_Dic = {
                "ctd": con_Select,
                "qtd": qtd_Select
            }

            create_Note(noteContent_Dic)
            newRoleTable(taskID_Select, con_Select, qtd_Select)
        }

        else{
            qtd_Select = parseInt(qtd_Select.value)
            
            const noteContent_Dic = {
                "ctd": con_Select,
                "qtd": qtd_Select
            }

            create_Note(taskID_Select, noteContent_Dic)
            newRoleTable(taskID_Select, con_Select, qtd_Select)

            // Alterar texto no botão
            createBTN.textContent = "Fazer anotação"
        }
    }
})


function testeRead(){
    const localStorage_set = {...localStorage}
    console.log(localStorage_set.teste)
}

// ====================
read_Note()
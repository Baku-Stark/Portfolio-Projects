const inputElement = document.querySelector('.new-task-input');
const addTaskElement = document.querySelector('.new-task-button');

const tasksContainer = document.querySelector('.tasks-container');

const validadeInput = () => {
    return inputElement.value.trim().length > 0;
};

const handleAddTask = () => {
    const inputIsValid = validadeInput();

    if(!inputIsValid) {
        window.alert('Nenhuma nota foi feita!');
        return inputElement.classList.add("error");
    }

    const taskItemContainer = document.createElement('div');
    taskItemContainer.classList.add('task-item');

    const taskContent = document.createElement('p');
    taskContent.innerText = inputElement.value;

    taskContent.addEventListener('click', () => 
        handleClick(taskContent)
    );

    const deleteItem = document.createElement('i');
    deleteItem.classList.add('fa-regular');
    deleteItem.classList.add('fa-trash-can');
    deleteItem.classList.add('delete-task-button');

    deleteItem.addEventListener('click', () => 
        handleDeleteClick(taskItemContainer, taskContent)
    );

    taskItemContainer.appendChild(taskContent);
    taskItemContainer.appendChild(deleteItem);

    tasksContainer.appendChild(taskItemContainer);

    inputElement.value == "";

    updateLocalStorage();
};

const handleClick = (taskContent) => {
    const tasks = tasksContainer.childNodes;

    for (const task of tasks) {
        if (task.firstChild.isSameNode(taskContent)) {
            task.firstChild.classList.toggle("completed");
        }
    }

    updateLocalStorage();
};

const handleDeleteClick = (taskItemContainer, taskContent) => {
    const tasks = tasksContainer.childNodes;

    for (const task of tasks) {
        const currentTaskIsBeingClicked = task.firstChild.isSameNode(taskContent);
        
        if (currentTaskIsBeingClicked) {
            taskItemContainer.remove();
        }
    }

    updateLocalStorage();
};


const handleInputChange = () => {
    const inputIsValid = validadeInput();

    if (inputIsValid) {
        return inputElement.classList.remove("error");
    }
};

const updateLocalStorage = () => {
    const tasks = tasksContainer.childNodes;

    const localStorageTasks = [ ... tasks].map(task => {
        const content = task.firstChild;
        const isCompleted = content.classList.contains('completed')

        return {description: content.innerText, isCompleted};
    });

    localStorage.setItem('tasks', JSON.stringify(localStorageTasks));
};

const refreshTasksUsingLocalStorage = () => {
    const tasksFromLocalStorage = JSON.parse(localStorage.getItem('tasks'));

    if(!tasksFromLocalStorage) return;
    
    for (const task of tasksFromLocalStorage) {
        const taskItemContainer = document.createElement('div');
        taskItemContainer.classList.add('task-item');

        const taskContent = document.createElement('p');
        taskContent.innerText = task.description;
        if (task.isCompleted) {
            taskContent.classList.add("completed");
        }

        taskContent.addEventListener('click', () => 
            handleClick(taskContent)
        );

        const deleteItem = document.createElement('i');
        deleteItem.classList.add('fa-regular');
        deleteItem.classList.add('fa-trash-can');
        deleteItem.classList.add('delete-task-button');

        deleteItem.addEventListener('click', () => 
            handleDeleteClick(taskItemContainer, taskContent)
        );

        taskItemContainer.appendChild(taskContent);
        taskItemContainer.appendChild(deleteItem);

        tasksContainer.appendChild(taskItemContainer);
    }
};

refreshTasksUsingLocalStorage();

addTaskElement.addEventListener('click', () => handleAddTask())

inputElement.addEventListener('change', () => handleInputChange())
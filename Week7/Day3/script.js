function fetchAndDisplayUsers(){
    fetch('http://localhost:3000/users')
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
        displayUsers(data)
    })
    .catch(error=>{
        console.error(`Error: ${error}`)
    })
}

function displayUsers(users){
    const userDataDiv=document.getElementById("userData")
    userDataDiv.innerHTML=''
    const userList=document.createElement('ul')

    users.forEach(user =>{
        const listItem=document.createElement('li')
        listItem.textContant=`ID: ${user.id}, Username: ${user.username}, Email: ${user.email}`
        userList.appendChild(listItem)
    })
    userDataDiv.appendChild(userList);
}
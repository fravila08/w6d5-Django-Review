console.log("hello!")

const createBook = (event) => {
    event.preventDefault();
    
    let title = document.getElementById("newTitle").value
    let description = document.getElementById("newDescription").value
    let price = document.getElementById("newPrice").value
    let author = document.getElementById("author").value
    let authorFirst = author.split(' ')[0]
    let authorLast = author.split(' ')[1]
    console.log(title,description, price, authorFirst, authorLast)

    axios.post("/books/",{
        title : title,
        description : description,
        price : price,
        first : authorFirst,
        last : authorLast,
    })
    .catch((err)=>{
        alert(err)
    })
    .then((response)=>{
        console.log(response)
        if(response.data.success){
            window.location.reload()
        }
    })
}

const updateBook = (event, id) => {
    event.preventDefault();

    let title = document.getElementById('title').value
    let firstName = document.getElementById('first').value
    let lastName = document.getElementById('last').value
    let description = document.getElementById('description').value
    let price = document.getElementById('price').value
    console.log(id, title, firstName, lastName, description, price)

    axios.put(`/book/${id}/`, {
        title : title,
        first_name : firstName,
        last_name : lastName,
        description : description,
        price : price
    })
    .catch((err)=>{
        alert(err)
    })
    .then((response)=>{
        console.log(response.data)
        if(response.data.success){
            window.location.reload()
        }
    })
}


const deleteBook = (id) =>{
    axios.delete(`/book/${id}/`)
    .catch((err)=>{
        alert(err)
    })
    .then((response)=>{
        console.log(response.data)
        if(response.data.success){
            window.location.reload()
        }
    })
}
//API request
fetch("https://jsonplaceholder.typicode.com/posts/1")
.then(resolve=>resolve.json())
.then(data=>{
    console.log("post Tittle :",data.title);
})
.catch(error=>{
    console.log("Error:",error)
});

//2nd programme
async function getUser(){
    try{
        const response = await fetch("https://jsonplaceholder.typicode.com/users/1")
        const data = await response.json();
        console.log("user name:",data.name);
    }catch(error){
        console.log("error:",error);
    }
}
getUser();
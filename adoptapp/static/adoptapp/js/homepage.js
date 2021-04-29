const testPost = [
    {
        info:"Perro encontrado en la calle" ,
        alt:"Perro corriendo",
        src: "media/dog.jpeg",
    },

]

presentation = document.getElementById("presentation") //creating a local variable to work with

/* function that adds posts to the homepage */
function addPost(n) {
    let petPost = document.createElement("div"); //create the div where everything goes
    petPost.setAttribute("class", "pet-post");
    petPost.setAttribute("onclick","");

    let petImg = document.createElement("img"); //create the image element for the post
    petImg.setAttribute("class","pet-img");
    petImg.setAttribute("src", "/static/users/"+testPost[n].src);
    petImg.setAttribute("alt", testPost[n].alt);

    let petInfo = document.createElement("div"); //create the div section for the information
    petInfo.setAttribute("class", "post-info");

    let text = document.createElement("p"); //create the section where the text will go
    text.setAttribute("id", "info-post " + n);

    //Creating the post's tree
    petInfo.appendChild(text);

    petPost.appendChild(petImg);
    petPost.appendChild(petInfo);

    //adding the nodes to the main node
    presentation.appendChild(petPost);

    //adding the text info to the text section
    document.getElementById("info-post " + n ).innerHTML += testPost[n].info;
}

//Adding all of the posts
for (let i = 0; i < testPost.length; i++) {
    addPost(i);
}


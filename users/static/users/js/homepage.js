const testPost = [
    {
        info:"Perro encontrado en la calle" ,
        alt:"Perro corriendo",
        src: "media/dog.jpeg",
    },

]

presentation = document.getElementById("presentation")

function addPost(n) {
    let petPost = document.createElement("div");
    petPost.setAttribute("class", "pet-post");
    petPost.setAttribute("onclick","");

    let petImg = document.createElement("img");
    petImg.setAttribute("class","pet-img");
    petImg.setAttribute("src", "/static/users/"+testPost[n].src);
    petImg.setAttribute("alt", testPost[n].alt);

    let petInfo = document.createElement("div");
    petInfo.setAttribute("class", "post-info");

    let text = document.createElement("p");
    text.setAttribute("id", "info-post" + n);

    petInfo.appendChild(text);

    petPost.appendChild(petImg);
    petPost.appendChild(petInfo);

    presentation.appendChild(petPost);
    document.getElementById("info-post" + n ).innerHTML += testPost[n].info;
}


for (let i = 0; i < testPost.length; i++) {
    addPost(i);
}


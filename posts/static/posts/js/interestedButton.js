const postId = document.getElementById('postId').value;
const userId = document.getElementById('userId').value;
const interestedButton = document.getElementById('interestedButton');
const alreadyInterestedButton = document.getElementById('alreadyInterestedButton');
const interestedMessage = document.getElementById('interestedMessage');
const notInterestedMessage = document.getElementById('notInterestedMessage');

/*
    We need to send the CSRF token cookie when doing AJAX with PUT or DELETE methods.
    See: https://docs.djangoproject.com/en/3.2/ref/csrf/#acquiring-the-token-if-csrf-use-sessions-and-csrf-cookie-httponly-are-false
 */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
const request = new Request(
    '/api/interested/' + userId + '/' + postId,
    {headers: {'X-CSRFToken': csrftoken}}
);

async function updateButton(updateText=false){
    let response = await fetch(request);
    if(response.ok) {
        alreadyInterestedButton.style.display = 'block';
        interestedButton.style.display = 'none';
        if(updateText){
            interestedMessage.style.display = 'block';
            notInterestedMessage.style.display = 'none';
        }
    }
    else {
        interestedButton.style.display = 'block';
        alreadyInterestedButton.style.display = 'none';
        if(updateText){
            interestedMessage.style.display = 'none';
            notInterestedMessage.style.display = 'block';
        }
    }
}

async function addInterest(){
    await fetch(request, {method: 'PUT', mode: 'same-origin'});
    await updateButton(true);
}

async function removeInterest(){
    await fetch(request, {method: 'DELETE'});
    await updateButton(true);
}

updateButton().then();
interestedButton.addEventListener('click', addInterest);
alreadyInterestedButton.addEventListener('click', removeInterest);

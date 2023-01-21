let likebtn = document.querySelector('#likebtn')
let dislikebtn = document.querySelector('#dislikebtn')
let likecount = document.querySelector('#likecount')
let dislikecount = document.querySelector('#dislikecount')

likebtn.addEventListener('click', () => {
    likecount.value = parseInt(likecount.value) + 1;
    likecount.style.color = "#12ff00";
})

dislikebtn.addEventListener('click', () => {
    dislikecount.value = parseInt(dislikecount.value) + 1;
    dislikecount.style.color = "#ff0000";
})
likebtn.addEventListener('click', () => {
    fetch('/vote/like/')
        .then(response => response.json())
        .then(data => {
            likecount.value = data.likes;
            likecount.style.color = "#12ff00";
        });
});

dislikebtn.addEventListener('click', () => {
    fetch('/vote/dislike/')
        .then(response => response.json())
        .then(data => {
            dislikecount.value = data.dislikes;
            dislikecount.style.color = "#ff0000";
        });
});
let myHeader = document.querySelector('.my-header');
let text = myHeader.innerHTML;
let textArray = text.split('');
let currentIndex = 0;
myHeader.innerHTML = '';
function typeWriter() {
    if (currentIndex < textArray.length) {
        myHeader.innerHTML += textArray[currentIndex];
        currentIndex++;
        setTimeout(typeWriter, 100);
    }
}

typeWriter();

function addComment(commentForm) {
    var commentList = commentForm.parentNode.parentNode;
    var newComment = document.createElement("li");
    var __ret = setUserNameComment();
    var userPic = __ret.userPic;
    var userName = __ret.userName;
    var comment = document.createElement("span");
    newComment.appendChild(userPic);
    newComment.appendChild(userName);
    commentBox = commentForm.firstElementChild.firstElementChild;
    comment.innerHTML = commentBox.value;
    commentBox.value = "";
    newComment.appendChild(comment);
    var commentText = commentForm.parentNode;
    commentList.removeChild(commentText);
    commentList.appendChild(newComment);
    commentList.appendChild(commentText);
    return false;
}

function setUserNameComment() {
    var userPic = document.createElement("img");
    var userName = document.createElement("a");
    userPic.src = "img/test/p2.jpg";
    userPic.className = "circular thumbnail_comment";
    userName.className = "username user_comment";
    userName.innerHTML = "John Smith";
    return {userPic: userPic, userName: userName};
}

function likeUnlike(like){
    if(like.innerHTML === "like"){
        like.innerHTML = "unlike"
    }else{
        like.innerHTML = "like"
    }
}
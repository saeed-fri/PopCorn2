function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function addComment(commentForm) {
    event.preventDefault();
    var commentBox = commentForm.firstElementChild.firstElementChild;
    var commentList = commentForm.parentNode.parentNode;
    var newComment = document.createElement("li");
    var __ret = setUserNameComment();
    var userPic = __ret.userPic;
    var userName = __ret.userName;
    var comment = document.createElement("span");
    newComment.appendChild(userPic);
    newComment.appendChild(userName);
    var commentValue = commentBox.value;
    comment.innerHTML = commentValue;
    commentBox.value = "";
    newComment.appendChild(comment);
    var commentText = commentForm.parentNode;
    //$.ajaxSetup({
    //    beforeSend: function(xhr, settings) {
    //        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //            xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //        }
    //    }
    //});
    var xhr = new XMLHttpRequest();
	xhr.open('get', '/comment/' + post_id + '/1/?text=' + decodeURI(commentValue)); //1 should be user id
    xhr.send(null);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                commentList.removeChild(commentText);
                commentList.appendChild(newComment);
                commentList.appendChild(commentText);
                var commentCount = document.getElementById('commentCount');
                commentCount.innerHTML = parseInt(commentCount.innerHTML) + 1;
            }
        }
    }
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
    var likes = document.getElementById('likeCount')
    if(like.innerHTML === "like"){
        var xhr = new XMLHttpRequest();
        xhr.open('get', '/like/' + post_id + '/1/'); //1 should be user id
        xhr.send(null);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    like.innerHTML = "unlike";
                    likes.innerHTML = parseInt(likes.innerHTML) + 1
                }
            }
        }
    }else{
        var xhr = new XMLHttpRequest();
        xhr.open('get', '/unlike/' + post_id + '/1/'); //1 should be user id
        xhr.send(null);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    like.innerHTML = "like";
                    likes.innerHTML = parseInt(likes.innerHTML) - 1
                }
            }
        }
    }
}
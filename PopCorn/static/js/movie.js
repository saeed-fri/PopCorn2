function calculate_rate(star) {
    var span_list = star.parentNode.getElementsByTagName("span");
    var rate = 10;
    for (var i = 0; i < span_list.length; i++) {
        if (span_list[i].isSameNode(star)) {
            rate -= i;
        }
    }
    return rate;
}
function rate(star){
    var rate = calculate_rate(star);
}

function edit_rate(star){
    var rate = calculate_rate(star);
    var rate_no = document.getElementById("user-rate-no");
    rate_no.innerHTML = rate + "/10";
    edit_modal(rate);
}

function edit_rate_out(star){
    var rate_no = document.getElementById("user-rate-no").innerHTML = "-/10";
}

function edit_stars(rate, stars) {
    var i = 0;
    var temp = rate / 2;
    if (rate % 2 == 1)
        temp -= 1;
    for (; i < temp; i++) {
        stars[i].className = "star star_full";
    }
    if (rate % 2 == 1) {
        stars[i].className = "star star_half";
        i++;
    }
    for (; i < 5; i++) {
        stars[i].className = "star star_empty";
    }
}
function edit_modal(rate){
    document.getElementById("rate-no").innerHTML = rate/2 + "/5";
    edit_stars(rate,document.getElementById("rating-stars").getElementsByClassName("star"));
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yy = today.getFullYear();
    if(dd<10) {
        dd='0'+dd
    }
    if(mm<10) {
        mm='0'+mm
    }
    today = dd + '-' + mm + '-' + yy;
    document.getElementById("post").getElementsByTagName("time")[0].innerHTML = today;
}


function post(){
    var text = document.getElementById('post_text').value;
    var rate = document.getElementById('rate-no').innerHTML.split('/')[0] * 2;
    var date = document.getElementById('post-date').innerHTML;
    console.log(decodeURI(text))
    var xhr = new XMLHttpRequest();
    xhr.open('get', '/addPost/' + user_id + '/' + movie_id + '/' + rate + '/?text=' + decodeURI(text));
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4) {
            if (xhr.status === 200) {
                $('#post').modal('hide');
            }
        }
    }
    xhr.send(null)
}
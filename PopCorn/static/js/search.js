function search(){
    event.preventDefault();
    var query = document.getElementById('search_input').value
    //alert(query)
    var xhr = new XMLHttpRequest();
	xhr.open('get', '/search_ajax/?q=' + query);
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4) {
            if (xhr.status === 200) {
                var movies = document.getElementById('movies')
                var jsonObj = JSON.parse(xhr.responseText)
                movies.innerHTML = ''
                for(key in jsonObj){
                    //debugger
                    var movie = jsonObj[key]

                    var firstDiv = document.createElement("div");
                    firstDiv.className = "search_movie_result col-md-4";
                    firstDiv.id = key;
                    var img = document.createElement("img");
                    //Console.log()
                    img.src = static_url + "img/posters/" + movie.id + ".jpg";
                    img.className = "col-md-6 search_movie_poster";
                    var secondDiv = document.createElement("div");
                    secondDiv.className = "col-md-6 search_movie_info";
                    var h4 = document.createElement("h4");
                    h4.innerHTML = movie.name;
                    secondDiv.appendChild(h4);
                    var rating = document.createElement("div");
                    rating.className = "rating";
                    var starSpans = [];
                    for(var i = 0; i < 5; i++){
                        starSpans[i] = document.createElement("span");
                        starSpans[i].className = "star";
                        starSpans[i].setAttribute("hidden", "hidden");
                        rating.appendChild(starSpans[i]);
                    }
                    var rateNumber = document.createElement("div");
                    rateNumber.className = "rating_number full_rate";
                    rateNumber.id = "r" + key.split('t')[1];
                    rateNumber.innerHTML = movie.rating_count + " " + movie.rating_sum;
                    rating.appendChild(rateNumber);
                    //rate(rating);
                    //stars
                                //<span class="star star_full"></span><span class="star star_full"></span><span class="star star_full"></span><span class="star star_full"></span><span class="star star_half"></span>
                                // <div class="rating_number full_rate">4.5/5</div>

                    secondDiv.appendChild(rating);
                    var fourthDiv = document.createElement("div");
                    fourthDiv.className = "search_movie_director"
                    var director = document.createElement("strong");
                    director.innerHTML = "Director:";
                    fourthDiv.appendChild(director);
                    fourthDiv.innerHTML += movie.director;
                    secondDiv.appendChild(fourthDiv);
                    firstDiv.appendChild(img);
                    firstDiv.appendChild(secondDiv);
                    movies.appendChild(firstDiv);
                }
            initialRate();
            }
        }
    }
    xhr.send(null)
}

function initialRate(){
    var movies = document.getElementById('movies');
    var children = movies.childNodes;
    for(var i = 0; i < children.length; i++){
        ch = children[i];
        if(ch.id !== undefined){
            var id = 'r'+ch.id.split('t')[1]
            var x = document.getElementById(id).innerHTML.split(' ');
            console.log("x : " + x)
            search_rate(id, x[0], x[1], ch.id);
        }
    }
}

function search_rate(id, count, sum, pid){
    console.log(id + ' ' + pid + ' ' + count)
    var rating = document.getElementById(id);
    var rate = 0;
    if(count != 0) {
        rate = Math.floor(sum / count);
        rating.innerHTML = rate + "/5.0"
    }
    else
    {
        rating.innerHTML = "no review";
        rating.style.color = 'gray';
    }
    edit_stars(rate, document.querySelectorAll('#' + pid + ' .rating>.star'));
    rating.removeAttribute('hidden');
    document.querySelector('#' + pid + ' .rating').removeAttribute('hidden');
}

function follow(btn){
    if(btn.innerHTML === "follow"){
        btn.innerHTML = "unfollow";
    } else{
        btn.innerHTML = "follow";
    }
}

function edit(btn){
    if(btn.innerHTML === "edit"){
        btn.innerHTML = "save";
        showEditForm();
    } else{
        btn.innerHTML = "edit";
        saveProfile();
        deleteElement("edit_form");
    }
}

function showProfilePicture(formE) {
    var group_form = document.createElement("div");
    group_form.className = "form-group";
    var picLabel = document.createElement("label");
    picLabel.innerHTML = "picture:";
    picLabel.setAttribute("for", "profile_pic");
    group_form.appendChild(picLabel);
    var picE = document.createElement("input");
    picE.id = "profile_pic";
    picE.className = "form-control";
    picE.type = "file";
    picE.accept = "image/*";
    group_form.appendChild(picE);
    formE.appendChild(group_form);
}
function showUserName(formE) {
    var group_form = document.createElement("div");
    group_form.className = "form-group";
    formE.appendChild(group_form);
    var nameE = document.createElement("input");
    nameE.value = "John Smith";
    nameE.className = "form-control";
    nameE.placeholder = "Username";
    group_form.appendChild(nameE);
    formE.appendChild(group_form);
}

function showLocation(formE) {
    var group_form = document.createElement("div");
    group_form.className = "form-group";
    formE.appendChild(group_form);
    var city = document.createElement("input");
    city.value = "Tehran";
    city.className = "form-control";
    city.id = "city";
    city.placeholder = "City";
    group_form.appendChild(city);

    var coma = document.createElement("span");
    coma.innerHTML = ",";
    coma.id = "coma";
    group_form.appendChild(coma);

    var country = document.createElement("input");
    country.value = "Iran";
    country.className = "form-control";
    country.id = "country";
    country.placeholder = "Country";
    group_form.appendChild(country);
    formE.appendChild(group_form);
}

function showEditForm(){
    var formE = document.createElement("form");
    formE.className = "navbar-form navbar-left edit-form";
    showUserName(formE);
    showProfilePicture(formE);
    showLocation(formE);

    document.getElementById("profile_details").appendChild(formE);
}

function deleteElement(idName){
    element = document.getElementById(idName);
    if(idName === "save"){
        saveProfile();
    }else if(element != null){
        element.parentNode.removeChild(element);
    }
}

function saveProfile(){
    window.location = window.location.href;
}
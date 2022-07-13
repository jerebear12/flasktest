var form = document.getElementById("images-form");
function handleForm(event) { 
    if( document.getElementById("picture").files.length == 0 ){
        event.preventDefault();
    }
}
form.addEventListener('submit', handleForm);


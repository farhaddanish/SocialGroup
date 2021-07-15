//     change password 




const form = document.getElementById('form_change')
const csr = form.firstElementChild.value

form.addEventListener('submit',(event)=>{
    event.preventDefault()
    const id_old = document.getElementById('id_old_password').value
    const id_new = document.getElementById('id_new_password1').value
    const id_new2= document.getElementById('id_new_password2').value
    const url  = document.location.href
  const urlProfile = 'http://127.0.0.1:8000/profiles'
    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken : csr,
            old_password : id_old,
            new_password1:id_new,
            new_password2 : id_new2
        },
        
        success: function (response) {
            if(response.type){
                alert(response.type)
            }else{
                alert(response.message)
                // const profile = document.getElementById('profile')
                // window.location.href  = urlProfile
   
            }
        },
        error: function(response){
            console.log(response)
        }
    });
    
})
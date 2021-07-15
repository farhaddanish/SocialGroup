const joinBtn = document.getElementById('join_btn')
const joinForm = document.querySelectorAll('.join_form')

joinForm.forEach((el)=>{
    el.addEventListener('submit',(event)=>{
        event.preventDefault()
        const id = el.getAttribute('data-join-id')
        const url = 'http://127.0.0.1:8000/Allgroups/' + 'join/'
        const csr = el.firstElementChild.value
        console.log(id)
        console.log(el)
        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken : csr,
                id :id
            },
            
            success: function (response) {
                const countMember = document.getElementById(`countMember${id}`)
                console.log(countMember)
                if(response.join){
                    el.querySelector('#join_btn').textContent="disJoin"
                    countMember.textContent =  `Member  :  ${response.count}`
                }else{
                    el.querySelector('#join_btn').textContent="Join"
                    countMember.textContent =  `Member  :  ${response.count}`
                    
                }
            }
        });
    } )
})

//    delete Btn


const delete_form =  document.querySelectorAll('.delete_form')

delete_form.forEach((el)=>{
    el.addEventListener('submit',(event)=>{
        event.preventDefault()
        const id= el.getAttribute('data-Delete-id')
        const url = 'http://127.0.0.1:8000/Allgroups/' + 'delete/'
        const csr = el.firstElementChild.value

        $.ajax({
            type: "POST",
            url: url,
            data: {
                csrfmiddlewaretoken : csr,
                id: id
            },
            success: function (response) {
                alert('deleted')
            },
            error : function (error) {  }
        });
    })
})





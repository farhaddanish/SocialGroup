// const image_form = document.getElementById('image_form')
// const imageFile = document.getElementById('imageFile')
// console.log(imageFile)
// const url = document.location.href
// image_form.addEventListener('submit',(event)=>{
//     event.preventDefault()
// const csr = image_form.firstElementChild.value

//     if (imageFile.value === ''){
//         alert('plz select image')

//     }else{
//         const data = new FormData()
//         data.append('file' , imageFile[0].files[0])
//         data.append('csrfmiddlewaretoken',csr)
//         console.log(data)
//         $.ajax({
//             type: "POST",
//             url: url,
//             processData  :false,
//             contentType :false,
//             mimeType : "multipart/form-data",
//             data :data,
//             // data : {
//             //     // csrfmiddlewaretoken : csr,
//             //     data : data
//             // },
        
//             success: function (response) {
//                 console.log(response.link)
//             }
//         });
//     }
// })






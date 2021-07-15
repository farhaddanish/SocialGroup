const form = document.querySelectorAll("#postDeletion");

form.forEach((el) => {
  el.addEventListener("submit", (event) => {
    event.preventDefault();
    const id = el.getAttribute("data-post");
    const url = "http://127.0.0.1:8000/delete/";
    const csr = el.firstElementChild.value;

    $.ajax({
      type: "POST",
      url: url,
      data: {
        csrfmiddlewaretoken: csr,
        id: id,
      },

      success: function (response) {
        alert("deleted");
      },
    });
  });
});

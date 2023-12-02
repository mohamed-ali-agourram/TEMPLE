const spinner = document.getElementById("spinner")
const content = document.querySelectorAll(".the_item")

$.ajax({
    type: 'GET',
    url: '/',
    success: function(response) {
        setTimeout(() => {
            spinner.classList.add("removelem")
            content.forEach((i) => {
                i.classList.remove("removelem")
            })
        }, 500)

    },
    error: function(response) {
        console.log(error)
    }
})
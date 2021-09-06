console.log('hello world')

const spinnerBox = document.getElementById('spinner-box')
const dataBox = document.getElementById('data-box')

// console.log(spinnerBox)
// console.log(dataBox)

$.ajax({
    type: 'GET',
    url: '',
    success: function(response){
        spinnerBox.classList.add('not-visible')
        console.log(response)
    },
    error: function(error){
        console.log(error)
    }
})

$("#get_all_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/get_all_result/",
        beforeSend: function(){
            spinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            spinnerBox.classList.add('not-visible')
        }
    })
})

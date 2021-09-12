const getAllSpinnerBox = document.getElementById('get_all_spinner')
const learnVLANSpinnerBox = document.getElementById('learn_vlan_spinner')
const learnVRFSpinnerBox = document.getElementById('learn_vrf_spinner')
const showInventorySpinnerBox = document.getElementById('show_inventory_spinner')
const showIPIntBriefSpinnerBox = document.getElementById('show_ip_int_brief_spinner')
const showVersionSpinnerBox = document.getElementById('show_version_spinner')

$("#get_all_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/get_all_result/",
        beforeSend: function(){
            getAllSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            getAllSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_vlan_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/learn_vlan_result/",
        beforeSend: function(){
            learnVLANSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnVLANSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_vrf_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/learn_vrf_result/",
        beforeSend: function(){
            learnVRFSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnVRFSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#show_inventory_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/show_inventory_result/",
        beforeSend: function(){
            showInventorySpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            showInventorySpinnerBox.classList.add('not-visible')
        }
    })
})

$("#show_ip_int_brief_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/show_ip_int_brief_result/",
        beforeSend: function(){
            showIPIntBriefSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            showIPIntBriefSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#show_version_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/show_version_result/",
        beforeSend: function(){
            showVersionSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            showVersionSpinnerBox.classList.add('not-visible')
        }
    })
})
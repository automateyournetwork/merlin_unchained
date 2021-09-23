const getAllSpinnerBox = document.getElementById('get_all_spinner')
const learnACLSpinnerBox = document.getElementById('learn_acl_spinner')
const learnARPSpinnerBox = document.getElementById('learn_arp_spinner')
const learnBGPSpinnerBox = document.getElementById('learn_bgp_spinner')
const learnConfigSpinnerBox = document.getElementById('learn_config_spinner')
const learnInterfaceSpinnerBox = document.getElementById('learn_interface_spinner')
const learnPlatformSpinnerBox = document.getElementById('learn_platform_spinner')
const learnVLANSpinnerBox = document.getElementById('learn_vlan_spinner')
const learnVRFSpinnerBox = document.getElementById('learn_vrf_spinner')
const showInventorySpinnerBox = document.getElementById('show_inventory_spinner')
const showIPIntBriefSpinnerBox = document.getElementById('show_ip_int_brief_spinner')
const showVersionSpinnerBox = document.getElementById('show_version_spinner')

$("#get_all_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/GetAll/get_all_all_result/",
        beforeSend: function(){
            getAllSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            getAllSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_acl_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnACL/learn_acl_all_result/",
        beforeSend: function(){
            learnACLSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnACLSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_arp_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnARP/learn_arp_all_result/",
        beforeSend: function(){
            learnARPSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnARPSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_bgp_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnBGP/learn_bgp_all_result/",
        beforeSend: function(){
            learnBGPSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnBGPSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_config_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnConfig/learn_config_all_result/",
        beforeSend: function(){
            learnConfigSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnConfigSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_interface_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnInterface/learn_interface_all_result/",
        beforeSend: function(){
            learnInterfaceSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnInterfaceSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_platform_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnPlatform/learn_platform_all_result/",
        beforeSend: function(){
            learnPlatformSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnPlatformSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_vlan_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnVLAN/learn_vlan_all_result/",
        beforeSend: function(){
            learnVLANSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnVLANSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#learn_vrf_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/LearnVRF/learn_vrf_all_result/",
        beforeSend: function(){
            learnVRFSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            learnVRFSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#show_inventory_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/ShowInventory/show_inventory_all_result/",
        beforeSend: function(){
            showInventorySpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            showInventorySpinnerBox.classList.add('not-visible')
        }
    })
})

$("#show_ip_int_brief_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/ShowIPInterfaceBrief/show_ip_int_brief_all_result/",
        beforeSend: function(){
            showIPIntBriefSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            showIPIntBriefSpinnerBox.classList.add('not-visible')
        }
    })
})

$("#show_version_all_devices_button").click(function(e){
    e.preventDefault();
    $.ajax({
        type: 'GET',
        url: "/OnDemand/ShowVersion/show_version_all_result/",
        beforeSend: function(){
            showVersionSpinnerBox.classList.remove('not-visible')
        },
        success: function(response){
            showVersionSpinnerBox.classList.add('not-visible')
        }
    })
})
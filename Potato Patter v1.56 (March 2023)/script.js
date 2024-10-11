//divs
let statsDiv = document.getElementById("statsDiv")
let potatoBtn = document.getElementById("potatoBtn")
let upgClickerBtn = document.getElementById("upgClickerBtn")
let idahoansBtn = document.getElementById("idahoansBtn")
let startupgIdahoansBtn = document.getElementById("startupgIdahoansBtn")
let upgIdahoansBtn = 0 //defined later
let farmers = document.getElementById("farmers")
let ttlClickedDiv = document.getElementById("ttlClickedDiv")
let ttlPotatoesDiv = document.getElementById("ttlPotatoesDiv")
let ttlPrestigesDiv = document.getElementById("ttlPrestigesDiv")
let prestigeBtn = document.getElementById("prestigeBtn")
let prestigeImg = document.getElementById("prestigeImg")

let clickerCostDiv = document.getElementById("clickerCostDiv")
let idahoanCostDiv = document.getElementById("idahoanCostDiv")
let prestigeCostDiv = document.getElementById("prestigeCostDiv")

//buttons
potatoBtn.addEventListener("click" , potatoClicked)
upgClickerBtn.addEventListener("click", upgClicker)
idahoansBtn.addEventListener("click", purcahseIdahoan)
prestigeBtn.addEventListener("click", purchasePrestige)
//upgrade idahoans btn is in showidahoans function


//upgrade costs + auto clickers + auto clicker costs variables
let upg1Cost = 25
let amtUpgrade1 = 0
let idahoans = 0
let idahoansCost = 25
let hasIdahoans = false
let idMultiplier = 1
let idahoansUpgCost = 100
let prestigeAmount = 1
let prestigeCost = 1000
let amtIdahoanUpg = 0

//main variables
let totalClicks = 0
let totalPotatoes = 0
let potatoes = 0
let multiplier = 1
let pps = 0 

//load data
function loadSave(){
    if (localStorage.getItem('potatoesSave')){
        potatoes = Number(localStorage.getItem('potatoesSave'))
    }
    if (localStorage.getItem('amtUpgrade1Save')){
        amtUpgrade1 = Number(localStorage.getItem('amtUpgrade1Save'))
    }
    if (localStorage.getItem('totalPotatoesSave')){
        totalPotatoes = Number(localStorage.getItem('totalPotatoesSave'))
    }
    if (localStorage.getItem('totalClicksSave')){
        totalClicks = Number(localStorage.getItem('totalClicksSave'))
    }
    if (localStorage.getItem('idahoansSave')){
        idahoans = Number(localStorage.getItem('idahoansSave'))
        if (idahoans>0){
            showIdahoansUpg()
        }
    }
    if (localStorage.getItem('idMultiplierSave')){
        idMultiplier = Number(localStorage.getItem('idMultiplierSave'))
    }
    if (localStorage.getItem('amtIdahoanUpgSave')){
        totalClicks = Number(localStorage.getItem('amtIdahoanUpgSave'))
    }
    if (localStorage.getItem('prestigeAmountSave')){
        prestigeAmount = Number(localStorage.getItem('prestigeAmountSave'))
    }
    if (localStorage.getItem('prestigeCostSave')){
        prestigeCost = Number(localStorage.getItem('prestigeCostSave'))
    }

}


function devMode(){
    setInterval(function(){
        potatoes = prestigeCost ** 999
        purchaseIdahoanUpg()
        purcahseIdahoan()
        upgClicker()
    },100)
}

//big potato clicked
function potatoClicked(){
    totalClicks = totalClicks + 1
    ttlClickedDiv.innerHTML = ("<strong>"+totalClicks+"</strong>")
    totalPotatoes = totalPotatoes + multiplier*(prestigeAmount)
    ttlPotatoesDiv.innerHTML = ("<strong>"+totalPotatoes+"</strong>")
    potatoes = potatoes + multiplier*(prestigeAmount)
    displayPotatoes()

}

//upgrade clicker
function upgClicker(){
    if (potatoes >= upg1Cost){
        amtUpgrade1 = amtUpgrade1 + 1
        multiplier = 1*1.2**amtUpgrade1
        potatoes = potatoes - upg1Cost
        displayPotatoes()
        upg1Cost = Math.floor(25*1.35**amtUpgrade1+0.99)
        clickerCostDiv.innerHTML = ('<p class="transactionWorked">Upgrade Clicker</p><p class="transactionWorked">'+ upg1Cost +' potatoes</p>')
        setTimeout(function(){
            clickerCostDiv.innerHTML = ('<p>Upgrade Clicker</p><p>'+ upg1Cost +' potatoes</p>')
        }, 1000)
    }
    else{
        clickerCostDiv.innerHTML = ('<p class="transactionFailed">Upgrade Clicker</p><p class="transactionFailed">'+ upg1Cost +' potatoes</p>')
        setTimeout(function(){
            clickerCostDiv.innerHTML = ('<p>Upgrade Clicker</p><p>'+ upg1Cost +' potatoes</p>')
        }, 1000)
    }
}

//on purchasing idahoan
function purcahseIdahoan(){
    if (potatoes >= idahoansCost){
        potatoes = potatoes - idahoansCost
        idahoans = idahoans + 1
        addFarmer(1)
        showIdahoansUpg()
        idahoansCost = 25*1.25**idahoans
        idahoanCostDiv.innerHTML = ('<p class="transactionWorked">Hire an Idahoan</p><p class="transactionWorked">'+ Math.floor(idahoansCost+0.99) +' potatoes</p>')
        setTimeout(function(){
            idahoanCostDiv.innerHTML = ('<p>Hire an Idahoan</p><p>'+Math.floor(idahoansCost+0.99)+' potatoes</p>')
        }, 1000)
        definePPS()
        displayPotatoes()
    }
    else {
        idahoanCostDiv.innerHTML = ('<p class="transactionFailed">Hire an Idahoan</p><p class="transactionFailed">'+Math.floor(idahoansCost+0.99)+' potatoes</p>')
        setTimeout(function(){
            idahoanCostDiv.innerHTML = ('<p>Hire an Idahoan</p><p>'+Math.floor(idahoansCost+0.99)+' potatoes</p>')
        }, 1000)
    }
}

//on purchasing idahoan upgrade
function purchaseIdahoanUpg(){
    if (potatoes >= idahoansUpgCost){
        potatoes = potatoes - idahoansUpgCost
        idMultiplier = idMultiplier*1.5
        amtIdahoanUpg++
        idahoansUpgCost = 100*1.3**amtIdahoanUpg
        upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p class="transactionWorked"><strong>Upgrade Idahoans</strong></p><p class="transactionWorked"><strong>'+ Math.floor(idahoansUpgCost+0.99) +' potatoes</strong></p></div>')
        setTimeout(function(){
            upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+ Math.floor(idahoansUpgCost+0.99) +' potatoes</strong></p>')
        }, 1000)
        definePPS()
        displayPotatoes()
    }
    else {
        upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p class="transactionFailed"><strong>Upgrade Idahoans</strong></p><p class="transactionFailed"><strong>'+ Math.floor(idahoansUpgCost+0.99) +' potatoes</strong></p></div>')
        setTimeout(function(){
            upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+ Math.floor(idahoansUpgCost+0.99) +' potatoes</strong></p>')
        }, 1000)
    }
}

function purchasePrestige(){
    if (potatoes >= prestigeCost){
        potatoes = 0
        idMultiplier = 1
        idahoansUpgCost = 100
        amtIdahoanUpg = 0
        upgIdahoansBtn.innerHTML = ('<img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+ Math.floor(idahoansUpgCost+0.99) +' potatoes</strong></p></div>')
        idahoans = 0 
        hasIdahoans = false
        idahoansCost = 25
        idahoanCostDiv.innerHTML = ('<p>Hire an Idahoan</p><p>'+Math.floor(idahoansCost+0.99)+' potatoes</p>')
        multiplier = 1
        upg1Cost = 25
        amtUpgrade1 = 0
        clickerCostDiv.innerHTML = ('<p>Upgrade Clicker</p><p>'+ upg1Cost +' potatoes</p>')
        farmers.innerHTML = ("")
        prestigeAmount ++
        prestigeCost=((prestigeAmount**prestigeAmount) )*1000 + prestigeCost
        if (prestigeAmount<12){
            prestigeImg.innerHTML = ('<img class="scrollGroup2" src="images/prestigeIcons/'+ prestigeAmount +'.png" >')
        }
        else{
            prestigeImg.innerHTML = ('<img class="scrollGroup2" src="images/prestigeIcons/'+ 12 +'.png" >')
        }
        ttlPrestigesDiv.innerHTML = ("<strong>"+(prestigeAmount-1)+"</strong>")
        prestigeCostDiv.innerHTML = ('<p>'+Math.floor(prestigeCost+0.99)+' potatoes</p>')
        definePPS()
        displayPotatoes()

        prestigeCostDiv.innerHTML = ('<p class="transactionWorked">'+Math.floor(prestigeCost+0.99)+' potatoes</p>')
        setTimeout(function(){
            prestigeCostDiv.innerHTML = ('<p>'+Math.floor(prestigeCost+0.99)+' potatoes</p>')
        }, 1000)
        definePPS()
        displayPotatoes()
    }
    else{
        prestigeCostDiv.innerHTML = ('<p class="transactionFailed">'+Math.floor(prestigeCost+0.99)+' potatoes</p>')
        setTimeout(function(){
            prestigeCostDiv.innerHTML = ('<p>'+Math.floor(prestigeCost+0.99)+' potatoes</p>')
        }, 1000)
    }
}

//display potatoes amount
function displayPotatoes(){
    if (potatoes < 1000){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p><strong>"+ (Math.floor(100*potatoes)/100).toLocaleString("en-US") +" potatoes</strong></p><p><strong>per second: "+ Math.floor(100*pps)/100 +"</strong></p>")
    }
    else if (potatoes < 100000){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: green; text-shadow: green 1px 0px 10px'><strong>"+ (Math.floor(100*potatoes)/100).toLocaleString("en-US") +" potatoes</strong></p><p style='color: green; text-shadow: green 1px 0px 10px'><strong>per second: "+ (Math.floor(100*pps)/100).toLocaleString("en-US") +"</strong></p>")
    }
    else if (potatoes < 99999999999){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: blue; text-shadow: blue 1px 0px 10px'><strong>"+ (Math.floor(100*potatoes)/100).toLocaleString("en-US") +" potatoes</strong></p><p style='color: blue; text-shadow: blue 1px 0px 10px'><strong>per second: "+ (Math.floor(100*pps)/100).toLocaleString("en-US") +"</strong></p>")
    }
    else if (potatoes < 99999999999999999999999999999999999999999999999999999999999999999999999){
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: orange; text-shadow: orange 1px 0px 10px'><strong>"+ (Math.floor(100*potatoes)/100).toLocaleString("en-US") +" potatoes</strong></p><p style='color: orange; text-shadow: orange 1px 0px 10px'><strong>per second: "+ (Math.floor(100*pps)/100).toLocaleString("en-US") +"</strong></p>")
    }
    else{
        statsDiv.innerHTML = statsDiv.innerHTML = ("<p style='color: red; text-shadow: red 1px 0px 10px'><strong>"+ (Math.floor(100*potatoes)/100).toLocaleString("en-US") +" potatoes</strong></p><p style='color: red; text-shadow: red 1px 0px 10px'><strong>per second: "+ (Math.floor(100*pps)/100).toLocaleString("en-US") +"</strong></p>")
    }
}

//update pps
function definePPS(){
    pps = (idahoans*idMultiplier*.1)*(prestigeAmount)
}

//show idahoans upgrade
function showIdahoansUpg(){
    if (hasIdahoans == false){
        idahoansUpgCost = 100*1.15**idahoans
        startupgIdahoansBtn.innerHTML = ('<button type="button" id="upgIdahoansBtn" class="storeBtn"><img class="scrollGroup" src="images/upgidahoan.png" ><p><strong>Upgrade Idahoans</strong></p><p><strong>'+Math.floor(idahoansUpgCost+0.99)+' potatoes</strong></p></button></div>')
        upgIdahoansBtn = document.getElementById("upgIdahoansBtn")
        upgIdahoansBtn.addEventListener("click", purchaseIdahoanUpg)
        hasIdahoans = true
    }
}

//run auto clicker
setInterval(function(){
    totalPotatoes = totalPotatoes + pps*0.25
    potatoes = potatoes + pps*0.25 //change based on how often you refresh
    displayPotatoes()
    ttlPotatoesDiv.innerHTML = ("<strong>"+totalPotatoes+"</strong>")
}, 250)//refresh every quarter second


//add a farmer to screen
let randValue = 0
function addFarmer(x){
    if (x>0){
        
        randValue = Math.random()
        if (idMultiplier <= 15){
            if (randValue > 0.5){
                farmers.innerHTML += "<img src='images/idahoan.png'  style='position:absolute; top:"+ (75*Math.random() +20)  +"%;left:"+ 70*Math.random() +"%;width: 70px; opacity: "+(30*Math.random()+50)+"%; transform: scaleX(-1); transform: rotate("+ 360*Math.random() +"deg)'>"
            }
            else{
                farmers.innerHTML += "<img src='images/idahoan.png'  style='position:absolute; top:"+ (75*Math.random() +20)  +"%;left:"+ 70*Math.random() +"%;width: 70px; opacity: "+(30*Math.random()+50)+"%; transform: rotate("+ 360*Math.random() +"deg)'>"
            }
        }
        else{
            if (randValue > 0.5){
                farmers.innerHTML += "<img src='images/upgidahoan.png' style='position:absolute; top:"+ (75*Math.random() +20)  +"%;left:"+ 70*Math.random() +"%;width: 70px; opacity: "+(30*Math.random()+50)+"%; transform: scaleX(-1); transform: rotate("+ 360*Math.random() +"deg)'>"
            }
            else{
                farmers.innerHTML += "<img src='images/upgidahoan.png' style='position:absolute; top:"+ (75*Math.random() +20)  +"%;left:"+ 70*Math.random() +"%;width: 70px; opacity: "+(30*Math.random()+50)+"%; transform: rotate("+ 360*Math.random() +"deg)'>"
            }
        }
    }
}


function createSave(){

    localStorage.setItem('potatoesSave' , potatoes)
    localStorage.setItem('amtUpgrade1Save' , amtUpgrade1)
    localStorage.setItem('totalPotatoesSave', totalPotatoes)
    localStorage.setItem('totalClicksSave' , totalClicks)
    localStorage.setItem('idahoansSave' , idahoans)
    localStorage.setItem('idMultiplierSave' , idMultiplier)
    localStorage.setItem('amtIdahoanUpg', amtIdahoanUpg)
    localStorage.setItem('prestigeAmountSave' , prestigeAmount)
    localStorage.setItem('prestigeCostSave', prestigeCost) 

    console.log('save file created')
}

setInterval(createSave,5000)


//things that need to happen at start
function start(){
    loadSave()
    
    upg1Cost = Math.floor(25*1.35**amtUpgrade1+0.99)
    idahoansCost = 25*1.25**idahoans
    multiplier = 1*1.2**amtUpgrade1
    idahoansUpgCost = 100*1.3**amtIdahoanUpg

    clickerCostDiv.innerHTML = ('<p>Upgrade Clicker</p><p>'+ upg1Cost +' potatoes</p>')
    idahoanCostDiv.innerHTML = ('<p>Hire an Idahoan</p><p>'+Math.floor(idahoansCost+0.99)+' potatoes</p>')
    prestigeCostDiv.innerHTML = ('<p>'+Math.floor(prestigeCost+0.99)+' potatoes</p>')
    ttlClickedDiv.innerHTML = ("<strong>"+totalClicks+"</strong>")
    ttlPrestigesDiv.innerHTML = ("<strong>"+(prestigeAmount-1)+"</strong>")

    console.log(idahoans)
    addFarmer(idahoans)
    definePPS()
}

start()
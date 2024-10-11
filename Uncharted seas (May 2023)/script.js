//get elements
let boat = document.getElementById('boat')
let infection = document.getElementById('infection')
let woman = document.getElementById('woman')
let revolt = document.getElementById('revolt')
let fog = document.getElementById('fog')
let mysteryBoat = document.getElementById('mystery')
let island = document.getElementById('island')
let shortcuts = document.getElementById('shortcuts')
let pirate = document.getElementById('pirates')
let captain = document.getElementById('captain')
let box = document.getElementById('box')
let background = document.getElementById('background')
let storm = document.getElementById('storm')
let sharkBackground = document.getElementById('sharkBackground')
let hungry = document.getElementById('hungry')
let option1 = document.getElementById('option1')
let option2 = document.getElementById('option2')
let startBtn = document.getElementById('startBtn')
let startBtnImg = document.getElementById('startBtnImg')
let title1 = document.getElementById('title1')
let stats = document.getElementById('stats')
let eventMsg = document.getElementById('eventMsg')
let eventItems = document.getElementById('eventItems')


//variables
let boatHealth = 100
let food = 100
let crew = 8
let supplies = 300
let rounds = 21
let map = false
let inPosition = true
let gameOver = false
let firstRound = true
let transition = false

let prevBoatHealth = boatHealth
let prevFood = food
let prevCrew = crew
let prevSupplies = supplies
let prevRounds = rounds

let opentheme = new Audio('blueWaters.mp3')

let sinkingShip = false
let starvation = false
let lackOfCrew = false
let scurvy = false
let lBaby = false
let sharks = false
let pirates = false
let stormy = false //storm
let mystery = false //ss curiosity
let curse = false //mysterious island
let shortNot = false //shortcut
let badCap = false

var deathMsg = 0

function playMusic() {
    let audio = new Audio("blueWaters.mp3")
    audio.play()
    audio.loop = true
}


// Randomly select an event
let randomEvent = 0
let randomSupplies = Math.floor(Math.random() * 2) +1

  function enableRevolt() {
    boat.style.backgroundImage = "url('images/Revolt.png')";
  }
  function disableRevolt() {
    boat.style.backgroundImage = "url('images/boat.png')";
  }
  function enableWoman() {
    boat.style.backgroundImage = "url('images/Woman.png')";
  }
  function disableWoman() {
    boat.style.backgroundImage = "url('images/boat.png')";
  }
  function enableInfection() {
    boat.style.backgroundImage = "url('images/Infection.png')";
  }
  function disableInfection() {
    boat.style.backgroundImage = "url('images/boat.png')";
  }
  function enableStorm() {
    storm.style.display = "block";
    console.log('oh no')
  }
  function disableStorm() {
    storm.style.display = "none";
  }
  function enableHungry() {
    hungry.style.display = "block";
  }
  function disableHungry() {
    hungry.style.display = "none";
  }
  function enableSharkBackground() {
    sharkBackground.style.display = "block";
  }
  function disableSharkBackground() {
    sharkBackground.style.display = "none";
  }
  function enablePirateBackground() {
    pirate.style.display = "block";
  }
  function disablePirateBackground() {
    pirate.style.display = "none";
  }
  function enableCaptainBackground() {
    captain.style.display = "block";
  }
  function disableCaptainBackground() {
    captain.style.display = "none";
  }
  function enableBoxBackground() {
    box.style.display = "block";
  }
  function disableBoxBackground() {
    box.style.display = "none";
  }
  function enableFogBackground() {
    fog.style.display = "block";
  }
  function disableFogBackground() {
    fog.style.display = "none";
  }
  function enableMysteryBoat() {
    mysteryBoat.style.display = "block";
  }
  function disableMysteryBoat() {
    mysteryBoat.style.display = "none";
  }
  function enableIsland() {
    island.style.display = "block";
  }
  function disableIsland() {
    island.style.display = "none";
  }
  function enableShortcut() {
    shortcuts.style.display = "block";
    console.log("arg")
  }
  function disableShortcut() {
    shortcuts.style.display = "none";
    console.log('why')
  }
//when option1 is clicked
option1.addEventListener('click', function(){
    if (gameOver==false || transition==true){
        if (firstRound==true){
            food=food+40
            firstRound=false
            newEvent()
        }
        else{
            if (randomEvent.name == ('Sharks surround and prepare to attack your boat, what do you do')){
                if (randomSupplies===1){
                    crew -= Math.floor(3*Math.random())
                    boatHealth = boatHealth - 15
                }
                sharks=true
               
                newEvent()
            }
            if (randomEvent.name == ('Pirates are closing in on your boat ready to attack, what do you do')){
                supplies = supplies - 30
                pirates=true;
                
                newEvent();
                
            }
            if (randomEvent.name == ('2 members of your crew are infected with scurvy, what do you do with them')){
                crew = crew - 2
                scurvy = true
                newEvent()
            }
            if (randomEvent.name == ('You find a questionable boat stranded at sea, what do you do')){
                if(randomSupplies===1){
                    supplies-=20;
                }
                else{
                    food-=10
                }
                mystery = true
                newEvent()
            }
            if (randomEvent.name == ('You find a captain who offers to sell you a map, what do you do?')){
                supplies-=30;
                map=true
                badCap = true
                newEvent()
            }
            if (randomEvent.name == ('You find a shortcut that might save time, or not, what do you do')){
                newEvent()
                shortNot = true
            }
            if (randomEvent.name == ('Your crew is caught in a fog, you could risk saving time, but you might lose time')){
                rounds+=3
                newEvent()
            }
            if (randomEvent.name == ('You run into a mysterious island')){
                if (map==true){
                    supplies += 20
                    food += crew*2
                    rounds++
                }
                else{
                    if (randomSupplies === 1){
                        supplies += 20
                        food += crew*2
                        rounds++
                    }
                    else{
                        supplies-= 30
                        food-=crew
                    }
                }
                curse = true
                newEvent()
            }
            if (randomEvent.name == ('Your crew finds a suspicious shipment of supplies floating in the ocean, a crew member thanks the Goddess of Fortune Zaena')){
                supplies = supplies + 100
                newEvent()
            }
            if (randomEvent.name == ('Your ship is caught in a storm, how do you recover')){
                if (randomSupplies===1){
                    //blessed by eltia
                    food+=20
                    supplies+=20
                }
                else{
                    //prayers left unanswered
                    rounds+=2
                    food-=crew
                    supplies-=20
                    boatHealth-=20
                }
                newEvent()
            }
            if (randomEvent.name == ('A woman on the ship suddenly goes into labor, what do you do')){
                crew = crew + 1
                lBaby = true
                newEvent()
            }
            if (randomEvent.name == ('Your crew revolts against you, what do you try')){
                if(randomSupplies===1){
                    crew-=2;
                }
                else{
                    crew-=4
                }
                lackOfCrew = true
                newEvent()
            }
            if (randomEvent.name == ('Your crew is feeling a little hungry and wants to stop and fish')){
                food+= Math.floor(crew*6*Math.random())
                rounds+=2
                newEvent()
            }
        }
    }
})

//when option2 is clicked
option2.addEventListener('click', function(){
    if (gameOver==false || transition == true){
        if (firstRound==true){
            boatHealth=boatHealth+30
            firstRound=false
            newEvent()
        }
        else{
            if (randomEvent.name == ('Sharks surround and prepare to attack your boat, what do you do')){
                if (randomSupplies === 1){
                    supplies = supplies - 10
                    boatHealth = boatHealth - 20
                }
                else {
                    boatHealth-=5
                }
                food+= crew*2
                sharks = true
                
                newEvent()
            }
            if (randomEvent.name == ('Pirates are closing in on your boat ready to attack, what do you do')){
                if(randomSupplies===1){
                    supplies-=20;
                    boatHealth-=25
                    crew = Math.floor(crew/2)
                }
                else{
                    supplies+=20
                    boatHealth-=10
                    food += crew*2
                }
                pirates = true
                
                newEvent()
            }
            if (randomEvent.name == ('2 members of your crew are infected with scurvy, what do you do with them')){
                food=food-crew
                if (randomSupplies===1){
                }
                else{
                    crew=crew-3
                }
                scurvy = true
                newEvent()
            }
            if (randomEvent.name == ('You find a questionable boat stranded at sea, what do you do')){
                if(randomSupplies===1){
                    supplies-=30;
                    crew= crew - 1
                }
                else{
                    supplies+=20
                }
                mystery = true
                newEvent()
            }
            if (randomEvent.name == ('You find a captain who offers to sell you a map, what do you do?')){
                badCap = true
                newEvent()
            }
            if (randomEvent.name == ('You find a shortcut that might save time, or not, what do you do')){
                if (map==true){
                    rounds-=3;
                }
                else{
                    if(randomSupplies===1){
                        rounds+=1;
                        boatHealth-=25
                    }
                    else{
                    rounds-=3
                    }
                }
                newEvent()
            }
            if (randomEvent.name == ('Your crew is caught in a fog, you could risk saving time, but you might lose time')){
                rounds+=3
                newEvent()
            }
            if (randomEvent.name == ('You run into a mysterious island')){
                rounds+=2
                curse = true
                newEvent()
            }
            if (randomEvent.name == ('Your crew finds a suspicious shipment of supplies floating in the ocean, a crew member thanks the Goddess of Fortune Zaena')){
                newEvent()
            }
            if (randomEvent.name == ('Your ship is caught in a storm, how do you recover')){
                if (randomSupplies === 1){
                    crew-=2
                    boatHealth= boatHealth-20
                }
                else{
                    supplies-=20
                    rounds-=2
                }
                stormy = true
                newEvent()
            }
            if (randomEvent.name == ('A woman on the ship suddenly goes into labor, what do you do')){
                crew-=1
                lBaby = true
                newEvent()
            }
            if (randomEvent.name == ('Your crew revolts against you, what do you try')){
                supplies = supplies - 20
                lackOfCrew = true
                newEvent()
            }
            if (randomEvent.name == ('Your crew is feeling a little hungry and wants to stop and fish')){
                newEvent()
            }
        }
        }
})

//when start is clicked
startBtn.addEventListener('click', function(){
    startGame()
})

//when window is resized, resizes the elements
window.addEventListener('resize', setSize)
function setSize(){

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    background.style.height = window.innerHeight + "px"
    background.style.width = window.innerWidth + "px"
    background.style.top = 0
    background.style.left = 0
    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    storm.style.height = window.innerHeight + "px"
    storm.style.width = window.innerWidth + "px"
    storm.style.top = 0
    storm.style.left = 0

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    sharkBackground.style.height = window.innerHeight + "px"
    sharkBackground.style.width = window.innerWidth + "px"
    sharkBackground.style.top = 0
    sharkBackground.style.left = 0

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    hungry.style.height = window.innerHeight + "px"
    hungry.style.width = window.innerWidth + "px"
    hungry.style.top = 0
    hungry.style.left = 0

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    mysteryBoat.style.height = window.innerHeight/2 + "px"
    mysteryBoat.style.width = window.innerWidth + "px"
    mysteryBoat.style.backgroundPositionY = 0
    mysteryBoat.style.left = 0  
    
    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    island.style.height = window.innerHeight/2 + "px"
    island.style.width = window.innerWidth + "px"
    island.style.backgroundPositionY = 0
    island.style.left = 0    

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    shortcuts.style.height = window.innerHeight/4 + "px"
    shortcuts.style.width = window.innerWidth + "px"
    shortcuts.style.backgroundPositionY = 0
    shortcuts.style.left = 0    

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    fog.style.height = window.innerWidth + "px"
    fog.style.width = window.innerWidth + "px"
    fog.style.top = 0
    fog.style.left = 0

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    pirate.style.height = window.innerHeight + "px"
    pirate.style.width = window.innerWidth + "px"
    pirate.style.backgroundPositionY = 0
    pirate.style.left = 0

    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    captain.style.height = window.innerHeight/4.3 + "px"
    captain.style.width = window.innerWidth + "px"
    captain.style.backgroundPositionY = 0
    captain.style.left = 0    
    
    //making sure background fits, NEEDS TO BE FIRST ON THIS FUNCTION
    box.style.height = window.innerHeight/4.3 + "px"
    box.style.width = window.innerWidth + "px"
    box.style.backgroundPositionY = 0
    box.style.left = 0   

    if(window.innerHeight>window.innerWidth){
        boat.style.width = window.innerWidth/7 + "px"
        boat.style.height = boat.style.width
    }
    else{
       boat.style.height = window.innerHeight/7 + "px"
       boat.style.width = boat.style.height 
    }
    
    if(inPosition==true){
        boat.style.top = window.innerHeight/2 - parseFloat(boat.style.height)/2 + "px"
        boat.style.left = window.innerWidth/2 - parseFloat(boat.style.width)/2 + "px"

    }
    
    //option1 styles
    option1.style.height = window.innerHeight/5 + "px"
    option1.style.top = window.innerHeight - window.innerHeight/5 + "px"
    option1.style.width = window.innerWidth/2 + "px"
    option1.style.left = 0

    //option2 styles
    option2.style.height = window.innerHeight/5 + "px"
    option2.style.top = window.innerHeight - window.innerHeight/5 + "px"
    option2.style.width = window.innerWidth/2 + "px"
    option2.style.left = window.innerWidth/2 + "px"

    //startBtn styles
    startBtn.style.width = window.innerWidth/4 + "px"
    startBtn.style.height = window.innerHeight/4 + "px"
    startBtn.style.left = window.innerWidth/2 - parseFloat(startBtn.style.width)/2 + "px";
    startBtn.style.top = window.innerHeight/1.6 - parseFloat(startBtn.style.height)/2 + "px";
    if (window.innerWidth>window.innerHeight){
        startBtn.style.fontSize = window.innerHeight/10 + "px"
    }
    else{
        startBtn.style.fontSize = window.innerWidth/10 + "px"
    }

    //startBtn image
    startBtnImg.style.width = window.innerWidth/5 + "px"

    //title styles
    title1.style.width = window.innerWidth/3 + "px"
    title1.style.left = window.innerWidth/2 - parseFloat(title1.style.width)/2 + "px";
    title1.style.top = window.innerHeight/3 - parseFloat(title1.style.height)/2 + "px";
    if (window.innerWidth>window.innerHeight){
        title1.style.fontSize = window.innerHeight/25 + "px"
    }
    else{
        title1.style.fontSize = window.innerWidth/25 + "px"
    }
    
    //stats styles
    stats.style.height = window.innerHeight/2 + "px"
    stats.style.top = 0
    stats.style.width = window.innerWidth/4 + "px"
    stats.style.left = 0

    //eventMsg styles
    eventMsg.style.height = window.innerHeight/4 + "px"
    eventMsg.style.width = window.innerWidth/1.5 + "px"
    eventMsg.style.top = window.innerHeight/40 + "px"
    eventMsg.style.left = (window.innerWidth + parseFloat(stats.style.width))/2 - parseFloat(eventMsg.style.width)/2 + "px"


}

const events = [
    {
        name: 'Sharks surround and prepare to attack your boat, what do you do',
        choice: [
          'Flee the mass hoard of sharks, no matter who we leave behind',
          "Fight, we're eating shark meat tonight"
        ]
      },
      {
        name: 'Pirates are closing in on your boat ready to attack, what do you do',
        choice: [
          'Surrender, better to live with what we can',
          'Fight, we take this battle to the end'
          ]
      },
      {
        name: '2 members of your crew are infected with scurvy, what do you do with them',
        choice: [
          'Throw infected crew members overboard',
          'Treat them with fruit'
        ]
      },
      {
        name: 'You find a questionable boat stranded at sea, what do you do',
        choice: [
          'Avoid the strange boat',
          'Go to boat and search its insides'
     
        ]
      },
      {
        name: 'You find a captain who offers to sell you a map, what do you do?',
        choice: [
          'Buy a Map from the mysterious captain',
          'Decline the offer'
      ]
      },
      {
        name: 'You find a shortcut that might save time, or not, what do you do',
        choice: [
          "I don't think we should risk it",
          'Try the potential shortcut'
        ]
      },
      {
        name: 'Your crew is caught in a fog, you could risk saving time, but you might lose time',
        choice: [
          'Stay put, no need to lose ourselves',
          'Travel Anyways, we need to make it there in time'
          ]
      },
      {
        name: 'You run into a mysterious island',
        choice: [
          'Explore the island, maybe there are supplies.',
          'Sail around the island.'
        ]
      },
      {
        name: 'Your crew finds a suspicious shipment of supplies floating in the ocean, a crew member thanks the Goddess of Fortune Zaena',
        choice: [
          'Salvage the cargo, do not question gifts the godess gives',
          'Leave it, no need to fall into a trap'
        ]
      },
      {
        name: 'Your ship is caught in a storm, how do you recover',
        choice: [
          'Pray to Eltia, the Goddess of the Ocean and stay put.'
          ,
          'Brave the storm, we will make it.'
          ]
      },
      {
        name: 'A woman on the ship suddenly goes into labor, what do you do',
        choice: [
          "Help her, we aren't monsters."
        ,
          'Make her walk the plank (why are you this way?)'
          ]
      },
      {
        name:'Your crew revolts against you, what do you try',
          choice: [
            'The best offense is a good defense.'
          ,
            'Bribe them, paying them more always works.'
          ]
        },
        {
          name: "Your crew is feeling a little hungry and wants to stop and fish",
          choice: [
            'Stop and fish for some food.',
            'Keep sailing, no need to waste time.'
          ]
        }
  
];
 

 function checkGame(){
    
    if (rounds<=0){
        gameOver=true
        deathMsg = ("<p>Congratulations! You have survived the journey!</p>")
        option1.innerHTML = ('GAME OVER')
        option2.innerHTML = ('GAME OVER')
        eventMsg.innerHTML = (deathMsg)
    }
    else if(boatHealth<=0||food<=0||crew<=0||supplies<=0){
        if (sinkingShip == true){
            gameOver=true
            deathMsg = ("<p>The Ship Sunk!</p>")
        }
        if (starvation == true){
            gameOver=true
            deathMsg = ("<p>Eat Something!</p>")
        }
        if (lackOfCrew == true){
            gameOver=true
            deathMsg = ("<p>I Have Social Anxiety</p>")
        }
        if (scurvy == true){
            gameOver=true
            deathMsg = ("<p>You Need Some Vitamin C</p>")
        }
        if (lBaby == true){
            gameOver=true
            deathMsg = ("<p>I Hate Babies</p>")
        }
        if (sharks == true){
            gameOver=true
            deathMsg = ("<p>Shark Attack!</p>")
        }
        if (pirates == true){
            gameOver=true
            deathMsg = ("<p>Arg Give Me Yur Booty!</p>")
        }
        if (stormy == true){
            deathMsg = ("<p>Down to Davy Jones Locker</p>")
            gameOver=true
        }
        if (mystery == true){
            gameOver=true
            deathMsg = ("<p>S.S Curiosity</p>")
        }
        if (curse == true){
            gameOver=true
            deathMsg = ("<p>Why Does This Island have Cannibals?</p>")
        }
        if (shortNot == true){
            gameOver=true
            deathMsg = ("<p>Short Not</p>")
        }
        if (badCap == true){
            gameOver=true
            deathMsg = ("<p>Imagine being broke LOL</p>")
        }
        option1.innerHTML = ('GAME OVER')
        option2.innerHTML = ('GAME OVER')
        eventMsg.innerHTML = (deathMsg)
        boat.style.backgroundImage = "url('images/boatdamage.png')"
    }
    sinkingShip = false
    starvation = false
    lackOfCrew = false
    scurvy = false
    lBaby = false
    sharks = false
    pirates = false
    stormy = false
    mystery = false
    curse = false
    shortNot = false
    badCap = false
    
 }


function newEvent(){
    rounds-=1
    food-=crew
    loadLoss()
    option1.innerHTML = ('please wait')
    option2.innerHTML = ('please wait')
    transition=true

    console.log(boatHealth)

    setTimeout(function(){
        checkGame()
        loadStats()
        randomSupplies = Math.floor(Math.random() * 2) +1
        if (gameOver==false){
            randomEvent = events[Math.floor(Math.random() * events.length)];
            eventMsg.innerHTML = (randomEvent.name)
            option1.innerHTML = (randomEvent.choice[0])
            option2.innerHTML = (randomEvent.choice[1])
            transition=false

            prevBoatHealth = boatHealth
            prevFood = food
            prevCrew = crew
            prevSupplies = supplies
            prevRounds = rounds

            console.log(boatHealth)
            console.log(randomEvent)
            

            if (randomEvent.name == 'Sharks surround and prepare to attack your boat, what do you do') {
                enableSharkBackground();
                disablePirateBackground();
                disableFogBackground();
                disableMysteryBoat();
                disableIsland();
                disableCaptainBackground();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
              } else if (randomEvent.name == 'Pirates are closing in on your boat ready to attack, what do you do') {
                enablePirateBackground();
                disableSharkBackground();
                disableFogBackground();
                disableMysteryBoat();
                disableIsland();
                disableCaptainBackground();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
              } else if (randomEvent.name == 'Your crew is caught in a fog, you could risk saving time, but you might lose time') {
                enableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableIsland();
                disableCaptainBackground();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if (randomEvent.name == 'You find a questionable boat stranded at sea, what do you do') {
                enableMysteryBoat();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableIsland();
                disableCaptainBackground();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if (randomEvent.name == 'You run into a mysterious island') {
                enableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableCaptainBackground();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if(randomEvent.name == 'You find a captain who offers to sell you a map, what do you do?') {
                enableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if(randomEvent.name == 'You find a shortcut that might save time, or not, what do you do') {
                enableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if(randomEvent.name == 'Your crew finds a suspicious shipment of supplies floating in the ocean, a crew member thanks the Goddess of Fortune Zaena') {
                enableBoxBackground();
                disableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if(randomEvent.name == 'Your crew is feeling a little hungry and wants to stop and fish') {
                enableHungry();
                disableBoxBackground();
                disableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if(randomEvent.name == 'Your ship is caught in a storm, how do you recover') {
                enableStorm();
                disableHungry();
                disableBoxBackground();
                disableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
                disableInfection();
                disableWoman();
                disableRevolt();
            } else if(randomEvent.name == '2 members of your crew are infected with scurvy, what do you do with them') {
                enableInfection();
                disableStorm();
                disableHungry();
                disableBoxBackground();
                disableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
            } else if(randomEvent.name == 'A woman on the ship suddenly goes into labor, what do you do') {
                enableWoman();
                disableStorm();
                disableHungry();
                disableBoxBackground();
                disableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
            } else if(randomEvent.name == 'Your crew revolts against you, what do you try') {
                enableRevolt();
                disableStorm();
                disableHungry();
                disableBoxBackground();
                disableShortcut();
                disableCaptainBackground();
                disableIsland();
                disableFogBackground();
                disablePirateBackground();
                disableSharkBackground();
                disableMysteryBoat();
            } else {
                disableFogBackground();
                disableSharkBackground();
                disablePirateBackground();
                disableMysteryBoat();
                disableIsland();
                disableCaptainBackground();
                disableShortcut();
                disableBoxBackground();
                disableHungry();
                disableStorm();
                disableInfection();
                disableWoman();
                disableRevolt();
              }
        }
    },1000) 
}


//START UP FUNCTION
function firstEvent(){ 
    eventMsg.innerHTML = ('Welcome to uncharted sailing! As you set sail, you can choose to accept one of two gifts. What do you choose?')
    option1.innerHTML = ('<p>accept extra food</p>')
    option2.innerHTML = ('<p>accept extra boat health</p>')

}

//EVENT MESSAGE LOSS OR GAIN
function loadLoss(){
    if(prevBoatHealth>boatHealth){
        eventMsg.innerHTML = ('Gained ' + (prevBoatHealth-boatHealth) + ' boat health.')
    }
    else if(prevBoatHealth<boatHealth){
        eventMsg.innerHTML = ('Lost ' + (boatHealth-prevBoatHealth) + ' boat health.')
    }
    else {
        eventMsg.innerHTML = ('')
    }
    if(prevFood>food){
        eventMsg.innerHTML += ('Gained ' + (prevFood-food) + ' food.')
    }
    else if(prevFood<food){
        eventMsg.innerHTML += ('Lost ' + (food-prevFood) + ' food.')
    }
    if(prevCrew>crew){
        eventMsg.innerHTML += ('Gained ' + (prevCrew-crew) + ' crew members.')
    }
    else if(prevCrew<crew){
        eventMsg.innerHTML += ('Lost ' + (crew-prevCrew) + ' crew members.')
    }
    if(prevSupplies>supplies){
        eventMsg.innerHTML += ('Gained ' + (prevSupplies-supplies) + ' supplies.')
    }
    else if(prevSupplies<supplies){
        eventMsg.innerHTML += ('Lost ' + (supplies-prevSupplies) + ' supplies.')
    }
    if(prevRounds>rounds){
        eventMsg.innerHTML += ('Gained ' + (prevRounds-rounds) + ' days.')
    }
    else if(prevRounds<rounds){
        eventMsg.innerHTML += ('Lost ' + (rounds-prevRounds) + ' days.')
    }
    
}

//BOAT COMING ON SCREEN ANIMATION
function boatAnimation1(){
    setSize()
    inPosition=false
    boat.style.top = window.innerHeight + "px"
    console.log(boat.style.top)
    console.log(boat.style.width)
    boat.style.left = window.innerWidth/2 - parseFloat(boat.style.width)/2 + "px" //will fix later
    var boatAppear = setInterval(function(){
        boat.style.top = parseFloat(boat.style.top) - (window.innerHeight/2 + parseFloat(boat.style.height)/2)/30 + "px"
    },250)
    setTimeout(function(){
        clearInterval(boatAppear)
        inPosition=true
        setSize()
    },7500)
}

//BACKGROUND MOVING ANIMATION
setInterval(function(){
    background.style.backgroundPositionY = parseFloat(background.style.backgroundPositionY) + window.innerHeight/120 + "px"
},50)
setInterval(function(){
    sharkBackground.style.backgroundPositionY = parseFloat(background.style.backgroundPositionY) + window.innerHeight/120 + "px"
},50)
setInterval(function(){
    hungry.style.backgroundPositionY = parseFloat(background.style.backgroundPositionY) + window.innerHeight/120 + "px"
},50)
setInterval(function(){
    fog.style.backgroundPositionX = parseFloat(background.style.backgroundPositionY) + window.innerHeight + "px"
},50)
setInterval(function(){
    storm.style.backgroundPositionY = parseFloat(background.style.backgroundPositionY) + window.innerHeight/120 + "px"
},50)

//BOAT BOBBING ANIMATION
let bobbing = setInterval(function(){
    if (inPosition==true){
        boat.style.top = parseFloat(boat.style.top) - window.innerHeight/120 + "px"
        setTimeout(function(){
            boat.style.top = parseFloat(boat.style.top) + window.innerHeight/120 + "px"
        },400)
    } 
},800)
//BOAT BOBBING ANIMATION
let infectedBobbing = setInterval(function(){
    if (inPosition==true){
        infection.style.top = parseFloat(infection.style.top) - window.innerHeight/120 + "px"
        setTimeout(function(){
            infection.style.top = parseFloat(infection.style.top) + window.innerHeight/120 + "px"
        },400)
    } 
},800)
//BOAT BOBBING ANIMATION
let womanBobbing = setInterval(function(){
    if (inPosition==true){
        woman.style.top = parseFloat(woman.style.top) - window.innerHeight/120 + "px"
        setTimeout(function(){
            woman.style.top = parseFloat(woman.style.top) + window.innerHeight/120 + "px"
        },400)
    } 
},800)
//BOAT BOBBING ANIMATION
let revoltBobbing = setInterval(function(){
    if (inPosition==true){
        revolt.style.top = parseFloat(revolt.style.top) - window.innerHeight/120 + "px"
        setTimeout(function(){
            revolt.style.top = parseFloat(revolt.style.top) + window.innerHeight/120 + "px"
        },400)
    } 
},800)
let pirateBobbing = setInterval(function(){
    if (inPosition==true){
        pirate.style.backgroundPositionY = parseFloat(pirate.style.backgroundPositionY) - window.innerHeight/120 + "px"
        setTimeout(function(){
            pirate.style.backgroundPositionY = parseFloat(pirate.style.backgroundPositionY) + window.innerHeight/120 + "px"
        },400)
        
    } 
},800)
let captainBobbing = setInterval(function(){
    if (inPosition==true){
        captain.style.backgroundPositionY = parseFloat(captain.style.backgroundPositionY) - window.innerHeight/120 + "px"
        setTimeout(function(){
            captain.style.backgroundPositionY = parseFloat(captain.style.backgroundPositionY) + window.innerHeight/120 + "px"
        },400)
        
    } 
},800)
let islandBobbing = setInterval(function(){
    if (inPosition==true){
        island.style.backgroundPositionY = parseFloat(island.style.backgroundPositionY) - window.innerHeight/120 + "px"
        setTimeout(function(){
            island.style.backgroundPositionY = parseFloat(island.style.backgroundPositionY) + window.innerHeight/120 + "px"
        },400)
        
    } 
},800)
let shortcutBobbing = setInterval(function(){
    if (inPosition==true){
        shortcuts.style.backgroundPositionY = parseFloat(shortcuts.style.backgroundPositionY) - window.innerHeight/120 + "px"
        setTimeout(function(){
            shortcuts.style.backgroundPositionY = parseFloat(shortcuts.style.backgroundPositionY) + window.innerHeight/120 + "px"
        },400)
        
    } 
},800)
let boxBobbing = setInterval(function(){
    if (inPosition==true){
        box.style.backgroundPositionY = parseFloat(box.style.backgroundPositionY) - window.innerHeight/120 + "px"
        setTimeout(function(){
            box.style.backgroundPositionY = parseFloat(box.style.backgroundPositionY) + window.innerHeight/120 + "px"
        },400)
        
    } 
},800)
let mysteryBobbing = setInterval(function(){
    if (inPosition==true){
        mysteryBoat.style.backgroundPositionY = parseFloat(mysteryBoat.style.backgroundPositionY) - window.innerHeight/120 + "px"
        setTimeout(function(){
            mysteryBoat.style.backgroundPositionY = parseFloat(mysteryBoat.style.backgroundPositionY) + window.innerHeight/120 + "px"
        },400)
        
    } 
},800)
//STATS 
function loadStats(){
    stats.innerHTML = ("<h1 class='center' class='stat'><strong>Stats</strong></h1><h1 class='stat'>Boat Health: "+ boatHealth +"</h1><h1 class='stat'>Food: "+ food +"</h1><h1 class='stat'>Crew: "+ crew +"</h1><h1 class='stat'>Supplies: " + supplies + "</h1><h1 class='stat'>Days Until Land: "+ rounds +"</h1>")
}

//WHEN THE START BUTON IS CLICKED
function startGame(){
    boatAnimation1()
    loadStats()
    playMusic()
    option1.style.opacity = 1
    option1.disabled = false
    option2.style.opacity = 1
    option2.disabled = false
    boat.style.opacity = 1
    stats.style.opacity = 1
    startBtn.style.opacity = 0
    startBtn.disabled = true
    title1.style.opacity = 0
    eventMsg.style.opacity = 1
    console.log(window.innerWidth)
    firstEvent()
}

//WHEN THE TAB IS OPENED OR RELOADED
function start(){
    setSize()
    background.style.backgroundPositionY = 0
    option1.disbled = true
    option1.style.opacity = 0
    option2.disbled = true
    option2.style.opacity = 0
    boat.style.opacity = 0
    stats.style.opacity = 0
    eventMsg.style.opacity = 0
    mysteryBoat.style.opacity = 1
    disableFogBackground()
    disableSharkBackground()
    disablePirateBackground()
    disableCaptainBackground()
    disableMysteryBoat()
    disableIsland()
    disableShortcut()
    disableBoxBackground()
    disableHungry()
    disableStorm()
    disableInfection()
    disableWoman()
    disableRevolt()
}
start()
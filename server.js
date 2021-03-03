const express = require('express')
const app = express()
const port = 3000

var players = []

initialize_gameboard = function(x, y) {
    // Starta upp spelet med X rader
    var game_board= new Array(y)

    for (row in games_state) {
        games_state[row].append(new Array(x))
    }

    return game_board
}

var game_loop = function() {
    var game_state = initialize_gamestate()
}

var update_state = async function() {
    // Sends states to the gameclients
}

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/move', (req, res) => {
  /* A player makes a move 
    Check identification of the player too see which player
    is making a move

    Then update the gamestate accordingly.
  */
  res.send('Hello World!')
})

app.get('/add_player', (req, res) => {
  /* Add another player to the game */
  
  // Instanciate player

  

  res.send('Hello World!')

})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)

})





/* 
Tankar inför backend:

1. Skapa en funktion som bygger upp start state för en karta
2. När denna karta skickas till klienterna ska klienten kunna rita upp denna
3. När en klient gör en move, skicka denna till servern
4. Servern tar emot move och uppdaterar state # OBS HA NÅGON SORTS SYNCHRONIZERING HÄR FÖR BÄGGE SPELARNA

  - Kanske går att kolla på timestamps för varje move, och uppdatera varje 0.1s eller liknande?

5. Done?


*/
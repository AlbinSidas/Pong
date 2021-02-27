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
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)

})




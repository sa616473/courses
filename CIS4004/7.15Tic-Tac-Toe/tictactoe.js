let playerTurn = true;
let computerMoveTimeout = 0;

window.addEventListener("DOMContentLoaded", domLoaded);

function domLoaded() {
	// Setup the click event for the "New game" button
	let newBtn = document.getElementById("newGameButton");
	newBtn.addEventListener("click", newGame);

	// Create click-event listeners for each cell in the game board
	let cells = getGameBoard();
	for (let cell of cells) {
		cell.addEventListener("click", function () { cellClicked(cell); });
	}

	// Call newGame() to make sure the board is clear
	newGame();
}

// Returns an array of 9 <td> elements that make up the game board. The first 3 
// elements are the top row, the next 3 the middle row, and the last 3 the 
// bottom row. 
function getGameBoard() {
	let gameBoardTable = document.getElementById("gameBoard");
	let result = [];
	for (let i = 0; i < 3; i++) {
		for (let j = 0; j < 3; j++) {
			result.push(gameBoardTable.rows[i].cells[j]);
		}
	}
	return result;
}

function newGame() {
	// TODO: Complete the function
    /*
    1. Use clearTimeout() to clear the computer's move timeout and then set computerMoveTimeout back to 0.
    2. Loop through all game board cells and set the inner HTML of each to a non-breaking space: &nbsp;
    3. Reset to the player's turn by setting playerTurn to true.
    4. Set the text of the turn information paragraph to "Your turn".
*/
    
    clearTimeout(computerMoveTimeout);
    
    // Set innerHTML of all cells to "&nbsp;"
	let cells = getGameBoard();
    
	for (let cell of cells) 
    {
		cell.innerHTML = "&nbsp;";
	}
    
    playerTurn = true;
    document.getElementById("turnInfo").innerHTML = "Your turn";
    
}

function cellClicked(cell) {
	// TODO: Complete the function
    /*
    Implement the cellClicked() function to do the following:

    If playerTurn is true and the clicked cell is empty:
    1. Set the cell's innerHTML to "X"
    2. Set the cell's style color to "red"
    3. Call switchTurn()
    */
    if(playerTurn && cell.innerHTML !== "X" && cell.innerHTML !== "O")
    {    
        cell.innerHTML = "X";
		cell.style.color = "red";
        switchTurn();
    }
}

function switchTurn() {
	// TODO: Complete the function
    /*
    Implement the switchTurn() function to do the following:

    1. If switching from the player's turn to the computer's turn, use setTimeout() to call makeComputerMove() after 1 second (1000 milliseconds). Assign the return value of setTimeout() to computerMoveTimeout. The timeout simulates the computer "thinking", and prevents the nearly-instant response to each player move that would occur from a direct call to makeComputerMove().
    2. Toggle playerTurn's value from false to true or from true to false.
    3. Set the turn information paragraph's text content to "Your turn" if playerTurn is true, or "Computer's turn" if playerTurn is false.
    */
    // true is the computer
    if(playerTurn)
    {
        computerMoveTimeout = setTimeout(makeComputerMove, 1000);
        playerTurn = false;
        document.getElementById("turnInfo").innerHTML = "Your turn";
    }
    // false is the human
    else
    {
        playerTurn = true;
        document.getElementById("turnInfo").innerHTML = "Computer's turn";
    }
}

function makeComputerMove() {
	// TODO: Complete the function
    /*
Implement makeComputerMove() so that the computer puts an "O" in a random, available cell. Set the cell's style color to "blue". Call switchTurn() at the end of the function to switch back to the player's turn.    */
    
    let cells = getGameBoard();
    
	for (let cell of cells) 
    {
		cell.innerHTML = "O";
        cell.style.color = "blue";
	}
    
    switchTurn();
    
}
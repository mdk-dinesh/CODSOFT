const choices = ['rock', 'paper', 'scissors'];
const emojis = {
    rock: '✊',
    paper: '✋',
    scissors: '✌️'
};

let scores = {
    player: 0,
    computer: 0
};

// DOM Elements
const playerDisplay = document.getElementById('player-score');
const computerDisplay = document.getElementById('computer-score');
const resultText = document.getElementById('result-text');
const choicesContainer = document.getElementById('choices-container');
const choicesDisplay = document.getElementById('choices-display');
const userPickEmoji = document.getElementById('user-pick');
const computerPickEmoji = document.getElementById('computer-pick');
const playAgainBtn = document.getElementById('play-again');

// Event Listeners
document.querySelectorAll('.choice-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const userChoice = e.target.closest('.choice-btn').dataset.choice;
        playGame(userChoice);
    });
});

playAgainBtn.addEventListener('click', resetRound);

function playGame(userChoice) {
    const computerChoice = choices[Math.floor(Math.random() * 3)];
    const result = getWinner(userChoice, computerChoice);
    
    updateScore(result);
    updateUI(userChoice, computerChoice, result);
}

function getWinner(player, computer) {
    if (player === computer) return 'tie';
    
    if (
        (player === 'rock' && computer === 'scissors') ||
        (player === 'paper' && computer === 'rock') ||
        (player === 'scissors' && computer === 'paper')
    ) {
        return 'win';
    }
    
    return 'loss';
}

function updateScore(result) {
    if (result === 'win') scores.player++;
    if (result === 'loss') scores.computer++;
    
    playerDisplay.textContent = scores.player;
    computerDisplay.textContent = scores.computer;
}

function updateUI(userChoice, computerChoice, result) {
    // Hide buttons, show result
    choicesContainer.style.display = 'none';
    choicesDisplay.style.display = 'flex';
    playAgainBtn.classList.add('active');
    
    userPickEmoji.textContent = emojis[userChoice];
    computerPickEmoji.textContent = emojis[computerChoice];
    
    resultText.className = ''; // reset classes
    
    if (result === 'win') {
        resultText.textContent = "YOU WIN!";
        resultText.classList.add('win');
    } else if (result === 'loss') {
        resultText.textContent = "YOU LOSE!";
        resultText.classList.add('loss');
    } else {
        resultText.textContent = "IT'S A TIE!";
        resultText.classList.add('tie');
    }
}

function resetRound() {
    choicesContainer.style.display = 'flex';
    choicesDisplay.style.display = 'none';
    playAgainBtn.classList.remove('active');
    resultText.textContent = "Pick your weapon!";
    resultText.className = '';
}

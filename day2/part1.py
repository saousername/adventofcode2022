totalScore = 0

oppChoices = {"A": "rock", "B": "paper", "C": "scissors"}
myChoices = {"Y": "paper", "X": "rock", "Z": "scissors"}

shapeScores = {"rock": 1, "paper": 2, "scissors": 3}

inputFile = open("data.txt", "r")
puzzleInputs = inputFile.readlines()

def whatWins(oppChoice, playerChoice):
    # DRAW
    if playerChoice == oppChoice:
        return "draw"
    # WINS
    elif playerChoice == "rock" and oppChoice == "scissors":
        return "win"
    elif playerChoice == "paper" and oppChoice == "rock":
        return "win"
    elif playerChoice == "scissors" and oppChoice == "paper":
        return "win"
    # LOSSES
    elif playerChoice == "scissors" and oppChoice == "rock":
        return "lose"
    elif playerChoice == "rock" and oppChoice == "paper":
        return "lose"
    elif playerChoice == "paper" and oppChoice == "scissors":
        return "lose"


for puzzleInput in puzzleInputs:
    puzzleInput = puzzleInput.strip()
    oppChoice = oppChoices[puzzleInput.split(" ")[0]]
    playerChoice = myChoices[puzzleInput.split(" ")[1]]

    roundResult = whatWins(oppChoice, playerChoice)

    # WIN
    if roundResult == "win":
        totalScore += 6
    # DRAW
    elif roundResult == "draw":
        totalScore += 3
    # LOSS
    elif roundResult == "lose":
        totalScore += 0 # Ineffective - just for sanity
    
    totalScore += shapeScores[playerChoice]

print(f"Complete simulation! The total score is {str(totalScore)}!")
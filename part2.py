totalScore = 0

oppChoices = {"A": "rock", "B": "paper", "C": "scissors"}
myChoices = {"Y": "paper", "X": "rock", "Z": "scissors"}
desiredResults = {"Y": "draw", "X": "lose", "Z": "win"}

shapeScores = {"rock": 1, "paper": 2, "scissors": 3}

correctChoices = { "win": { "scissors": "rock", "rock": "paper", "paper": "scissors" }, "lose": { "scissors": "paper", "paper": "rock", "rock": "scissors" } }

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

def whatToPlay(oppChoice, desiredResult):
    if desiredResult == "draw":
        return oppChoice
    else:
        return correctChoices[desiredResult][oppChoice]

for puzzleInput in puzzleInputs:
    puzzleInput = puzzleInput.strip()
    oppChoice = oppChoices[puzzleInput.split(" ")[0]]
    desiredResult = desiredResults[puzzleInput.split(" ")[1]]
    playerChoice = ""

    playerChoice = whatToPlay(oppChoice, desiredResult)

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

print(totalScore)
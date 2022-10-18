from flask import Flask, request

app = Flask(__name__)

numbers = []
numberOfTries = 1


# returns true if there are duplicates
def checkIfDuplicates(array):
    return False if len(array) == len(set(array)) else True


def consensus():
    global numberOfTries
    # to inform the user
    print(numbers)
    thereIsConsensus = checkIfDuplicates(numbers)
    if thereIsConsensus:
        print("Consensus achieved!!! " + "it took " + str(numberOfTries) + " tries")
        # reset the number of tries
        numberOfTries = 1
    else:
        print("No consensus :(")
        numberOfTries += 1
    # flush the array after every iteration
    numbers.clear()


@app.post("/addNumber")
def add_thing():
    global numberOfTries
    if request.is_json:
        thing = request.get_json()
        # store the received number in the numbers array
        numbers.append(thing["random"])
        # once the clients have sent their numbers, the consensus method is executed to check if there is consensus
        if len(numbers) >= 3:
            consensus()
        return thing, 201
    return {"error": "Request must be JSON"}, 415

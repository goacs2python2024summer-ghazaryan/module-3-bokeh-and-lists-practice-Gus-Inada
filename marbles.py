import random


def marble_game(plays):
    results = []
    count = 0
    for _ in range(plays):
        choices = ["red", "red", "black", "blue", "blue", "blue"]
        random.shuffle(choices)
        first = choices.pop()
        second = choices.pop()
        if first == second:
            count +=1
        else:
            count -=1
        results.append(count)
    return results

print (marble_game(10))
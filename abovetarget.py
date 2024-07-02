

def aboveTarget(numbers, target):
    for number in numbers:
        if number < target:
            return True
    return False

numbers = [1, 2, 3, 4, 5]
target = 4

print (aboveTarget(numbers, target)) 
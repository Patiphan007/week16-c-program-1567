def eventOdd(x:int)->int:
    if(x % 2 == 0):
        result = "event"
        return x
    else:
        return x
        return result
    
def callEventOdd():
    print("Plese enter number: ")
    x = int(input())
    ans = eventOdd(x)
    print(f"Number = {x} is {ans}")
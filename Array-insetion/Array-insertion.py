import array


def InsertElement(arr,n,pos,x):
    n = int(input("Enter the size of the array"))
    inputArray = [0] * n 
    print(inputArray)

    for i in range(n):
        while True:
            try:
              inputValue = input(f"Enter the value {i+1} element")
              inputArray[i] = int(inputValue)
              break;
            except ValueError:
                print("value error")
            
    x = int(input("Enter the element you want to insert"))
    pos = int(input("Enter the exact position you want to enter the element"))
    arr = array.array("i", inputArray)
    for i in range(n-1,pos-1,-1):
        arr[i + 1] = arr[i]
        arr[pos] = x
        arr.pop()
        print(arr[pos]) 
        print(arr)      

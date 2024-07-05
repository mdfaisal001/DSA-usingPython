import array


def InsertElement(arr,n,pos,x):
    n = int(input("Enter the size of the array"))
    inputArray = [0] * n  # array of [0,0,....] to n time
    print(inputArray)

    for i in range(n):
        while True:
            try:
              inputValue = input(f"Enter the value {i+1} element") #getting input for the input array which contain [0,0,..]
              inputArray[i] = int(inputValue)
              break;
            except ValueError:
                print("value error")
            
    x = int(input("Enter the element you want to insert"))   #getting input for the element to be insert
    pos = int(input("Enter the exact position you want to enter the element")) #getting input for the position of the element
    arr = array.array("i", inputArray) #input array
    for i in range(n-1,pos-1,-1): #loop start from end 
        arr[i + 1] = arr[i] #shifting the elements to right
    arr[pos] = x
    arr.pop()
    print(arr[pos]) 
    print(arr)      

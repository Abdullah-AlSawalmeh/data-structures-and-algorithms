# Code Challenge Whiteboarding

1. Problem Domain:

> > create a function that takes in a value and and array, return a new array with the value added to it is middle without using any Python built-in method.

2. In/Out

> > Input: Array of n elements and a value
> > Output: Array with the value added to it is middle

3. Edge cases:

- Empty array
- Not adding a value
- Null
- Not an array
- Array of single element

4. Visulization

- In: [2,4,6,-8], 5
- Out: [2,4,5,6,-8]

- In: [42,8,15,23,42], 16
- Out: [42,8,15,16,23,42]

- In: [], 5
- Out: [5]

- In: ["Hello"], "Abdullah"
- Out: ["Hello", "Abdullah"]

5. Big-O: Look at the code below

6. Algortihm:

   1. Add the element to the end of the array
   2. Get the length of the array
   3. Loop through the array by using it is length
   4. Swap the last value with the before last value and so, until it reach the middle

7. Pseudo Code

   1. test_array = test_array + test_value
   2. Define j=len(a)-1
   3. for i in range of array the array length
      1. temp = test_array[j]
      2. test_array[j] = test_array[j-1]
      3. test_array[j-1] = temp
      4. if (i == j or i+1 == j):
      5. temp = test_array[j-1]
      6. test_array[j-1] = test_array[j]
      7. test_array[j] = temp
      8. break
         j = j -1

8. Code

```python

test_array = [1,2,3,4,5,6,7,8,9,10]
test_value= "Abdullah"

def insertShiftArray(test_array,test_value):

    ######### Method 1
    test_array = test_array + [test_value] # 1 time only
    array_length = len(test_array) # 1 time only
    j = array_length - 1 # 1 time only
    # i = 0
    for i in range(array_length): # n/2 times
      temp = test_array[j] # 1 time in every loop
      test_array[j] = test_array[j-1] # 1 time in every loop
      test_array[j-1] = temp # 1 time in every loop
      if (i == j or i+1 == j): # 1 time in every loop
        temp = test_array[j-1]  # 1 time only
        test_array[j-1] = test_array[j] # 1 time only
        test_array[j] = temp # 1 time only
        break
      j = j -1 # 1 time in every loop

    ######### Method 2
    # if array_length %2 == 1 :
    #   while(i != j) :
    #     temp = test_array[j]
    #     test_array[j] = test_array[j-1]
    #     test_array[j-1] = temp
    #     j = j - 1
    #     i = i + 1

    # if array_length %2 == 0 :
    #   while(i+1 != j) :
    #     temp = test_array[j]
    #     test_array[j] = test_array[j-1]
    #     test_array[j-1] = temp
    #     j = j - 1
    #     i = i + 1

    return test_array

print(insertShiftArray(test_array,test_value))
```

> > Complexity = 1 + 1 + 1 + n/2 \* (5) + 1 + 1 + 1

           = constants + n/2 * (5)
           = constants + n/2 * constant
           = n

> > Time Complexity = O(n/2) = O(n) <br><br>

9. Verification:

In: test_array = [1,2,3,4]  
test_value = "Abdullah"  
expected Out: [1,2,"Abdullah",3,4]

```
test_array = [1,2,3,4,"Abdullah" ]
array_length = 5
j = 4

for 0 in 5:
    temp = "Abdullah"
    test_array[j] = 4
    test_array[j-1] = "Abdullah"

    ### test_array = [1,2,3,"Abdullah",4]

    if (0 == 4 or 0+1 == 4):
        ### No entry
    break

    j = j -1  ===> 3

for 1 in 5:
    temp = "Abdullah"
    test_array[j] = 3
    test_array[j-1] = "Abdullah"

    ### test_array = [1,2,"Abdullah",3,4]

    if (1 == 3 or 1+1 == 3):
        ### No entry
    break

    j = j -1  ===> 2

for 2 in 5:
    temp = "Abdullah"
    test_array[j] = 2
    test_array[j-1] = "Abdullah"

    ### test_array = [1,"Abdullah",2,3,4]

    if (2 == 2 or 2+1 == 2):
        ### entry
        temp = "Abdullah"
        test_array[j-1] = 2
        test_array[j] = "Abdullah"

        ### test_array = [1,2,"Abdullah",3,4]

        break


    j = j -1  ===> 2
```

# Code Challenge Whiteboarding

1. Problem Domain:

> > Create a function the reverse an array, without using any built-in array

2. In/Out

> > Input: Array of n elements
> > Output: Array in reversed ordered

3. Edge cases:

- Empty array
- Null
- Not an array

4. Visulization

- In: [1,2,3,4]
- Out: [4,3,2,1]

- In: []
- Out: []

5. Big-O: Look at the code below

6. Algortihm:

   1. Loop through the array
   2. For every ietration swap the current index with the alternative from the end (so we swap 0 with n-1, 1 with n-2, etc)
   3. Stop when you reach the middle

7. Pseudo Code

   1. Define i=0 and j=len(a)-1
   2. while i<j:
      1. swap a[i] and a[j]
      2. i++
      3. j--

8. Code

```python
  def reverse_array(a): # a has length of n
    if not( type(a) == type([]) ): # If not array
      return 'error' # 1 time only
    i = 0 # 1 time only
    j = len(a)-1 # 1 time only
    while i<j: # n/2 times
      a[i], a[j] = a[j], a[i] # 3 times in every loop
      i += 1 # 1 time in every loop
      j -= 1 # 1 time in every loop
    return a # 1 time only
```

> > Complexity = 1 + 1 + 1 + n/2 \* (3) + 1

           = constants + n/2 * (3)
           = constants + n/2 * constant
           = n

> > Time Complexity = O(n/2) = O(n) <br><br>

9. Verification:

In: a = [7, 'a', 6, -4]
expected Out: [-4, 6, 'a', 7]

i = 0
j = 4-1 = 3
while 0<3: #True
a[0], a[3] = a[3], a[0]
a = [-4, 'a', 6, 7]
i = 0+1 = 1
j = 3-1 = 2

i = 1
j = 2
while 1<2: # True
a[1], a[2] = a[2], a[1]
a = [-4, 6, 'a', 7]
i = 1+1 = 2
j = 2-1 = 1

while 2 < 1: # False
Stop the loop

return [-4, 6, 'a', 7]

<br>

```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

[8,4,23,42,16,15]

i = 1

    j = 0
    temp = 4

    WHILE j >= 0 AND temp < arr[j]=8 ===> True
        arr[1] = 8
        j = j - 1 = -1

    arr[0] = 4

    [4,8,23,42,16,15]

i = 2

    j = 1
    temp = 23
    WHILE j >= 0 AND 23 < arr[j]=8 ===> Flase
    [4,8,23,42,16,15]

i = 3
j = 2
temp = arr[i] = 42
WHILE j >= 0 AND 42 < arr[j]=23 ===> Flase
[4,8,23,42,16,15]

i = 4
j = 3
temp = arr[i] = 16
WHILE j >= 0 AND 16 < arr[j]=42 ===> True
arr[4] = 42
j <-- j - 1 = 2
[4,8,23,16,42,15]
WHILE j >= 0 AND 16 < arr[j]=23 ===> True
arr[3] = 16
j <-- j - 1 = 1
[4,8,16,23,42,15]
WHILE j >= 0 AND 16 < arr[j]=8 ===> False
[4,8,16,23,42,15]

i = 5
j = 4
temp = arr[i] = 42
WHILE j >= 0 AND 42 < arr[j]=23 ===> False
[4,8,16,23,42,15]

i = 6
j = 5
temp = arr[i] = 15
WHILE j >= 0 AND 15 < arr[j]=42 ===> False
... before 16

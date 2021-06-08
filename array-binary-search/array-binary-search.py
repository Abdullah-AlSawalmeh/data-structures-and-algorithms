test_array = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20]
test_value = 17

def BinarySearch(test_array,test_value):
  full_right = len(test_array) - 1
  full_left = 0
  current = full_right//2
  # print(current)
  while(True):
    temp = current
    if test_value > test_array[current]:
      full_left = current
      current = (current) + ((full_right - current + 1)//2)
    if test_value < test_array[current] : 
      full_right = current
      current = (full_left + current + 1) // 2
    if test_value == test_array[current]:
      return current
    if current == temp:
      return -1
      
print(BinarySearch(test_array,test_value))


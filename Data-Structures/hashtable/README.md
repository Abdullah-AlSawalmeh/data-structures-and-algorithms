# Hashtables
### Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.
## Challenge
### The challenge was with collisions and implementing a linked list to solve them, also with testing internals.
## Approach & Efficiency
### The approach used is to convert the key of the input into index and put the key value object in the hashtable, that contains a linked list for the collisions.
### Big O Notation
#### Time: O(1)
#### Space: O(N)
## API
* Create a hashtable with the following methods:
    - `add`which takes in both the key and value. Hash the key, and add the key and value pair to the table, handling collisions as needed.
    - `get` that takes in the key and returns the value from the table.
    - `contains` that takes in the key and returns a boolean, indicating if the key exists in the table already.
    - `hash` that takes in an arbitrary key and returns an index in the collection.
* Insert key, value pair in the hashtable.
* Hash keys to determine is which index it should be added.
* Make a link_list to handle collisions.
* Retrieve the value of the bucket using its key.
* Determine if a specific key is inside the hashtable or not.

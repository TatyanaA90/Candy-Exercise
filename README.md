# Directions

## Candy Functions Exercises
1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list. In the dictionary, the keys should be the name of a candy and the values should be the number of times said candy appears in `friend_favorites`. 

2. Given the list `friend_favorites`, in the function called `create_new_candy_data_structure` return a dictionary. This dictionary should contain keys that are a specific candy which has a corresponding value of a list containing the friends who like said candy. 

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the `candy_name` parameter. The parameter `data` will be the `friend_favorites` data structure. (Hint: think about how you could use other functions you have to implement this function.)

4. In `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. After implementing your functions, familiarize yourself with the first test. Then write some assert statements for the second test. Finally, starting with nominal cases, write tests for each of the functions in the file tests/test_candy_data_structure.py then write tests to handle edge cases.

## `friend_favorite` Data Structure

```python
friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
```
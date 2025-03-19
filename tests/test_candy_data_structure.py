import pytest
from candy_problem.candy_problem import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    '''
    Add your assertions here!
    '''

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''
# Add your own assertions to the test below
def test_get_friends_who_like_specific_candy():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    result = get_friends_who_like_specific_candy(friend_favorites, "lollipop")
    
    # Assert
    assert result == ('Sally', 'Bob')
# Edge: 
# pass candy does not exist in a friends favorite
def test_get_candy_not_in_friends_favorite():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    result = get_friends_who_like_specific_candy(friend_favorites, "lollipop_test")
    
    # Assert
    assert result == ()

def test_create_candy_set():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    result = create_candy_set(friend_favorites)
    
    # Assert
    #assert result == {'sour patch kids', 'chocolate bar', 'licorice', 'lollipop', 'bubble gum', 'nerds', 'laffy taffy', 'milky way'}
    # check if result is set
    assert type(result) == set

def test_create_candy_set_length():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    result = create_candy_set(friend_favorites)
    
    # Assert
    # check result length
    assert len(result) == 8
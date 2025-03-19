friend_favorites = [
    ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
    [ "Bob", ["milky way", "licorice", "lollipop"]],
    [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
    [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
]
    # create a dict of candy in the friend_favorites 
    # add key name of a candy value number of times said candy appears in friend_favorites
    # count each candy appears in the friend_favorites list
    # return  dict
def get_friends_favorite_candy_count(favorites):
    candy_count_dict = {}

    for friend_candy_faforites in favorites:
    #["Sally", [ "lollipop", "bubble gum", "laffy taffy"]]
        for candy in friend_candy_faforites[1]:
            if candy in candy_count_dict:
                candy_count_dict[candy] += 1
            else:
                candy_count_dict[candy] = 1
    print (candy_count_dict)
    return candy_count_dict

#get_friends_favorite_candy_count(friend_favorites)

# create a dict with keys for specific candy with value of 
#  friends who like it
#create_new_candy_data_structure_dict =
#{
#     "lollipop": ["Sally","Bob"],
#     "bubble gum": ["Sally"],
#     ....
#}
#
def create_new_candy_data_structure(favorites):
    favorite_candy = {}
    for friend_candies in favorites:
        for candy in friend_candies[1]:
            if candy not in favorite_candy:
                favorite_candy[candy] = [friend_candies[0]]
            else:
                favorite_candy[candy].append(friend_candies[0])
    return  favorite_candy

create_new_candy_data_structure(friend_favorites)


def get_friends_who_like_specific_candy(favorites, candy_name):
    candy_friends_dict = create_new_candy_data_structure(favorites)
    value = candy_friends_dict.get(candy_name, [])
    return tuple(value)
#print (get_friends_who_like_specific_candy(friend_favorites,"lollipop"))


def create_candy_set(favorites):
    candy_friends_dict = create_new_candy_data_structure(favorites)
    return (set(candy_friends_dict.keys()))
#print (create_candy_set(friend_favorites))



def get_friends_favorite_candy_count(favorites):
    candy_dict = {}

    for friend in favorites:
        for candy in friend[-1]:
            candy_dict[candy] = candy_dict.get(candy, 0) + 1
    
    return candy_dict

def create_new_candy_data_structure(data):
    candy_friend_dictionary = {}

    for ls in data:
        friend = ls[0]
        candies = ls[-1]

        for candy in candies:
            if not candy_friend_dictionary.get(candy):
                candy_friend_dictionary[candy] = [friend]
            else:
                candy_friend_dictionary[candy].append(friend)
    
    return candy_friend_dictionary

def get_friends_who_like_specific_candy(data, candy_name):
    candy_dict = create_new_candy_data_structure(data)

    return tuple(candy_dict[candy_name])

def create_candy_set(data):
    return set(data.keys())



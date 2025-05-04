
def word_counter(words):
    words_list = words.split()
    return len(words_list)

def character_counter(words):
    words = words.lower()
    char_count_dict = {}
    for char in words:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_on(dict2):
    return dict2['num']

def dict_to_sorted_list(dict1):
    unsorted_list = []
    for key in dict1:
        unsorted_list.append({'char': key, 'num':dict1[key]})
        unsorted_list.sort(reverse = True, key = sort_on)
    
    return unsorted_list



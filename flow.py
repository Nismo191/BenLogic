# Imports

# Change dict key to given value
def change_key(new_key, old_key, dict):
    for item in dict:
        item[new_key] = item.pop(old_key)

    return dict


def add_value(new_key, new_value, dict):
    for item in dict:
        item[new_key] = new_value

    return dict


def remove_key(key, dict):
    for item in dict:
        item.pop(key)

    return dict


def join(dict1, dict2, key1, key2):
    newdict = []
    unmatched = []
    for i, item in enumerate(dict1):
        for j, item2 in enumerate(dict2):
            ob = {}
            if item[key1] == item2[key2]:
                ob = {**item, **item2}
                newdict.append(ob)
                break
            if j == len(dict2) - 1:
                unmatched.append(item)

    return newdict, unmatched
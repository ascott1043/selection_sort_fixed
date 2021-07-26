def multi_selection_sort_codebasics(arr, sort_by_list):
    """In this approach we sort the entire array by the last key in the array, and 
    then sort it again for each additional key we use in reverse order. So in our 
    example the array gets sorted by last name, and then again by first name.  
    That means if elements are re-arranged in the second iteration, it can mess up the 
    initial sorting."""
    for key in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][key] < elements[min_index][key]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]

def multi_selection_sort(elements, sort_by_list):
    """In my approach, initially sort the array by the first key (First Name).
    Then I'll break the sorted array down into smaller arrays with matching keys
    ex. the three elements where first name == Raj will be treated as an array of len 3
    
    from there I can do another selection sort of that 3-element array on key 2 (Last Name)
    """
    key_nbr = 0
    for key in sort_by_list:
        #Use a typical selection sort for the first key:
        if key_nbr == 0:
            selection_sort(elements, key)
        #If we're sorting a second/third/etc key, we'll implement my method
        else:
            previous_key = sort_by_list[key_nbr - 1]
            for x in range(len(elements)):
                #If next element doesn't match previous key, skip
                index_array = find_matching_values(elements, x, key, previous_key)
                if not index_array:
                    continue
                #Otherwise, get the smaller array and do a selection sort against it
                else:
                    selection_sort_partial_array(elements, index_array, key)
        key_nbr += 1

def selection_sort(elements, key):
    """Basic selection sort for single dictionary key"""
    for x in range(len(elements)):
        min_index = x
        for y in range(x, len(elements)):
            if elements[y][key] < elements[min_index][key]:
                min_index = y
        if x != min_index:
            elements[x], elements[min_index] = elements[min_index], elements[x]

def selection_sort_partial_array(elements, index_array, key):
    """Sorting partial array. index_array is a list of indexes that have matching
    values for the previous key.  For example if elements[1] and elements[2] both have
    a <First Name> key == 'Armaan', then the index_array sould be [1,2] """
    for x in index_array:
        min_index = x
        for y in range(x, index_array[-1] + 1):
            if elements[y][key] < elements[min_index][key]:
                min_index = y
        if x != min_index:
            elements[x], elements[min_index] = elements[min_index], elements[x]


def find_matching_values(elements, index, key, previous_key):
    """Checks against the values of the previous key. If the next element has 
    different value for that previous key (ex. the first name of the next element is
    different from current), then return None
    Else, return an new array of indexes that match the previous key value
    """
    previous_value = elements[index][previous_key]
    i = index
    new_array = []

    while elements[i][previous_key] == previous_value:
        new_array.append(i)
        if len(elements) > i + 1:
            i += 1
        else:
            break

    if len(new_array) == 1:
        return None
    else:
        return new_array

        

if __name__ == '__main__':
    elements = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    multi_selection_sort(elements, ['First Name','Last Name', 'Middle'])
    for element in elements:
        print(element)

    three_key_elements = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar', 'Middle': 'P'},
    {'First Name': 'Raj', 'Last Name': 'Nayyar', 'Middle': 'Y'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Middle': 'I'},
    {'First Name': 'Karan', 'Last Name': 'Kumar', 'Middle': 'N'},
    {'First Name': 'Jade', 'Last Name': 'Canary', 'Middle': 'N'},
    {'First Name': 'Raj', 'Last Name': 'Thakur', 'Middle': 'I'},
    {'First Name': 'Raj', 'Last Name': 'Sharma', 'Middle': 'S'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Middle': 'E'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Middle': 'M'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar', 'Middle': 'I'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma', 'Middle': 'D'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore', 'Middle': 'X'},
    {'First Name': 'Jaya', 'Last Name': 'Seth', 'Middle': 'I'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra', 'Middle': 'B'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick', 'Middle': 'Z'},
    {'First Name': 'Aahana', 'Last Name': 'Arora', 'Middle': 'A'}
    ]
    print('\n\nTesting with a third key:')

    multi_selection_sort(three_key_elements, ['First Name','Last Name', 'Middle'])
    for element in three_key_elements:
        print(element)
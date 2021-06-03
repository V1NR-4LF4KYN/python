def makeNumReadable(num):
    num_arr = [] # arr for number with each item in num
    # appending reversed str of num to arr
    for letter in str(num)[::-1]: 
        num_arr.append(letter)
    
    counter = 1 # to count to three for dots
    converted_arr = [] # array for converted number (with dots)
    # add a '.' to a '0' if it is the third zero
    for item in num_arr:
        if counter == 3:
            item += '.'
            counter = 0
        counter += 1
        converted_arr.append(item) # adding (changed) item to array
    
    converted_str = '' # var for converted number in string 
    # adding each item of the array to the string
    for item in converted_arr:
        converted_str += item
    # turning it back around
    converted_str = converted_str[::-1]

    # reverting possible error -> dot at beginning of whole converted number
    s_arr = []
    for letter in converted_str: 
        s_arr.append(letter)
    if s_arr[0] == '.':
        s_arr[0] = ''
        converted_str = ''
        for item in s_arr:
            converted_str += item



    # returning converted num as string
    return converted_str
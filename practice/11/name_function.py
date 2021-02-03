def get_full_name(first, last, middle=''):
    if middle:
        fullname = f'{first} {middle} {last}'
    else:
        fullname = f'{first} {last}'
    
    return fullname.title()
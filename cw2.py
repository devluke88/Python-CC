def to_camel_case(text):
    if text:
        if '-' in text:
            tx = text.split('-')
        elif '_' in text:
            tx = text.split('_')
        if tx[0].isupper():
            new_string = ''
            for t in tx:
                new_string += t.capitalize()
        else:
            new_string = tx.pop(0)
            for t in tx:
                new_string += t.capitalize()
    print(new_string)

to_camel_case('the-stealth-warrior')
to_camel_case('The_Stealth_Warrior')
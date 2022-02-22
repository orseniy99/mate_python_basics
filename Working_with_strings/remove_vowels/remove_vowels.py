def remove_vowels(document: str) -> str:
    # write your code here
    no_v = ''
    for i in document:
        if i in 'aeiouyAEIOUY':
            pass
        else:
            no_v += str(i)
    return no_v

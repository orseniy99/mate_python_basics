def make_abbr(words: str) -> str:
    # write your code here
    abbr = ''
    for word in words.split():
        abbr = abbr + word[0]
    return(abbr.upper())

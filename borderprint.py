def bordered(s: str) -> str:
    """ Return string wrapped with a nice 'border',
        .-----------.
        | like this |
        '-----------' .
    """
    # Top row
    bs = '.-'
    for i,char in enumerate(s):
        bs += '-'
    # End top, start middle
    bs += '-.\n| '
    for i,char in enumerate(s):
        bs += char
    # End middle, start bottom
    bs += " |\n'-"
    for i,char in enumerate(s):
        bs += '-'
    bs += "-'"
    return bs

def bordered_print(s: str):
    print(bordered(s))

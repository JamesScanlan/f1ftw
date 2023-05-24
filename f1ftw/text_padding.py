def pad_left(text, padding):
    left_padding = padding - len(text)
    output = ''
    for counter in range(0, left_padding):
        output += ' '
    output += text
    return output

def pad_right(text, padding):
    right_padding = padding - len(text)
    output = text
    for counter in range(0, right_padding):
        output += ' '
    return output
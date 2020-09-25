# Print table functions

def get_width(title, data):
    length = len(title)
    spacing = 5
    for item in data:
        if len(item) > length:
            length = len(item)
    return length + spacing

def print_table(title, data):
    width = get_width(title, data)
    print_header(title, width)
    for item in data:
        print(f'| {item}')
    print_separator(width)

def print_header(title, width):
    print_separator(width)
    print(f'| {title}')
    print_separator(width)

def print_separator(width):
    print(f"+{'=' * width}")


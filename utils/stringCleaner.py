def to_clean_string(raw_string):
        clean_string = ""
        for char in raw_string:
            if char.isdigit():
                clean_string += char
        return clean_string

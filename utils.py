def is_file_dir(string: str):
    if  type(string) != str or \
        len(string.split()) != 1:
        return False
    else:
        string_lt = string.split('/')
        for dir_name in string_lt[:-1]:
            if len(dir_name) > 255:
                return False

        if len(string_lt[-1]) > 255:
            return False

    return True
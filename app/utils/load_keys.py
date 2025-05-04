def get_value(value:str):
    if value == "":
        raise ValueError(f"Got an unxpected API KEY VALUE, {value}")
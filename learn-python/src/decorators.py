def shout(text: str) -> str:
    return text.upper() + "!"


yell = shout

print(yell("hello"))


def log_call(func):
    def wrapper(*args, **kwargs):
        print(
            f"Calling {func.__name__} with arguments: {args} and keyword arguments: {kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


print(log_call(shout)("hello"))


def lowerCase(text: str):
    return text.title()


def naming(func):
    def fName(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return fName


print(naming(lowerCase)("HELLO FERENC"))

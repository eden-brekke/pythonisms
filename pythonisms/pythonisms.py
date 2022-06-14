from functools import wraps
from time import sleep

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        val_undecorated_function = func(*args, **kwargs)
        emphasized = val_undecorated_function.upper() + "!!!!!!"
        return emphasized
    return wrapper

def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "I do DECLARE, " + orig_val
    return wrapper
  
def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2.5)
        return func(*args, **kwargs)
    return wrapper
  
def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Oh of course, "{orig_val}" sounds like a "fantastic" idea. Sure sure, do you\'re thing, it\'ll be totally FINE'
    return wrapper


@procrastinate
@proclaim
def say(txt):
    return txt

@sarcastic_decorator
@emphasize
def restaurant_suggestion(cuisine):
    return cuisine

if __name__ == "__main__":
    print(say('Jackington\'s the third is the bestest of bois.'))
    print(restaurant_suggestion("Thai"))
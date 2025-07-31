from functools import wraps
import logging

logging.basicConfig(
    filename="functions.log",
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
    level=logging.INFO,
)

def log_call(original_function):

    @wraps(original_function) # renames wrapper to original_function's name
    def _wrapper(*args, **kwargs):
        logging.info(f"Called {original_function.__name__}")
        result = original_function(*args, **kwargs)
        return result

    return _wrapper

# @fix_result
# @timestamp
@log_call
def spam():
    print("SPAM SPAM SPAM")
# spam = doit(spam)
spam()  # really calling _wrapper()
spam()
spam()

@log_call
def ham():
    print("HAM!")

@log_call
def eggs():
    print("scrambled!!!")

ham()
eggs()
spam()
spam()
eggs()
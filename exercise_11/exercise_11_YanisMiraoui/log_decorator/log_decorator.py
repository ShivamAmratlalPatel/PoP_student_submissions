from functools import wraps
import logging


def log_call(fn):
    """Return logging info."""

    @wraps(fn)
    def build_message(*args, **kwargs):
        message = "Calling: "
        message += str(fn.__name__) + "("
        for n in args:
            message += repr(n) + ", "
        for n in kwargs:
            message += str(n) + "=" + repr(kwargs[n]) + ", "
        message = message[:-2]
        message += ")"
        print(message)
        logging.info(message)
        return fn(*args, **kwargs)

    return build_message

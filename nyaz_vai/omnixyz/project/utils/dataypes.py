import random
import string
import os
from project import config


def random_intnum():
    """
    Generate a random integer.
    
    Returns:
      A random integer.
    """
    return str(random.randint(config.integer.min, config.integer.max))



def random_realnum():
    """
    Generate a random number
    
    Returns:
      A random floating point number
    """
    length = random.randint(config.float.decimal_min, config.float.decimal_max)
    return str(round(random.uniform(config.float.min, config.float.max), length))



def random_alphanumerics():
    """
    Generate a random string of alphanumerics
    
    Returns:
      A random string of alphanumeric characters.
    """
    length = random.randint(config.alphanumeric.min, config.alphanumeric.max)
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def random_alphabetical():
    """
    Generate a random string of alphabetical characters
    
    Returns:
      A random string of alphabetical characters.
    """
    length = random.randint(config.alphabetical.min, config.alphabetical.max)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


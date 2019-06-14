import numpy as np

def random_vec(length):
    if type(length) is not int:
        raise ValueError("length should be int.")
    elif length <= 0:
        raise ValueError("length should be a positive number.")
    
    return np.random.rand(length)

def normalize_vec(vector):
    return vector / np.linalg.norm(vector)
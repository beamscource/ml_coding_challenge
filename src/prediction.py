from typing import Optional


def predict(data: Optional[list] = None) -> dict:
    """Small example function that will take some data and returns a response.
    Right now everything is with fixed values.

    Args:
        data (list): prediction data

    Returns:
        dict: predict response (DUMMY)
    """
    return {
        "Boot": 0.33,
        "Sandal": 0.33,
        "Shoe": 0.33,
    }

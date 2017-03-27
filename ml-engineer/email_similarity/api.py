
from scipy import spatial

from email_similarity import features


def email_similarity(e1, e2):
    """ Returns a float between 0 and 1 indicating how similar are the
        email addresses parameters `e1` and `e2`.
    """

    return spatial.distance.cosine(
        features.features(e1),
        features.features(e2),
    )

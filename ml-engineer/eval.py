import random
import string

from email_similarity import api


def test_api():
    """
    Test cases consist of lists of email address. The lists are ranking in terms of how similar
    they are to the base email address (most similar to the base case first). The ideal feature
    vectors would perfectly reproduce this ranking. This script produces an ncdg score whereby
    a score of 1 represents a perfect reproduction of the rankings.
    """
    base_email = 'test_account@ravelin.com'

    test_cases = [[
        # append
        'test_account1@ravelin.com',
        'test_account12@ravelin.com',
        'test_account123@ravelin.com',
        'test_account1234@ravelin.com',
        'test_account12345@ravelin.com',
    ], [
        # delete
        'test_accoun@ravelin.com',
        'test_accou@ravelin.com',
        'test_acco@ravelin.com',
        'test_acc@ravelin.com',
        'test_ac@ravelin.com',
    ], [
        # transpose
        'test_acocunt@ravelin.com',
        'test_acocotu@ravelin.com',
        'tset_acocotu@ravelin.com',
    ], [
        # substitution
        't3st_account@ravelin.com',
        't3st_acc0unt@ravelin.com',
        't3st_4cc0unt@ravelin.com',
        't3st.4cc0unt@ravelin.com',
    ], [
        # abbreviation
        't.account@ravelin.com',
        'ta@ravelin.com',
    ]]

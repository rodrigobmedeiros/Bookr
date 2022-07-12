import base64
import json
import pprint
import sys

def get_session_dictionary(session_key):
    """Function used to decode and get dictionary session."""

    _, payload = base64.b64decode(session_key).split(b':', 1)
    session_dictionary = json.loads(payload.decode())
    return session_dictionary

def average_rating(rating_list):
    """Calculate the average rating of a Book."""

    if not rating_list:

        return 0

    return round(sum(rating_list) / len(rating_list))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        session_key = sys.argv[1]
        session_dictionary = get_session_dictionary(session_key)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(session_dictionary)
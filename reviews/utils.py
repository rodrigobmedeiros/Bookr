def average_rating(rating_list):
    """Calculate the average rating of a Book."""

    if not rating_list:

        return 0

    return round(sum(rating_list) / len(rating_list))
def first_different_index(string1: str, string2: str | None = None):
    """Returns the first index where the two strings doesn't match"""

    # The second string is null, so no point in calculating
    if string2 is None:
        return -1

    # Get the shorter string of the two
    shorter_string = string1 if len(string1) < len(string2) else string2

    # Get the first differing index
    for i in range(0, len(shorter_string)):
        if (string1[i] != string2[i] or shorter_string[i] != string1[i]):
            return i
    # This means that the strings are identical
    return -1

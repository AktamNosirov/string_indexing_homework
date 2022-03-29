def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if str(s[0:n+1]).isalpha() :
        return s[0:n+1]
    else:
        bool(0)
print(main('efs4',0))
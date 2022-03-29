def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if n<=len(s)-1:
     return str(s[n]) 
    if n>len(s)-1:
     return bool(0)
     
       
    
print(main('efs4',2))
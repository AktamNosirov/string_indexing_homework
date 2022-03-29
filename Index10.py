def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans=0
    if s[0].isdigit() :
       ans+=int(s[0])
    if s[1].isdigit() :
       ans+=int(s[1])
    if s[2].isdigit() :
       ans+=int(s[2])
    if s[3].isdigit() :
       ans+=int(s[3])
    if s[4].isdigit() :
       ans+=int(s[4])
    
    return ans

print(main("1*2a4"))
  
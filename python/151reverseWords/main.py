def reverseWords(s: str) -> str:
    s = s.strip()
    l = s.split()
    l.reverse()
    return ''.join(l)



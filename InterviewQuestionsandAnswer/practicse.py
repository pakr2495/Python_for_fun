def test(*args,**kwargs):
    print(args)
    print(kwargs)

test(1,2,3,4,5,6,"Test",test=2)

import re

word = "unexpected in expected word"

print(re.findall("(?:un)?expected",word))
print(re.match("(un)?expected",word).group())
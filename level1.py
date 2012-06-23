def foo(x):
    f = open('/home/nick/gettysburg.txt')
    s = f.read()
    rs = s[::-1]

    y = 0

    while y != len(s):
        sub = rs[y:(x+y)]
        print sub
        for i in xrange(0, len(s)):
            if s[i:(i+x)] == sub:
                print "yeah"
                print sub
                return sub

        y = y+1



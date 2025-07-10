# ООП (magic methods)
# method override; operator overloading


class myTime:
    def __init__(self, minutes, seconds):
        if 0 <= minutes < 60:
            self.minutes = minutes
        if 0 <= seconds < 60:
            self.seconds = seconds

    def __add__(self, other):
        m = self.minutes + self.minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        m = m % 60
        print(m, s)
        return myTime(m, s)

    def __str__(self):
        return f'<Time {self.minutes:02}:{self.seconds}>'

t1 = myTime(13, 0)
t2 = myTime(53, 5)
print(t1 + t2)


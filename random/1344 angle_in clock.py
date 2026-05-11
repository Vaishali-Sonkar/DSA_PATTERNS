class Solution(object):
    def angleClock(self, hour, minutes):
        mint=minutes*6
        hr=abs((hour%12)*30+(minutes*0.5))
        diff=abs(mint-hr)
        return min(diff,360-diff)
        
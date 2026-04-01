# https://leetcode.com/problems/insert-interval/
class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]                      # to store the intervals after inserting the new interval
        n=len(intervals)
        ins=False            # to check whether the new interval is inserted or not
        for i in range(0,n):
            start=intervals[i][0]          # starting point of the current interval
            if(ins==False and start>=newInterval[0]):
                res.append(newInterval)
                ins=True
            res.append(intervals[i])
        if(ins==False):            # if the new interval is not inserted then insert it at the end
            res.append(newInterval)
        merge=[]             # to store the merged intervals
        s1=res[0][0]
        e1=res[0][1]
        for i in range(1,len(res)):
            s2=res[i][0]
            e2=res[i][1]
            if(e1>=s2):
                e1=max(e1,e2)         # if the end point of the previous interval is greater than or equal to the start point of the current interval then merge the intervals
                continue
            merge.append([s1,e1])         # if the end point of the previous interval is less than the start point of the current interval then add the previous interval to the merged intervals and update the start and end points of the previous interval
            s1=s2
            e1=e2
        merge.append([s1,e1])               # add the last interval to the merged intervalsS
        return merge
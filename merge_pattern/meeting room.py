#https://www.geeksforgeeks.org/problems/attend-all-meetings-ii/1

class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()        #sort the start and end times of the meetings
        end.sort() 
        n=len(start)
        room=0       
        res=0
        i=0
        j=0
        while(i<n and j<n):
            if(start[i]<end[j]):     #start is small then firstly room will be allocated
                room+=1
                res=max(res,room)
                i+=1                   
            else:                  #if end is small then room will be deallocated
                room-=1             
                j+=1
        return res
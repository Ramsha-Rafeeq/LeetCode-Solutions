class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        from datetime import datetime
        s=datetime.strptime(startTime,"%H:%M:%S")
        e=datetime.strptime(endTime,"%H:%M:%S")
        diff=e-s
        return int(diff.total_seconds())
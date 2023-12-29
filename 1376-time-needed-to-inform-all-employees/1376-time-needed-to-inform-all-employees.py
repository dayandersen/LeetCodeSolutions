class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_map = defaultdict(lambda: list())

        for i in range(len(manager)):
            manager_map[manager[i]].append(i)

        def explore(emp_id, time):
            if emp_id not in manager_map:
                return time
            maxx = 0
            for emp in manager_map[emp_id]:
                maxx = max(explore(emp, time+informTime[emp_id]), maxx)
            return maxx
        
        return explore(headID, 0)

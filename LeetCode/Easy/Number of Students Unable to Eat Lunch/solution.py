class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        q = deque(students)
        rotations = 0

        while q and rotations < len(q):
            if q[0]==sandwiches[0]:
                q.popleft()
                sandwiches.pop(0)
                rotations =0

            else:
                q.append(q.popleft())
                rotations +=1
        return len(q)

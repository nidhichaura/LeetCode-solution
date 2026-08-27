class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [0, 0]
        for s in students:
            counts[s] += 1
            
        # Serve sandwiches in stack order
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                # No student left wants this sandwich; queue stalls
                break
            counts[sandwich] -= 1
            
        # Remaining students cannot eat
        return sum(counts)
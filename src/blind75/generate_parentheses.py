"""
Given n, generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

constraints
1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(opening_count: int, closed_count: int, path):
            indent = "  " * len(path)
            print(f"{indent}backtrack(open={opening_count}, close={closed_count}, path='{path}')")

            if opening_count == closed_count == n:
                print(f"{indent}  -> Found valid combination: '{path}'")
                res.append(path)
                return 

            if opening_count < n:
                backtrack(opening_count + 1, closed_count, path + "(")
            
            if closed_count < opening_count:
                backtrack(opening_count, closed_count + 1, path + ")")
            
        backtrack(0, 0, "")

        return res
                


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    assert set(solution.generateParenthesis(3)) == set(["((()))","(()())","(())()","()(())","()()()"])
    print("Example 1 passed!")
    
    # Example 2
    assert set(solution.generateParenthesis(1)) == set(["()"])
    print("Example 2 passed!")
    
    print("All tests passed!")

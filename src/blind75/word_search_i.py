"""
given an m * n board, and a string
Input: board = [["o","a","a"],["e","t","a"],["t","a","n"]],
        words = "oath"
"""


class Solution:
    def word_search(board, word):
        m = len(board)
        n = len(board[0])

        # DFS
        def dfs(i, j):

            dfs(i + 1, )

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # start dfs


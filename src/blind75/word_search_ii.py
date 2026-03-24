"""
Given an m * n board of characters and a list of words,
return all words from the list that exist in the board.

Input: board = [["o","a","a"],["e","t","a"],["t","a","n"]],
        words = ["oath","pea","eat","tan"]
Output: ["eat","oath"]
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    @staticmethod
    def find_words(board, words):
        if not board or not board[0] or not words:
            return []

        # build trie for all the words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row, col, parent):
            char = board[row][col]
            node = parent.children.get(char)
            if node is None:
                return

            if node.word is not None:
                result.append(node.word)
                node.word = None

            board[row][col] = "#"

            for next_row, next_col in (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ):
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    if board[next_row][next_col] in node.children:
                        dfs(next_row, next_col, node)

            board[row][col] = char

            if not node.children and node.word is None:
                del parent.children[char]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in root.children:
                    dfs(row, col, root)

        return result

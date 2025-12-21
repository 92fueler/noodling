"""
Trie Basics (Prefix Tree)

1. create & initialize - empty trie, from words, TrieNode structure
2. insert (create) - add words to trie
3. search (read) - check if word exists, check if prefix exists
4. delete - remove words from trie
5. traverse - iterate through all words, get all words with prefix
6. patterns & utilities - count words, longest common prefix, autocomplete
"""


# ============================================================================
# 1. CREATE & INITIALIZE
# ============================================================================
class TrieNode:
    """Node structure for Trie"""
    def __init__(self):
        self.children = {}  # dict mapping char -> TrieNode
        self.is_end = False  # marks end of a word


class Trie:
    """Basic Trie implementation"""
    def __init__(self):
        self.root = TrieNode()

    # From list of words
    @classmethod
    def from_words(cls, words):
        """Create trie from list of words"""
        trie = cls()
        for word in words:
            trie.insert(word)
        return trie

    def insert(self, word: str) -> None:
        """Insert word into trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True  # mark end of word

    def search(self, word: str) -> bool:
        """Check if word exists in trie (exact match)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end  # must be end of word

    def starts_with(self, prefix: str) -> bool:
        """Check if any word in trie starts with prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True  # prefix path exists

    def delete(self, word: str) -> bool:
        """Delete word from trie. Returns True if deleted, False if not found"""
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end:
                    return False  # word doesn't exist
                node.is_end = False
                return len(node.children) == 0  # return True if can delete node
            
            char = word[index]
            if char not in node.children:
                return False  # word doesn't exist
            
            child = node.children[char]
            should_delete = _delete(child, word, index + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end
            
            return False
        
        return _delete(self.root, word, 0)

    def get_all_words(self) -> list:
        """Get all words stored in trie"""
        words = []
        
        def dfs(node, prefix):
            if node.is_end:
                words.append(prefix)
            for char, child in node.children.items():
                dfs(child, prefix + char)
        
        dfs(self.root, "")
        return words

    def get_words_with_prefix(self, prefix: str) -> list:
        """Get all words that start with prefix"""
        # Navigate to prefix node
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # prefix doesn't exist
            node = node.children[char]
        
        # Collect all words from this node
        words = []
        
        def dfs(n, path):
            if n.is_end:
                words.append(prefix + path)
            for char, child in n.children.items():
                dfs(child, path + char)
        
        dfs(node, "")
        return words

    def count_words(self) -> int:
        """Count total number of words in trie"""
        count = 0
        
        def dfs(node):
            nonlocal count
            if node.is_end:
                count += 1
            for child in node.children.values():
                dfs(child)
        
        dfs(self.root)
        return count

    def is_empty(self) -> bool:
        """Check if trie is empty"""
        return len(self.root.children) == 0

    def longest_common_prefix(self) -> str:
        """Find longest common prefix among all words in trie"""
        if not self.root.children:
            return ""
        
        prefix = ""
        node = self.root
        
        while len(node.children) == 1 and not node.is_end:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        
        return prefix

    def clear(self) -> None:
        """Remove all words from trie"""
        self.root = TrieNode()

    def autocomplete(self, prefix: str, limit: int = 10) -> list:
        """Get autocomplete suggestions for prefix (limited results)"""
        words = self.get_words_with_prefix(prefix)
        return words[:limit]

    def can_construct(self, word: str) -> bool:
        """Check if word can be formed by concatenating other words in trie"""
        def dfs(word, index, count):
            if index == len(word):
                return count > 1  # must use at least 2 words
            
            node = self.root
            for i in range(index, len(word)):
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                if node.is_end and dfs(word, i + 1, count + 1):
                    return True
            return False
        
        return dfs(word, 0, 0)


# ============================================================================
# 2. INSERT (CREATE)
# ============================================================================
trie = Trie()

# Insert examples
trie.insert("apple")                       # insert "apple"
trie.insert("app")                         # insert "app" (prefix of "apple")
trie.insert("apply")                       # insert "apply"
trie.insert("banana")                      # insert "banana"


# ============================================================================
# 3. SEARCH (READ)
# ============================================================================

# Search if word exists (exact match)
·····trie.search("apple")                       # True - word exists
trie.search("app")                         # True - word exists
trie.search("appl")                        # False - prefix exists but not a word
trie.search("banana")                      # True - word exists
trie.search("ban")                         # False - prefix exists but not a word
trie.search("xyz")                         # False - doesn't exist

# Check if prefix exists (starts with)
trie.starts_with("app")                    # True - "apple", "app", "apply" all start with "app"
trie.starts_with("ban")                    # True - "banana" starts with "ban"
trie.starts_with("xyz")                    # False - no words start with "xyz"
trie.starts_with("")                       # True - empty prefix matches all


# ============================================================================
# 4. DELETE
# ============================================================================

# Delete examples
trie.delete("app")                         # True - deletes "app", keeps "apple" and "apply"
trie.search("app")                         # False - deleted
trie.search("apple")                       # True - still exists
trie.delete("xyz")                         # False - word doesn't exist


# ============================================================================
# 5. TRAVERSE
# ============================================================================

# Traverse examples
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apply")
trie.insert("banana")
trie.get_all_words()                       # ["app", "apple", "apply", "banana"]
trie.get_words_with_prefix("app")          # ["app", "apple", "apply"]
trie.get_words_with_prefix("ban")          # ["banana"]
trie.get_words_with_prefix("xyz")          # []


# ============================================================================
# 6. PATTERNS & UTILITIES
# ============================================================================

# Pattern examples
trie = Trie.from_words(["flower", "flow", "flight"])
trie.count_words()                         # 3
trie.longest_common_prefix()               # "fl"
trie.clear()
trie.is_empty()                            # True

# Autocomplete examples
trie = Trie.from_words(["apple", "app", "apply", "application"])
trie.autocomplete("app", limit=2)          # ["app", "apple"]

# Word break example
trie = Trie.from_words(["leet", "code", "leetcode"])
trie.can_construct("leetcode")             # True - "leet" + "code"
trie.can_construct("leetcodes")            # False - cannot be formed

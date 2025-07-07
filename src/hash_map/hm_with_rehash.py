"""
Rehashing process:
1. create a new array of buckets (typically 2 * the current capacity)
2. iterate through the old hash table
3. for each key-value pair, recompute the hash : new_hash = key % new_capacity
4. insert earch pair into the new array using the new index
5. discard the old array
"""

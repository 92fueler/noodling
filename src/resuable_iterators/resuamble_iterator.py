"""
OpenAI
https://aonecode.com/Interview-Question/Design-and-implement-Resumable-Iterator

Reading:
- https://instaloader.github.io/module/nodeiterator.html
- https://community.openai.com/t/issue-with-structured-outputs-returning-invalid-json-object/926409


Design the abstract class/interface

Challenge:
Create an iterator that can pause and resume its state,
extending to handle multiple files and asynchronous operations.

Key Concepts:

State Management: Implementing get_state and set_state methods.
Composite Iterators: Managing multiple iterators concurrently.
Asynchronous Programming: Utilizing coroutines for async iteration.

Followup 1:
- implement Resumable List Iterator. Write a test function that checks `set_state`
    and `get_state` work in all position and error for the end of iterator is handled.

Followup 2:
- You are provided with a JSON file iterator, implement a resumale iterator for
    reading a list of JSON files.
"""


class IteratorInterface:
    def __init__(self, object):
        pass

    def __iter__(self):
        # return an iterable object
        pass

    def __next__(self):
        # get the next item
        pass

    def get_state(self):
        # return a placeholder (state) for the current state of the iterator
        pass

    def set_state(self, state):
        # using a placeholder (state), resume the iterator from the place where the state refers to
        pass

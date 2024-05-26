
from rx.subject import Subject

class LeadQueue:
    """
    A queue that triggers a callback function whenever an item is added.
    
    Attributes:
        _subject (Subject): The RxPY Subject that handles the items.
    """
    
    def __init__(self):
        """
        Initializes the CallbackQueue with an RxPY Subject.
        """
        self._subject = Subject()

    def put(self, item):
        """
        Adds an item to the queue and triggers the callback.

        Args:
            item: The item to be added to the queue.
        """
        self._subject.on_next(item)

    def subscribe(self, callback):
        """
        Registers a callback function to be called whenever an item is added.

        Args:
            callback (function): The function to be called with the item as an argument.
        """
        self._subject.subscribe(callback)
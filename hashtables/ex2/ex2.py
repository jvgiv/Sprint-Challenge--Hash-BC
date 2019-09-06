#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in range(length):
        hash_table_insert(hashtable, tickets[ticket].source, tickets[ticket].destination)

    route[0] = (hash_table_retrieve(hashtable, "NONE"))

    for dest in range(1, length):
        start = route[dest - 1]
        route[dest] = hash_table_retrieve(hashtable, start)

    return route

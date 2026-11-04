# Assessment 3.2 - Queue
# Based on Assessment 3.1: ENONSAON
# A queue follows FIFO (First In, First Out).

from collections import deque


def main():
    letters = "ENONSAON"
    queue = deque()

    print("=== QUEUE PROGRAM ===")
    print("Enqueuing letters at the rear:")
    for letter in letters:
        queue.append(letter)
        print(f"Enqueued {letter}: {list(queue)}")

    print("\nDequeuing letters from the front:")
    while queue:
        removed = queue.popleft()
        print(f"Dequeued: {removed} | Remaining: {list(queue)}")

    print("\nQueue is empty.")


if __name__ == "__main__":
    main()

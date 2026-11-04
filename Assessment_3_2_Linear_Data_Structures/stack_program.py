# Assessment 3.2 - Stack
# Based on Assessment 3.1: ENONSAON
# A stack follows LIFO (Last In, First Out).

def main():
    letters = "ENONSAON"
    stack = []

    print("=== STACK PROGRAM ===")
    print("Pushing letters onto the stack:")
    for letter in letters:
        stack.append(letter)
        print(f"Pushed {letter}: {stack}")

    print("\nPopping letters from the stack:")
    while stack:
        removed = stack.pop()
        print(f"Popped: {removed} | Remaining: {stack}")

    print("\nStack is empty.")


if __name__ == "__main__":
    main()

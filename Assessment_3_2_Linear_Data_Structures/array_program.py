# Assessment 3.2 - Array
# Based on Assessment 3.1: ENONSAON
# An array/list removes items from the beginning in this example.

def main():
    letters = list("ENONSAON")

    print("=== ARRAY PROGRAM ===")
    print("Adding letters to the array:")
    array = []
    for letter in letters:
        array.append(letter)
        print(f"Added {letter}: {array}")

    print("\nRemoving letters from the beginning:")
    while array:
        removed = array.pop(0)
        print(f"Removed: {removed} | Remaining: {array}")

    print("\nArray is empty.")


if __name__ == "__main__":
    main()

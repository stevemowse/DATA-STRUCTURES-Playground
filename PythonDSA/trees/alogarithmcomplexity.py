def divide_conquer(cards):
    # Base case: if 0 or 1 element, return as-is (already sorted)
    if len(cards) <= 1:
        return cards

    # Create a copy to avoid modifying the original list
    sorted_cards = list(cards)
    mid = len(sorted_cards) // 2  # No need for -1

    # Recursively divide and sort left and right halves
    left = divide_conquer(sorted_cards[:mid])  # Left half
    right = divide_conquer(sorted_cards[mid:])  # Right half

    print("Left:", left, "Right:", right)  # Debugging (optional)
    return merge(left, right)  # Merge the two sorted halves

def merge(left, right):
    result = []
    i = j = 0

    # Compare and merge in descending order
    while i < len(left) and j < len(right):
        if left[i] > right[j]:  # For descending order
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
cards = [3, 1, 4, 2]
output = sorted(cards, reverse=True)  # [4, 3, 2, 1]
print(divide_conquer(cards) == output)  # True
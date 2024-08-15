def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    :param boxes: List of lists, where each inner list represents keys inside a box.
    :return: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    unlocked = [False] * n  # Initialize all boxes as locked
    unlocked[0] = True  # The first box is already unlocked
    keys = [0]  # Start with the keys from the first box

    while keys:
        current_key = keys.pop(0)  # Take the first available key
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # Only proceed if the key corresponds to a box
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add the keys from this box to the list

    return all(unlocked)


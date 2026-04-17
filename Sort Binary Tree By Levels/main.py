def tree_by_levels(node):
    if node is None:
        return []

    queue = [node]
    i = 0

    while i < len(queue):
        current = queue[i]
        i += 1

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return [m.value for m in queue]
def has_eight(board, size):
    """Return whether a padded, 1-indexed board has >=8 stones in a line."""
    for y in range(1, size + 1):
        for x in range(1, size + 1):
            color = board[y][x]
            if color not in (1, 2):
                continue
            for dy, dx in ((0, 1), (1, 0), (1, 1), (-1, 1)):
                ey, ex = y + 7 * dy, x + 7 * dx
                if 1 <= ey <= size and 1 <= ex <= size:
                    if all(board[y + k * dy][x + k * dx] == color for k in range(1, 8)):
                        return True
    return False

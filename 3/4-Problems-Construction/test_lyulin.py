def lyulin_seen(blocks):
    if len(blocks) == 0:
        return 0

    seen = 1
    current_max = blocks[0]
    
    for block in blocks:
        if block > current_max:
            seen += 1
            current_max = block
    return seen

blocks = lyulin_seen([1,2,3,4,5])
print(blocks)
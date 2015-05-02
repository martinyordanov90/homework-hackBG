def how_many_blocks_can_see(blocks):
    if len(blocks) == 0:
        return 0

    seen = 1
    current_max = blocks[0]

    for block in blocks:
        if block > current_max:
            seen += 1
            current_max = block
    return seen

result = how_many_blocks_can_see([5,4,3,2,1])
print(result)

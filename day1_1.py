total_zeros = 0

def get_data(filename):
    return (line for line in open('./{}.txt'.format(filename)))

def get_new_position(curr, instruction):
    global total_zeros
    (direction, iterations) = (instruction[0], int(instruction[1:]))
    step = 1 if direction == "R" else -1
    for i in range(iterations):
        curr += step
        if curr == 100:
            curr = 0
        elif curr == -1:
            curr = 99
    if curr == 0:
        total_zeros += 1
    return curr

curr_num = 50

for inst in get_data('day1_data'):
    curr_num = get_new_position(curr_num, inst)

print(total_zeros)
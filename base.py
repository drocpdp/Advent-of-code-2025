
def get_data(filename):
    return (line for line in open('./{}.txt'.format(filename)))
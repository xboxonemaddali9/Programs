import math
def find_next_square(sq):
    if math.sqrt(sq).is_integer() == False:
        return -1
    return (math.sqrt(sq)+1)**2

if __name__ == "__main__":
    print(find_next_square(342786627))

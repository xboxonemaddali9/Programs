def maskify(cc):
    for i in range(len(cc) - 4):
        cc = list(cc)
        cc[i] = "#"
    return ''.join(cc)


if __name__ == "__main__":
    print(maskify('5678458834'))

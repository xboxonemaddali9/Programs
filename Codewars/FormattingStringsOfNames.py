def namelist(Names):
    names = [Name['name'] for Name in Names] or ['']
    return ' & '.join([', '.join(names[:-1]), names[-1]]) if len(names) > 1 else names[0]


if __name__ == "__main__":
    print(namelist(
        [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]
    ))
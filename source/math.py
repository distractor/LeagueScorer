# compares names and returns boolean
def compareName(name1, name2):
    bIsTheSame = True
    for part in name1.split(' '):
        bIsTheSame = bIsTheSame and (name2.find(part) != -1)

    return bIsTheSame
import level2

def run(num):
    total = 0
    divider = 1
   
    addnums = []

    while divider < num:
        if num % divider == 0:
            if level2.is_prime(divider):
                total = total + divider
                addnums.append(divider)
        divider = divider+1

    return total-1

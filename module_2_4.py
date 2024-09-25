import pandas as pd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
while True:
    is_prime = True
    for i in numbers:
        if i == 1:
            numbers.remove(1)
            continue
        if i in (2, 3):
            primes.append(i)
            continue
        else:
            if (i%2 == 0) or (i%3==0):
                not_primes.append(i)
            else:
                continue
    break
new_numbers = pd.Series(numbers)
primes = new_numbers[~new_numbers.isin(pd.Series(not_primes))].tolist()

print(not_primes, primes, sep='\n')


# or 


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    print('Первое число из numbers: ', i)
    if i == 1:
        continue # numbers.remove(1) # он тогда берет второй элемент в numbers а он уже равен "3"
    if i in (2, 3):
        print(i)
        primes.append(i)
        continue
    else:
        if (i%2 == 0) or (i%3==0):
            not_primes.append(i)
        else:
            primes.append(i)
            continue
print('not_primes: ', not_primes, '\n', 'primes: ', primes)

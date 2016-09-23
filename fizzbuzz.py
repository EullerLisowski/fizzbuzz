"""
Regras do Fizzbuzz:
    1. Se a posição for multiplo de 3: fizz
    2. Se a posição for multiplo de 5: buzz
    3. Se a posição for multiplo de 3 e 5: fizzbuzz
    4. Qualquer outra posição: o próprio numero

"""

from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_3 = partial(multiple_of, 3)
multiple_of_5 = partial(multiple_of, 5)

def robot(pos):
    """
    Robot receive a number as a parameter and
    return 'fizz' if the number is multiple_of_3,
    return 'buzz' if the number is multiple_of_5,
    return 'fizzbuzz' if the number is multiple_of both
    and finally return the own number otherwise."""
    
    say = str(pos)
    
    if multiple_of_3(pos) and multiple_of_5(pos):
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'  
    elif multiple_of_3(pos):
        say = 'fizz'
 
    return say

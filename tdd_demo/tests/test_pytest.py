from scripts.inc import increment as inc
from scripts.dec import decrement as dec
import scripts.dec

from scripts.next_perm import permutate


def test_increment():
    assert inc(3) == 4

def test_decrement():
    assert dec(3) == 2

def test_range_decrement():
    for x in range(99):
        assert scripts.dec.decrement(x) == (x-1)

def test_perm_low(): 
    assert permutate('12345') == '12354'

def test_perm_high():
    assert permutate('54321') == '12345'

def test_perm_short(): 
    assert permutate('5') == '5'

def test_perm_dublet(): 
    assert permutate('12') == '21'

def test_perm_revdublet(): 
    assert permutate('21') == '12'

def test_perm_eq():
    assert permutate('3333') == '3333'

def test_perm_nan():
    assert permutate('33d33') == 'NaN'


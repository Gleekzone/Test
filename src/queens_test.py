#Test para las soluciones dadas online al problema de las n-reinas
#El test esta diseñado para n >= 8 hasta n=15
#La referencia es la tabla de soluciones del siguiente link: http://www.ic-net.or.jp/home/takaken/e/queen/

import pytest
from queens import SolutionQ

def test_8():
    
    sl = SolutionQ()
    assert sl.nqueens(8) == 92

def test_9():

    sl = SolutionQ()
    assert sl.nqueens(9) == 352

""" def test_10():

    sl = SolutionQ()
    assert sl.nqueens(10) == 724
    
def test_11():

    sl = SolutionQ()
    assert sl.nqueens(11) == 2680   

def test_12():

    sl = SolutionQ()
    assert sl.nqueens(12) == 14200    

def test_13():

    sl = SolutionQ()
    assert sl.nqueens(13) == 73712

def test_14():

    sl = SolutionQ()
    assert sl.nqueens(14) == 365596

def test_15():

    sl = SolutionQ()
    assert sl.nqueens(15) == 2279184  """   
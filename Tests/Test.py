from Library import Library as l

""" ---------------------------- LAB 01 --------------------------------"""
c1 = complex(-3,2)
c2 = complex(4,1)
c3 = complex(3,5)

def test_sum():
    assert l.sum(c1,c2)== complex(1,3), "1+3i"

def test_rest():    
    assert l.rest(c1,c2)==complex(-7,1), "-7+1i"

def test_product():
    assert l.product(c1,c2)==complex(-14,5), "-14+5i"
    
def test_division():
    assert l.division(c1,c2)==complex(-0.5882352941176471, 0.6470588235294118), "-0.5882352941176471+0.6470588235294118i"

def test_module():
    assert l.module(c1)==3.6055512754639896, "3.6055512754639896"

def test_conjugate():
    assert l.conjugate(c1)==complex(-3,-2), "-3-2i"

def test_phase():
    assert l.phase(c3)==59.04, "59.04"

def test_cartesianToPolar():
    assert l.cartesianToPolar(c3)==[5.83,59.04], "5.83,1.03"

def test_polarToCartesian():
    assert l.polarToCartesian([5.83,59.04])==[3.0,5.0], "3+5i"

test_sum()
test_rest()
test_product()
test_division()
test_module()
test_conjugate()
test_phase()
test_cartesianToPolar()
test_polarToCartesian()

""" ---------------------------- LAB 02 --------------------------------"""
def test_sumVector():
    assert l.sumVector([8+3j,-1-4j,0-9j],[8+3j,2+5j,3+0j])==[16+6j, 1+1j, 3-9j], "[[16, 6], [1, 1], [3, -9]]"

def test_inverseVector():
    assert l.inverseVector([-5+2j,3+0j,0-1j])==[5-2j,-3+0j,0+1j], "[[5, -2], [-3, 0], [0, 1]]"

def test_sumMatrix():
    assert l.sumMatrix([[-8-3j,-6-4j,0-4j],[-1+8j,6-10j,8-5j],[4+0j,8+5j,-7-9j]],[[-7-2j,-4-2j,7+7j],[5+9j,0+3j,6-5j],[1+5j,-6-6j,5+8j]])==[[-15-5j,-10-6j,7+3j], [4+17j,6-7j,14-10j], [5+5j,2-1j,-2-1j]], "[[[-15, -5], [-10, -6], [7, 3]], [[4, 17], [6, -7], [14, -10]], [[5, 5], [2, -1], [-2, -1]]]"

def test_inverseMatrix():
    assert l.inverseMatrix([[7+3j,-1+7j],[-9-4j,-7-9j]])==[[-7-3j,1-7j], [9+4j,7+9j]], "[[-7-3j,1-7j], [9+4j,7+9j]]"


def test_scalarToMatrix():
    assert l.scalarToMatrix(-2+3j, [[3-2j, 8-4j], [4-10j,-2-8j]]) == [
        [0+13j,-4+32j], [22+32j,28+10j]], "[[[0, 13], [-4, 32]], [[22, 32], [28, 10]]]"


def test_transposedMatrix():
    assert l.transposedMatrix([[3-2j,8-4j], [4-10j,-2-8j]]) == [[3-2j,4-10j], [8-4j,-2-8j]], "[[[3, -2], [4, -10]], [[8, -4], [-2, -8]]]"


def test_conjugateMatrix():
    assert l.conjugateMatrix([[-6+1j,3+8j], [2+-6j,3+0j]]) == [[-6-1j, 3-8j], [2+6j,3+0j]], "[[[-6,1],[3,8]],[[2,-6],[3,0]]]"


def test_adjoinMatrix():
    assert l.adjoinMatrix([[7+7j,3+8j,8+4j], [5+0j,8-6j,-10-1j]]) == [[7-7j, 5+0j], [3-8j,8+6j], [8-4j,-10+1j]], "[[[7, -7], [5, 0]], [[3, -8], [8, 6]], [[8, -4], [-10, 1]]]"


def test_productMatrix():
    assert l.productMatrix(
        [[-6+2j, 0+6j, 7+2j], [6+9j,7+7j,-6+-6j], [5+8j,-6+8j,6+9j]],[[9-6j,-3-4j,5-2j], [3+6j,-1-5j,0-5j], [9+9j,8-4j,-8-4j]])==[[-33+153j,120+0j,-44-22j], [87+0j,-26-117j,107+70j], [0+165j,147+26j,69-36j]], "[[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]], [[0, 165], [147, 26], [69, -36]]]"


def test_matrixOnVector():
    assert l.matrixOnVector(
        [[-1+5j,1-7j,-6+3j], [-3-9j,2-5j,1-10j], [-6+5j, 6-5j, 3-2j]],
        [1-3j,4+3j,-3+1j]) == [54-32j,0+17j,41+30j], "[[54, -32], [0, 17], [41, 30]]"


def test_normVector():
    assert l.normVector([8.8+8.6j, 3.9-6j]) == 14.23, "10.0"


def test_distanceVector():
    assert l.distanceVector([2+7j,4-1j,2-4j], [7+8j,2-8j,1+4j]) == 12.0, "12"


def test_isUnitary():
    assert l.isUnitary(
        [[0+1j,1+0j,0+0j], [0+0j,0+1j,1+0j], [1+0j,1+0j,0+1j]]) == False, "False"


def test_isHermitian():
    assert l.isHermitian(
        [[3+0j,2-1j,0-3j], [2+1j,0+0j,1-1j], [0+3j,1+1j,0+0j]]) == True, "True"


def test_tensorProduct():
    assert l.tensorProduct(
        [[1+1j,0+0j], [1+0j,0+1j]],[[-1+2j,-2-2j,0+2j], [2+3j,3+1j,2+2j], [-2+1j,1-1j,2+1j]])==[[-3+1j,0-4j,-2+2j,0+0j,0+0j,0+0j],[-1+5j,2+4j,0+4j,0+0j,0+0j,0+0j],[-3-1j,2+0j,1+3j,0+0j,0+0j,0+0j],[-1+2j,-2-2j,0+2j,-2-1j,2-2j,-2+0j],[2+3j,3+1j,2+2j,-3+2j,-1+3j,-2+2j],[-2+1j,1-1j,2+1j,-1-2j,1+1j,-1+2j]], "[[[-3, 1], [0, -4], [-2, 2], [0, 0], [0, 0], [0, 0]], [[-1, 5], [2, 4], [0, 4], [0, 0], [0, 0], [0, 0]], [[-3, -1], [2, 0], [1, 3], [0, 0], [0, 0], [0, 0]], [[-1, 2], [-2, -2], [0, 2], [-2, -1], [2, -2], [-2, 0]], [[2, 3], [3, 1], [2, 2], [-3, 2], [-1, 3], [-2, 2]], [[-2, 1], [1, -1], [2, 1], [-1, -2], [1, 1], [-1, 2]]]"


test_sumVector()
test_inverseVector()
test_sumMatrix()
test_inverseMatrix()
test_scalarToMatrix()
test_transposedMatrix()
test_conjugateMatrix()
test_adjoinMatrix()
test_productMatrix()
test_matrixOnVector()
test_normVector()
test_distanceVector()
test_isUnitary()
test_isHermitian()
test_tensorProduct()

import Lab2

def test_find_min_max():
    input=[25,30,34,32]
    result=[]
    result=Lab2.find_min_max(input)
    
    assert (result[0]== input[0] and result[1]==input[2])

def test_calc_average():
    input=[20,30]
    test=Lab2.calc_average(input)
    result=25

    assert(test==result)

def test_calc_median_temperature():
    input=[20,40,30]
    test=Lab2.calc_median_temperature(input)
    result=30
    assert(test==result)
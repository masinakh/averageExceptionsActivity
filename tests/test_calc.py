import pytest 

from average_calculator.calc import rounded_average

# @pytest.mark.skip
def test_average_of_two_numbers_is_properly_computed():
    #Arrange
    num_list = [4,6] 
    

    #Act
    actual = rounded_average(num_list)
    # Delete the skip and write the proper assertion here!
    #Assert
    assert actual == 5

def test_average_of_empty_list_raises_ValueError():
    # Delete the skip and write the test here!
    # Hint: use pytest.raises

    with pytest.raises(ValueError):
        rounded_average([])

    

   

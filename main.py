import numpy as np
from scipy.special import factorial
#Machine Epsilon manually
def get_machine_epsilon():
    epsilon = 1
    while True:
        if (epsilon + 1 <= 1):
            break
        epsilon = epsilon/2
    return 2 * epsilon 
#################################################
# Estimate the value of a e^x using the first n terms of its maclaurin expansion
def get_maclaurin_expansion_of_e_to_x_till_n_terms(x,n):
    value = 0
    for i in range(0,n):
        value += ((1/factorial(i, exact=True)) * (x**i))
    return value
#################################################
# Gets true precent relative error
def get_true_precent_relative_error(true_value, computed_value):
    return (abs(true_value - computed_value) / true_value) * 100
#################################################
# Iterates over the values of the first n terms e^x's macluarin expansion until it reaches an acceptable true precent relative error and then returns the number of terms it took to reach that acceptabe error  
def get_number_of_terms__of_e_to_x_mac_expansion(x,acceptable_error):
    e_to_x = (np.e**x)
    i = 0
    while True:
        if (get_true_precent_relative_error(e_to_x,get_maclaurin_expansion_of_e_to_x_till_n_terms(x,i)) < acceptable_error):
            return i
        i += 1
####################################################
# testing functions
def main():
    ## Machine epsilon manually
    machine_epsilon = get_machine_epsilon()
    print(machine_epsilon)
    ## Machine Epsilon from numpy
    machine_epsilon = np.finfo(np.float64).eps
    print(machine_epsilon) 
    #### 
    e_to_half_test = get_maclaurin_expansion_of_e_to_x_till_n_terms(0.5,5)
    print(e_to_half_test)
    e_to_x = (np.e**0.5)
    print(get_true_precent_relative_error(e_to_x,e_to_half_test))
    print(get_number_of_terms__of_e_to_x_mac_expansion(0.5,0.05))
#################################################
if __name__ == "__main__":
    main()


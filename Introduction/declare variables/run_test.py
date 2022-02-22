import test_declare_variables

def intro_tests():
    '''
    Run all tests for introduction module
    '''

    test_declare_variables.test_age_should_be_an_integer()
    test_declare_variables.test_age_should_be_a_positive_number()
    test_declare_variables.test_age_should_be_defined()

if __name__ == "__main__": # run tests if run file themself
    intro_tests()

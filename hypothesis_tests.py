"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
import math

def create_sample_dists(cleaned_data, y_var, categories):
    """
    Each hypothesis test will require you to create a sample distribution from your data
    Best make a repeatable function

    :param cleaned_data:
    :param y_var: The numeric variable you are comparing
    :param categories: the categories whose means you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests

    """
    htest_dfs = []
    
    # Create categories (KDN addition)
    for category in set(cleaned_data[categories]):
        sample = cleaned_data[cleaned_data[categories]==category][y_var]
        htest_dfs.append(sample)

    # Main chunk of code using t-tests or z-tests
    return htest_dfs

def compare_pval_alpha(p_val, alpha):
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status


def hypothesis_test_one(cleaned_data, alpha = 0.05):
    """
    Describe the purpose of your hypothesis test in the docstring
    These functions should be able to test different levels of alpha for the hypothesis test.
    If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

    :param alpha: the critical value of choice
    :param cleaned_data:
    :return:
    """
    # Get data for tests
    comparison_groups = create_sample_dists(cleaned_data, y_var='Pledge Rate', categories='Trust Bin')

    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    ###
    results = stats.ttest_ind(comparison_groups[0], comparison_groups[1], axis=0, equal_var=False)
    
    p_val = results[1]
    
    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our alpha of {alpha} we {status.lower()} the null hypothesis.'
          f'\n\nDue to these results, we {assertion} state that there is a difference between the pledge rate in high-trust and low-trust countries')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status
    

def hypothesis_test_two():
    pass

def hypothesis_test_three():
    pass

def hypothesis_test_four():
    pass

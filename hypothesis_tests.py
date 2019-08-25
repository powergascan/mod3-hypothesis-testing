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
from statistics import mean, stdev
from math import sqrt
from statsmodels.stats.power import TTestIndPower
import statsmodels.formula.api as smf

def create_sample_dists(df, var, size, n):
    #visualize CLT
    # - pass data in
    # - sample from without replacement
    # - take the mean and add it to a list
    # - return the sample means for plotting (KDN)
    means = []
    for i in range(n):
        means.append(df[var].sample(size,replace=False).mean())
    return means

def compare_pval_alpha(p_val, alpha=0.05):
    if p_val > alpha:
        return "Fail to reject"
    else:
        return 'Reject'

def power_analysis(coh_d, length, alpha=0.05):
    power_analyzer = TTestIndPower()
    power = power_analyzer.solve_power(effect_size=coh_d, nobs1=length, alpha=alpha)
    return power

def cohen_d(c0, c1):
    coh_d = (mean(c0) - mean(c1)) / (sqrt((stdev(c0) ** 2 + stdev(c1) ** 2) / 2))
    return coh_d

def TTest(data1, data2, Null_Statement=['Mean of A', 'Mean of B', 'equal to', ''], two_sided=True, alpha=0.05):
    """
    This is a very general TTest: One sample/ Two sample and One sided (mean A - mean B > 0) / Two sided (mean A - mean B =0 )

    :param alpha: the critical value of choice, set to 0.05
    :param data1, data2, Null_Statement (describe the null), two_sided (bool, default True)
    :return: print strings of the Null, the testing statistic, power analysis
    """
    print(f'We test the null hypothesis of H0: {Null_Statement[0]} is {Null_Statement[2]} {Null_Statement[1]}')
    assert(alpha<1)
    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    ###
    results = stats.ttest_ind(data1, data2, equal_var=False)
    # starter code for return statement and printed results
    if two_sided:
        p_val=results[1]
    else:
        p_val=results[1]/2
        
    status = compare_pval_alpha(p_val, alpha)
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"

    print(f'Based on the p value of {p_val} and our alpha of {alpha} we {status.lower()} the null hypothesis.'\
          f'\n\nDue to these results, we {assertion} {Null_Statement[3]}')

    # calculations for effect size, power, etc here as well
    coh_d= cohen_d(data1,data2)
    power=power_analysis(coh_d, min(len(data1),len(data2)), alpha=0.05)
    
    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")
    return results
    
def FTest(data, equation, Null=" ", alpha=0.05):
    
    print(f'We test the null hypothesis of H0: {Null}')
    regression = smf.ols(formula=equation, data=data).fit()
    
    p_val=regression.f_pvalue
    status = compare_pval_alpha(p_val, alpha)
    
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        
    print(f'Based on the p value of {p_val} and our alpha of {alpha} we {status.lower()} the null hypothesis.')
    
    print("---------------------")
    print("Here is the regression for you to reference")
    print("---------------------")
    print(regression.summary())
    return regression

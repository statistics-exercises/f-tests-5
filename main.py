import numpy as np
import scipy.stats

def sample_variance( data ) : 
  # Your code to calculate the sample variance from the data in 
  # the numpy array called data goes here
  
  
def testStatistic( data1, data2 ) : 
  # Your code to compute the test statistic should be inserted here.
  # Remember to use calls to sample_variance to lower the ammount of
  # code you are writing
  
def pvalue( data1, data2 ) : 
  F = testStatistic( data1, data2 )
  # Your code to calculate the  p-value given the value of the 
  # test statistic (F) should go here.
  

data1 = np.array([2.96, 1.04, 1.33, 1.51, -1.84, 1.78, 0.54, 1.82, 1.68, 0.58])
data2 = np.array([-2.07, -0.82, -0.73, -1.00, -1.77, -1.83, 0.22, 0.47, 0.14, -0.08])
print("Null hypothesis: the distributions that were sampled to generate the data in the")
print("numpy arrays data1 and data2 have the same variance")
print("Alternative hypothesis: the distribution that was sampled to generate the data in")
print("the numpy array called data1 is smaller than the variance for the distribution")
print("from which the data in data2 was generated")
print("The p-value for this hypothesis test is", pvalue( data1, data2 ) )

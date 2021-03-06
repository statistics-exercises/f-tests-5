import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_sample_var(self) :
        for i in range(5) : 
            tdata = np.random.normal(0,1,size=100)
            mu = sum(tdata) / len(tdata)
            var = (len(tdata) / (len(tdata)-1))*( sum(tdata*tdata) / len(tdata) - mu*mu )
            self.assertTrue( np.abs( var - sample_variance(tdata) )<1e-7, "Your function for calculating the sample variance is not correct" )
            
    def test_testStatistic(self) : 
        var1, var2 = sample_variance(data1), sample_variance(data2)
        self.assertTrue( np.abs( var1 / var2 - testStatistic(data1, data2))<1e-7, "your code for calculating the test statistic is not correct"  )
        self.assertTrue( self.assertFalse( np.abs( var2 / var1 - testStatistic(data1, data2))<1e-7, "The variance you have placed in the numerator of the expression for the test statistic should be in the denominator and vice versa." )
        
    def test_pvalue(self) : 
        stat = testStatistic( data1, data2 )
        pval = scipy.stats.f.cdf( stat, len(data1)-1, len(data2)-1 )
        self.assertTrue( np.abs( pvalue(data1,data2) - pval)<1e-7, "your code for calculating the p-value is not correct" )

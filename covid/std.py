import math

class Statistics:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def n(self):
        return len(self.x)
    
    @property
    def x_mean(self):
        return sum(self.x)/self.n

    @property
    def y_mean(self):
        return sum(self.y)/self.n

    @property
    def x_times_y(self):
        result = sum([couple[0]*couple[1] for couple in zip(self.x, self.y)])
        # lo que hace la comprehension: 
        # lista_en_conjunto = zip(self.x, self.y)
        # result = 0
        # for pareja in lista_en_conjunto:
        #     result += pareja[0] * pareja[1]
        return result
    
    @property
    def x_pow(self):
        result = sum([value**2 for value in self.x])
        return result

    @property
    def y_pow(self):
        result = sum([value**2 for value in self.y])
        return result

    @property
    def x_variance(self):
        divisor = sum([(num-self.x_mean)**2 for num in self.x])
        return divisor/self.n
    
    @property
    def y_variance(self):
        divisor = sum([(num-self.y_mean)**2 for num in self.y])
        return divisor/self.n
    
    @property
    def covariance(self):
        result = (self.x_times_y/self.n) - self.x_mean*self.y_mean
        return result
    
    @property
    def b(self):
        divisor = self.n*self.x_times_y - sum(self.x)*sum(self.y)
        dividend = self.n*self.x_pow - sum(self.x)**2
        return divisor/dividend

    @property
    def b_0(self):
        result = self.y_mean - self.b*self.x_mean
        return result

    @property
    def r_pearson(self):
        result = self.x_times_y / math.sqrt(self.x_pow*self.y_pow)
        return result

    def get_prediction(self, x_value):
        result = self.b*x_value + self.b_0
        return result
    

test = Statistics([1,2,3], [1,2,3])
print(test.r_pearson)




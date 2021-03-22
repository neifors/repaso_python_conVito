
class Statistics:
    def __init__(self, x , y ):
        self.x = x
        self.y = y

    @property
    def merge(self):
        return list(zip(self.x, self.y))

    @property
    def x_avg(self):
        return sum(self.x)/len(self.x)
    @property
    def y_avg(self):
        return sum(self.y)/len(self.y)

    #VARIANCE:
    @property
    def y_variance(self):
        result = 0
        n = len(self.y)
        for value in self.y:
            result += value - self.y_avg
        return result/n
    #LINEAR REGRESSION:
    @property
    def b_coeficent(self):
        n = len(self.x)
        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_x_pow_2 = sum([x**2 for x in self.x])
        sum_x_times_y = 0
        for couple in self.merge:
            sum_x_times_y += couple[0] * couple[1]
        result = ((n*sum_x_times_y)-(sum_x*sum_y))/((n*sum_x_pow_2)-(sum_x)**2)
        return result
    @property
    def order_b_coeficent(self):
        return self.y_avg - self.b_coeficent*self.x_avg
    def direct_regression(self, score):
        return self.b_coeficent * score + self.order_b_coeficent
        

data_1 = Statistics([1,2,13],[1,1,2])
print(data_1.y_variance)
from math import sqrt
class Dea():
    
    def __init__(self, x, y, id_code, address):
        self.x = float(x)
        self.y = float(y)
        self.id = id_code
        self.address = address
        
    
    def get_distance(self,x_user,y_user):
        leg1 = abs(x_user - self.x)
        leg2 = abs(y_user - self.y)
        distance = sqrt(leg1**2 + leg2**2)
        return distance
        
from random import choice

class RandomWalk():
    
    def __init__(self, num_points=5000):
        
        self.num_points = num_points
        
        self.x_values = [0]
        self.y_values = [0]
        
        
        
    def get_step(self):
        
        x_direction = choice([1])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
          
            
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return x_direction * x_distance, y_direction * y_distance
    
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            
            x_step, y_step = self.get_step()
           
        
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
        
            if x_step == 0 and y_step == 0:
                continue
                
            self.x_values.append(x)
            self.y_values.append(y)  
    
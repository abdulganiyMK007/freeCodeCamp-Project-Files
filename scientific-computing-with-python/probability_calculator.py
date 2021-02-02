import random
import copy

class Hat:
    contents = []
    
    def __init__(self, **kwargs):
            self.contents = []
            self.list = []
            for key, value in kwargs.items():
                #print ("%s == %s" %(key, value))
                for i in range(value):
                    self.contents.append(key)
            #print("contents:", self.contents)
            
            
    def draw(self, nBalls):
        list = []
        if nBalls > len(self.contents):
            list = self.contents
            self.contents = []
        else:
            for i in range(nBalls):
                r = random.randrange(0, len(self.contents))
                list.append(self.contents.pop(r))
            
        return list
        
############################   
        

# hat
# expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. F
# num_balls_drawn: The number of balls to draw out of the hat in each experiment.

# num_experiments: The number of experiments to perform.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        if (isDrawn(expected_balls, drawn_balls)):
            count += 1
        
    return count/num_experiments

    
def isDrawn(expected_balls, drawn_balls):
    
    set_of_drawn_balls = set(drawn_balls)
    for aBall in expected_balls:
        if (aBall in set_of_drawn_balls):
            drawn_balls.remove(aBall)
            set_of_drawn_balls = set(drawn_balls)
        else:
            return False
    return True   



import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        contents=[]
        for item in kwargs:
            for i in range(kwargs[item]):
                contents.append(item)
        self.contents=contents
    def draw(self,number):
        draw_balls=[]
        if number >= len(self.contents):
            draw_balls=self.contents
            return draw_balls
        for i in range(number):
            ball=random.choice(self.contents)
            self.contents.remove(ball)
            draw_balls.append(ball)
        return draw_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count=0
    #a for loop according to the numbers of experiments
    for i in range(num_experiments):
        #copying all the balls in the hat
        balls_in_hat=copy.deepcopy(hat)
        #drawing balls for an experiment
        drawn_balls=balls_in_hat.draw(num_balls_drawn)
        # making a dictionary for drawn balls to comparing to expected balls later
        balls_dic={}
        for i in range(len(drawn_balls)):
            if drawn_balls[i] in balls_dic:
                balls_dic[drawn_balls[i]] +=1
            else:
                balls_dic[drawn_balls[i]] = 1
        #checking for number of all expected ball appeared in drawn balls and incrementing the counter
        if all(key in balls_dic and balls_dic[key] >= value for key,value in expected_balls.items()):
            count += 1
    probability = count/num_experiments
    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)


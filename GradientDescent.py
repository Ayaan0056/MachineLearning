import numpy as np

# n stands for length of x array
# m_curr is the slope 
# c_curr is the y-intercept 

def gradient_descent(x,y):
    iterations = 1000
    n = len(x)  
    m_curr = c_curr = 0  
    learning_rate = 0.001

    for i in range(iterations):
        y_predicted = m_curr * x + c_curr
        
        cost = (1/n) * sum([j**2 for j in (y - y_predicted)])

        m_derivative = -(2/n) * sum(x*(y-y_predicted))
        c_derivative = -(2/n) * sum(y-y_predicted)

        m_curr = m_curr - learning_rate * m_derivative
        c_curr = c_curr - learning_rate * c_derivative

        print(" Slope m:{} , y-Intercept c:{} , Cost Function:{} , Iterations: {} ".format(m_curr,c_curr,cost,i))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)
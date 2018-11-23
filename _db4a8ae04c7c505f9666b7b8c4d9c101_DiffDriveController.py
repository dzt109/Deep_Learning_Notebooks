class DiffDriveController():
    """
    Class used for controlling the robot linear and angular velocity
    """
    def __init__(self, max_speed, max_omega):
        # TODO for Student: Specify these parameters
        self.kp=1.0
        self.ka=2.0
        self.kb=-1.0
        self.MAX_SPEED = np.float(max_speed)
        self.MAX_OMEGA = np.float(max_omega)
        
    def compute_vel(self, state, goal):
        """
        Function that computes the desired outputs given the state and goal
        Inputs:
        state - a numpy vector of size 3 by 1 with components (x,y,theta)
        goal - a numpy vector of size 2 by 1 specifying the location of the goal
        Outputs: a tuple with 3 elements
        v - a number specifying the forward speed (in m/s) of the robot (should 
            be no more than max_speed)
        omega - a number specifying the angular velocity (in rad/s) of the robot
            (should be no more than max_omega)
        done - a boolean value specifying if the robot has reached its goal (or
            is close enough
        """
        # YOUR CODE HERE
        x = state[0]
        y = state[1]
        theta = state[2]

        gx = goal[0]
        gy = goal[1]

        dx = gx - x
        dy = gy - y
        rho = np.sqrt(dx**2 + dy**2)
        alpha = -theta + atan2(dy,dx)
        beta = -theta - alpha

        A = np.matrix([[self.kp,0,0],[0,self.ka,self.kb]])

        vw = A*(np.array([rho,alpha,beta])[:,None])
        v = vw[0,0]
        w = vw[1,0]

        done = True if ((rho<0.01) and (abs(alpha) <0.01 ) and (abs(beta<0.01)) else False
        
        return (min(self.MAX_SPEED,v),min(self.MAX_OMEGA,w),done)
        #return (v,w,done)
        pass

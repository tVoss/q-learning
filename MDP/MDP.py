import math
import random

class MDP:

    def __init__(self,
                 ball_x=None,
                 ball_y=None,
                 velocity_x=None,
                 velocity_y=None,
                 paddle_y=None):
        '''
        Setup MDP with the initial values provided.
        '''
        self.create_state(
            ball_x=ball_x,
            ball_y=ball_y,
            velocity_x=velocity_x,
            velocity_y=velocity_y,
            paddle_y=paddle_y
        )

        # the agent can choose between 3 actions - stay, up or down respectively.
        self.actions = [0, 0.04, -0.04]


    def create_state(self,
              ball_x=None,
              ball_y=None,
              velocity_x=None,
              velocity_y=None,
              paddle_y=None):
        '''
        Helper function for the initializer. Initialize member variables with provided or default values.
        '''
        self.paddle_height = 0.2
        self.ball_x = ball_x if ball_x != None else 0.5
        self.ball_y = ball_y if ball_y != None else 0.5
        self.velocity_x = velocity_x if velocity_x != None else 0.03
        self.velocity_y = velocity_y if velocity_y != None else 0.01
        self.paddle_y = 0.5

    def simulate_one_time_step(self, action_selected):
        '''
        :param action_selected - Current action to execute.
        Perform the action on the current continuous state.
        '''

        # Do action
        self.paddle_y += self.actions[action_selected]

        self.paddle_y = max(0, min(1 - self.paddle_height, self.paddle_y))

        # Move ball
        self.ball_x += self.velocity_x
        self.ball_y += self.velocity_y

        # Bounce off top wall
        if self.ball_y < 0:
            self.ball_y = -self.ball_y
            self.velocity_y = -self.velocity_y

        # Bounce off bottom wall
        if self.ball_y > 1:
            self.ball_y = 2-self.ball_y
            self.velocity_y = -self.velocity_y

        # Bounce off left wall
        if self.ball_x < 0:
            self.ball_x = -self.ball_x
            self.velocity_x = -self.velocity_x

        # Ball is not at right wall
        if self.ball_x < 1:
            return 0

        # Miss
        if (self.ball_y < self.paddle_y or self.ball_y > self.paddle_y + self.paddle_height):
            return -1

        # Hit paddle
        self.ball_x = 2-self.ball_x
        self.velocity_x = -self.velocity_x + random.uniform(-0.015, 0.015)
        if abs(self.velocity_x) < 0.3:
            self.velocity_x = abs(self.velocity_x)/self.velocity_x * 0.03
        self.velocity_x = max(-1, min(1, self.velocity_x))
        self.velocity_y = self.velocity_y + random.uniform(-0.03, 0.03)
        self.velocity_y = max(-1, min(1, self.velocity_y))

        return 1

    def discretize_state(self):
        # Special state for failure
        if (self.ball_x >= 1): return (12, 0, 0, 0, 0)

        ball_x = int(math.floor(self.ball_x * 12))
        ball_y = int(math.floor(self.ball_y * 12))
        velocity_x = int(abs(self.velocity_x) / self.velocity_x)
        velocity_y = int(0 if abs(self.velocity_y) < 0.015 else abs(self.velocity_y) / self.velocity_y)
        paddle_y = int(11 if self.paddle_y == 1 - self.paddle_height else math.floor(12 * self.paddle_y / (1 - self.paddle_height)))

        return (ball_x, ball_y, velocity_x, velocity_y, paddle_y)

import random

from MDP.MDP import MDP
from Q.Q import Q

class Simulator:

    def __init__(self, num_games=0, alpha_value=0, gamma_value=0, epsilon_value=0):
        '''
        Setup the Simulator with the provided values.
        :param num_games - number of games to be trained on.
        :param alpha_value - 1/alpha_value is the decay constant.
        :param gamma_value - Discount Factor.
        :param epsilon_value - Probability value for the epsilon-greedy approach.
        '''
        self.num_games = num_games
        self.epsilon_value = epsilon_value
        self.alpha_value = alpha_value
        self.gamma_value = gamma_value

        # Your Code Goes Here!
        self.q = Q()
        self.mdp = MDP()
        self.iteration = 0

        self.train_agent()

    def f_function(self, state):
        '''
        Choose action based on an epsilon greedy approach
        :return action selected
        '''
        actions = self.q.get_actions(state)

        if random.random() < self.epsilon_value:
            rand = random.randint(0, 2)
            return actions[rand], rand

        return max(actions), actions.index(max(actions))

    def train_agent(self):
        '''
        Train the agent over a certain number of games.
        '''
        print 'Training agent for ', self.num_games, ' trials'
        hits = []
        for x in range(1, self.num_games + 1):
            self.iteration = x
            hits.append(self.play_game())
            self.mdp = MDP()
            if x % 1000 == 0:
                print 'Averaging ', sum(hits)/len(hits), ' hit(s) by game ', x
                hits = []

        print 'Training done! Testing agent over 5 games'
        avg = 0.0
        for x in range(5):
            avg += self.play_game() / 5.0
            self.mdp = MDP()

        print 'Average hits over 5 games: ', avg

    def play_game(self):
        '''
        Simulate an actual game till the agent loses.
        '''
        hits = 0

        while True:
            # Get current state and an action
            state = self.mdp.discretize_state()

            value, action = self.f_function(state)

            # Simulate
            reward = self.mdp.simulate_one_time_step(action)

            # Gather information about the new state
            new_state = self.mdp.discretize_state()
            future_value, _ = self.f_function(new_state)

            # Estimate new value
            new_value = value + self.alpha_value * (reward + self.gamma_value * future_value - value)

            self.q.set(action, state, new_value)

            # Missed
            if reward == -1:
                return hits

            hits += reward

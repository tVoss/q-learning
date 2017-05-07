from Simulator.simulator import Simulator

if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    '''
    alpha_value = 0.5
    gamma_value = 0.8
    epsilon_value = 0.05
    num_games = 100000
    Simulator(num_games, alpha_value, gamma_value, epsilon_value)

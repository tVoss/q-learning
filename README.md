This readme serves to give an overview of the flow of the MP.

runner.py
	- Setup the required parameters and start Simulation.

Simulator
	- The broad tasks of the Simulator are to train the agent and then test it on a real game.
	- During the training phase, the agent must learn the optimal parameters to ensure as many bounces as possible.
	- Training will be done over a certain number of games so you must modular code that allows you to reuse the same code game over game.
	- For testing, use the parameters learnt on an actualy pong game. Keep playing till the agent loses and track the bounces.

MDP
	- Sets up the Markov Decision Process that includes states, actions, (refer to the documentation for more details).
	- Performs actions on states for example, moves the paddle up and the ball in a certain direction.
	- Keeps track of 2 kinds of states - continuous and discrete.
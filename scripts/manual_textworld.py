import gym
import torch
import textworld.gym
from textworld import EnvInfos, text_utils

env_options = textworld.EnvInfos(facts=True, intermediate_reward = True, admissible_commands=True, last_action = True, game = True, description=True, entities=True, extras=["recipe","walkthrough"])

env_id = textworld.gym.register_game("../twgames/home_theme/new/new_game_test.ulx", env_options)
env = gym.make(env_id)  # Start the environment.

obs, infos = env.reset()  # Start new episode.
env.render()

score, moves, done = 0, 0, False
while not done:
    command = input("> ")
    obs, score, done, infos = env.step(command)
    print(infos['extra.walkthrough'],infos['admissible_commands'])
    print(score, infos['intermediate_reward'])
    env.render()
    moves += 1

env.close()
print("moves: {}; score: {}".format(moves, score))
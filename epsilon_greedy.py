from arm import Arm
import random
import numpy as np


def mean(values):
    return sum(values)*1.0/len(values)

class EpsilonGreedyAlgorithm(object):

    def __init__(self, arms, epsilon):
        self.epsilon = epsilon
        self.arms = arms
        self.values = [[] for i in arms]

    def select_arm(self):
        if random.random() > self.epsilon:
            arm_idx = self.get_best_arm_idx()
        else:
            arm_idx = self.get_random_arm_idx()

        arm = self.arms[arm_idx]
        reward = arm.pull()
        self.update(arm_idx, reward)

    def update(self, arm_idx, reward):
        self.values[arm_idx].append(reward)

    def get_best_arm_idx(self):
        max_yhat = 0.0
        max_idx = None
        for i, values in enumerate(self.values):
            yhat = 0.0 if len(values) == 0 else mean(values)
            if yhat > max_yhat:
                max_yhat = yhat
                max_idx = i

        if max_idx is None:
            return self.get_random_arm_idx()
        else:
            return max_idx

    def get_random_arm_idx(self):
        return random.randrange(len(self.arms))


if __name__=="__main__":
    for epsilon in np.linspace(0, 1, 200):
        losses = []
        for j in range(500):
            ps = [random.random() for i in range(random.randrange(2, 8))]
            arms = [Arm(p) for p in ps]
            algo = EpsilonGreedyAlgorithm(arms, epsilon=epsilon)
            for i in range(100):
                algo.select_arm()
            total_reward = 0
            for i, vals in enumerate(algo.values):
                total_reward += sum(vals)

            #
            optimal = max(ps) * 100.0
            loss = optimal - total_reward
            losses.append(loss)

        print "mean:", np.mean(losses), "\t var:", np.var(losses), "\t epsilon:", epsilon
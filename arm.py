
from random import random


class Arm(object):

    def __init__(self, p):
        """
        Represents an arm in the Multi-armed bandit model.

        :param p: probability of payout.
        """
        self.p = p

    def pull(self):
        """
        Exploit arm to get payout
        :return: payout
        """
        return 1 if random() < self.p else 0


if __name__ == "__main__":
    arm_one = Arm(0.5)
    arm_two = Arm(0.2)
    payouts_from_arm_one = [arm_one.pull() for i in range(10)]
    payouts_from_arm_two = [arm_two.pull() for i in range(10)]
    print sum(payouts_from_arm_one)*1.0 / len(payouts_from_arm_one)
    print sum(payouts_from_arm_two)*1.0 / len(payouts_from_arm_two)

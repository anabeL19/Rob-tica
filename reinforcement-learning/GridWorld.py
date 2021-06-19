import numpy as np

class Grid: # Environment
  def __init__(self, width, height, start):
    self.width = width
    self.height = height
    self.i = start[0]
    self.j = start[1]

  def set(self, rewards, actions):
    # rewards should be a dict of: (i, j): r (row, col): reward
    # actions should be a dict of: (i, j): A (row, col): list of possible actions
    self.rewards = rewards
    self.actions = actions

  def set_state(self, s):
    self.i = s[0]
    self.j = s[1]

  def current_state(self):
    return (self.i, self.j)

  def move(self, action):
    if action in self.actions[(self.i, self.j)]:
      if action == 'U':
        self.i -= 1
      elif action == 'D':
        self.i += 1
      elif action == 'R':
        self.j += 1
      elif action == 'L':
        self.j -= 1
    return self.rewards.get((self.i, self.j), 0)

  def all_states(self):
    return set(self.actions.keys()) | set(self.rewards.keys())


def standard_grid():
  '''
  define a grid that describes the reward for arriving at each state
  and possible actions at each state
  the grid looks like this
  x means you can't go there
  s means start position
  number means reward at that state
  .  .  .  1
  .  x  . -1
  s  .  .  .
  '''
  g = Grid(4, 4, (2, 2))
  rewards = {
    (1, 0): -5, 
    (2, 3): 5,
  }
  actions = {
    (0, 0): ('R'),
    (0, 1): ('L', 'R'),
    (0, 2): ('L', 'R'),
    (0, 3): ('L', 'D'),
    (1, 0): ('R', 'D'),
    (1, 1): ('L', 'R', 'D'),
    (1, 2): ('L', 'R', 'D'),
    (1, 3): ('L', 'U', 'D'),
    (2, 0): ('U', 'D', 'R'),
    (2, 1): ('U', 'L', 'R'),
    (2, 2): ('U', 'L', 'R'),
    (2, 3): ('U', 'L'),
    (3, 0): ('U', 'R'),
    (3, 1): ('L', 'R'),
    (3, 2): ('L', 'R'),
    (3, 2): ('L'),
  }
  g.set(rewards, actions)
  return g


def rest_grid(step_cost=-1):
  g = standard_grid()
  g.rewards.update({
    (0, 0): step_cost,
    (0, 1): step_cost,
    (0, 2): step_cost,
    (0, 3): step_cost,
    (1, 0): step_cost,
    (1, 1): step_cost,
    (1, 2): step_cost,
    (1, 3): step_cost,
    (2, 0): step_cost,
    (2, 1): step_cost,
    (2, 2): step_cost,
    (2, 3): step_cost,
    (3, 0): step_cost,
    (3, 1): step_cost,
    (3, 2): step_cost,
    (3, 3): step_cost,
  })
  return g


def print_values(V, g):
  for i in range(g.width):
    print("---------------------------")
    for j in range(g.height):
      v = V.get((i,j), 0)
      if v >= 0:
        print(" %.2f|" % v, end="")
      else:
        print("%.2f|" % v, end="") # -ve sign takes up an extra space
    print("")


def print_policy(P, g):
  for i in range(g.width):
    print("---------------------------")
    for j in range(g.height):
      a = P.get((i,j), ' ')
      print("  %s  |" % a, end="")
    print("")
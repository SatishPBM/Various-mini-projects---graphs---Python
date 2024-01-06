# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:34:00 2020

@author: s_pot
"""


def compute_rss(y_estimate, y):
  return sum(np.power(y-y_estimate, 2))

def estimate_y(x, b_0, b_1):
  return b_0 + b_1 * x


n = 100
beta_0 = 5
beta_1 = 2
np.random.seed(1)

rss = compute_rss(estimate_y(x, beta_0, beta_1), y) 
print(rss)
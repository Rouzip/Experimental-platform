#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 17:09:43 2018

@author: yz
"""

import threading


class Server:

    def __init__(self):
        self.weights = None    # what to fill in here
        self.num_samples = 0
        self.lock = threading.Lock()

    # 更新总权重，使用线程锁保持权重每次独立运算
    def update_weights(self, num_samples, weights):
        with self.lock:
            self.num_samples += num_samples
            for sw, w in zip(self.weights, weights):
                sw += num_samples * w

    def get_weights(self):
        with self.lock:
            if self.num_samples == 0:
                return self.weights

            for w in self.weights:
                w /= self.num_samples

            self.num_samples = 0
            return self.weights

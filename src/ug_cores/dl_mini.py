"""Tiny MLP from scratch (numpy) — UG Deep Learning mini."""
from __future__ import annotations

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -30, 30)))


def train_xor(epochs: int = 2000, lr: float = 0.5, seed: int = 0):
    rng = np.random.default_rng(seed)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([[0], [1], [1], [0]], dtype=float)
    W1 = rng.normal(scale=0.5, size=(2, 4))
    b1 = np.zeros((1, 4))
    W2 = rng.normal(scale=0.5, size=(4, 1))
    b2 = np.zeros((1, 1))
    for _ in range(epochs):
        h = sigmoid(X @ W1 + b1)
        o = sigmoid(h @ W2 + b2)
        err = o - y
        dW2 = h.T @ (err * o * (1 - o))
        db2 = np.sum(err * o * (1 - o), axis=0, keepdims=True)
        dh = (err * o * (1 - o)) @ W2.T
        dW1 = X.T @ (dh * h * (1 - h))
        db1 = np.sum(dh * h * (1 - h), axis=0, keepdims=True)
        W2 -= lr * dW2
        b2 -= lr * db2
        W1 -= lr * dW1
        b1 -= lr * db1
    pred = (sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2) > 0.5).astype(int)
    acc = float(np.mean(pred == y))
    return {"xor_accuracy": acc}

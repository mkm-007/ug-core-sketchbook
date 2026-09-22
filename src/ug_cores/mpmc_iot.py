"""Register-style GPIO bit simulation (MPMC / IoT mini)."""
from __future__ import annotations


class GpioBank:
    def __init__(self):
        self.reg = 0  # 8-bit

    def set_bit(self, bit: int) -> None:
        self.reg |= 1 << bit

    def clear_bit(self, bit: int) -> None:
        self.reg &= ~(1 << bit)

    def read_bit(self, bit: int) -> int:
        return (self.reg >> bit) & 1

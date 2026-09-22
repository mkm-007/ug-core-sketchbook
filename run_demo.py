#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from ug_cores import dsa, dbms, dl_mini, ml_classic, mpmc_iot, networks


def main():
    print("UG core sketchbook demos")
    print("DSA mergesort:", dsa.mergesort([3, 1, 2]))
    print("ML logistic:", ml_classic.run_logistic_demo())
    print("DL XOR MLP:", dl_mini.train_xor())
    print("Networks ARQ:", networks.stop_and_wait())
    print("DBMS:", dbms.demo_db())
    bank = mpmc_iot.GpioBank()
    bank.set_bit(2)
    print("MPMC GPIO bit2:", bank.read_bit(2), "reg=", bin(bank.reg))


if __name__ == "__main__":
    main()

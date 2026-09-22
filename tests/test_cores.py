import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ug_cores import dsa, dbms, dl_mini, ml_classic, mpmc_iot, networks


def test_dsa():
    assert dsa.mergesort([3, 1, 2]) == [1, 2, 3]
    assert dsa.binary_search([1, 2, 3], 2) == 1


def test_ml():
    assert ml_classic.run_logistic_demo()["accuracy"] >= 0.7


def test_dl():
    assert dl_mini.train_xor(epochs=3000)["xor_accuracy"] >= 0.75


def test_net():
    st = networks.stop_and_wait(n_frames=10, loss=0.1)
    assert st.delivered == 10


def test_dbms():
    assert dbms.demo_db()["rows"][0][0] == "Ada"


def test_gpio():
    g = mpmc_iot.GpioBank()
    g.set_bit(1)
    assert g.read_bit(1) == 1
    g.clear_bit(1)
    assert g.read_bit(1) == 0

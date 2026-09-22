"""Stop-and-wait ARQ simulation."""
from __future__ import annotations

from dataclasses import dataclass
import random


@dataclass
class Stats:
    sent: int = 0
    delivered: int = 0
    retransmits: int = 0


def stop_and_wait(n_frames: int = 20, loss: float = 0.2, seed: int = 0) -> Stats:
    rng = random.Random(seed)
    st = Stats()
    seq = 0
    delivered = 0
    while delivered < n_frames:
        st.sent += 1
        # send
        if rng.random() < loss:
            st.retransmits += 1
            continue
        # ACK may also drop
        if rng.random() < loss:
            st.retransmits += 1
            continue
        delivered += 1
        st.delivered += 1
        seq ^= 1
    return st

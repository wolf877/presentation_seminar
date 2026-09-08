from topology.run_topology import run_topology
import numpy as np

run_topology(
        topology='E1',
        l_max=5,
        Lx=1.0,
        Ly=1.0,
        Lz=1.0,
        beta=90,
        alpha=90,
        gamma=0,
        do_polarization=False,
        normalize=True,
        l_range=np.array([[2, 5]]),
        lp_range=np.array([[2, 5]])
    )

print("Example 1 completed.\n")
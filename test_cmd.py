from topology.run_topology import run_topology
import numpy as np

run_topology(
    topology='E1',
    l_max=30,
    Lx=1.0, Ly=1.0, Lz=1.0,
    beta=90, alpha=90,
    x0 = np.array([0.1, 0.2, 0.3]),
    do_polarization=False,
    normalize=True,
)
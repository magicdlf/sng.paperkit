# Notation

| Symbol | Description | Unit |
| --- | --- | --- |
| $t$ | time | day |

Table: Notation used throughout this paper {#tbl:notation}

Each trace was processed in four steps. The swing axis was found by projecting x and y onto the direction that maximises spectral power at the oscillation frequency, rather than the axis of greatest variance, since the release transient contributes large off-axis excursions. The release instant was located as the point of maximum speed and the following 0.45 s discarded. The usable window was ended where the trace stops moving, identifying frames where the tracker had locked onto a stationary feature. The remainder was fitted to ₀ x(t) = A e^(−γt) cos(ωt + φ) + c + dt by non-linear least squares over the whole trace, rather than by picking peaks and fitting a

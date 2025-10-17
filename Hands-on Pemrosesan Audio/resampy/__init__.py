import numpy as np
from scipy.signal import resample_poly


def resample(x, sr_orig, sr_new, filter="kaiser_best", axis=-1):
    """
    Minimal stub of resampy.resample for environments without the real package.
    Falls back to scipy.signal.resample_poly.
    """
    if sr_orig == sr_new:
        return x

    sr_orig = int(sr_orig)
    sr_new = int(sr_new)
    gcd = int(np.gcd(sr_new, sr_orig))
    up = sr_new // gcd
    down = sr_orig // gcd
    return resample_poly(x, up, down, axis=axis)


__all__ = ["resample"]

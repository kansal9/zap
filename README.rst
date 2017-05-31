ZAP2 (the Zurich Atmosphere Purge reloaded)
-------------------------------------------

Tired of sky subtraction residuals? ZAP them!

This repository is a fork of the original zap_, developed by Kurt Soto. The
differences with the original software are listed below.

ZAP is a high precision sky subtraction tool which can be used as complete sky
subtraction solution, or as an enhancement to previously sky-subtracted MUSE
data.  The method uses PCA to isolate the residual sky subtraction features and
remove them from the observed datacube. Future developments will include
modification for use on a variety of instruments.

..
    The last stable release of ZAP can be installed simply with::
        pip install zap2
    Or into the user path with::
        pip install --user zap2


Links
~~~~~

- Documentation :
  `zap.readthedocs.org <http://zap.readthedocs.io/en/latest/>`_

- Git repository (report issues, etc.) : https://git-cral.univ-lyon1.fr/MUSE/zap2

Changes
~~~~~~~

- Addition of a new method for the continuum filter, using a polynomial fit
  (``cftype='fit'``). This uses ``numpy.polyfit``, which is parallelized
  internally, with a polynomial of degree 5.

- The PCA is now done with *scikit-learn* (`sklearn.decomposition.PCA`_). This
  solved a major issue with spatial variations introduced by zap. Also it is
  much faster than the previous implementation. A drawback however is that it
  is no more possible to save the SVD file, it could be added back if needed.

- By default there is now only one *sky segment*, which means that the cube is
  no more split on the wavelength axis. Originally zap used 11 segments, whose
  goals were to have coherent groups of sky emission lines, with a smaller
  number of eigenvalues per segment. And it also allowed to parallelize the
  computation. But, the segments were also responsible for weird continuum
  oscillations, and made the choice of the number of eigenvalues per segment
  very difficult and very sensitive. With only one segment the performance of
  the sky subtraction is much better, thanks to the higher correlation between
  sky lines on the whole wavelength range.

  It is still possible to modify the sky segments::

    import zap
    zap.SKYSEG[:] = [0, 5400, ..., 10000]


Citation
~~~~~~~~

The paper describing the original method can be found here:
http://adsabs.harvard.edu/abs/2016MNRAS.458.3210S

Please cite ZAP as::

\bibitem[Soto et al.(2016)]{2016MNRAS.458.3210S} Soto, K.~T., Lilly, S.~J., Bacon, R., Richard, J., \& Conseil, S.\ 2016, \mnras, 458, 3210

.. _zap: https://github.com/ktsoto/zap
.. _sklearn.decomposition.PCA: http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA

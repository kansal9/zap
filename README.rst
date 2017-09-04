ZAP (the Zurich Atmosphere Purge reloaded)
-------------------------------------------

Tired of sky subtraction residuals? ZAP them!

This repository is a fork of the original zap_, developed by Kurt Soto. The
differences with the original software are listed in the changelog_. This
version is also compatible with the AO mode.

ZAP is a high precision sky subtraction tool which can be used as complete sky
subtraction solution, or as an enhancement to previously sky-subtracted MUSE
data.  The method uses PCA to isolate the residual sky subtraction features and
remove them from the observed datacube. Future developments will include
modification for use on a variety of instruments.

..
    The last stable release of ZAP can be installed simply with::
        pip install zap
    Or into the user path with::
        pip install --user zap


Links
~~~~~

- `documentation <http://zap.readthedocs.io/en/latest/>`_

- `git repository <https://github.com/musevlt/zap>`_

- changelog_

Citation
~~~~~~~~

The paper describing the original method can be found here:
http://adsabs.harvard.edu/abs/2016MNRAS.458.3210S

Please cite ZAP as::

\bibitem[Soto et al.(2016)]{2016MNRAS.458.3210S} Soto, K.~T., Lilly, S.~J., Bacon, R., Richard, J., \& Conseil, S.\ 2016, \mnras, 458, 3210

.. _zap: https://github.com/ktsoto/zap
.. _changelog: https://github.com/musevlt/zap/blob/master/CHANGELOG
.. _sklearn.decomposition.PCA: http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA

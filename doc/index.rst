================================
Welcome to ZAP2's documentation!
================================

.. toctree::
   :maxdepth: 2

Tired of sky subtraction residuals? ZAP them!

ZAP2 (the *Zurich Atmosphere Purge*) is a high precision sky subtraction tool
which can be used as complete sky subtraction solution, or as an enhancement to
previously sky-subtracted MUSE integral field spectroscopic data.  The method
uses PCA to isolate the residual sky subtraction features and remove them from
the observed datacube. Though the operation of ZAP2 is not dependent on perfect
flatfielding of the data in a MUSE exposure, better results are obtained when
these corrections are made ahead of time. Future development will include
expansion to more instruments.

Installation
============

Requirements
------------

ZAP2 requires the following packages:

* Numpy 1.6.0 or later
* Astropy v1.0 or later
* SciPy v0.13.3 or later
* Scikit-learn

Many linear algebra operations are performed in ZAP2, so it can be beneficial to
use an alternative BLAS package. In the Anaconda distribution, the default BLAS
comes with Numpy linked to MKL, which can amount to a 20% speedup of ZAP2.

..
    Steps
    -----
    ZAP2 can be installed using pip ::
        pip install zap2


Usage
=====

In its most hands-off form, ZAP2 can take an input FITS datacube, operate on it,
and output a final FITS datacube. The main function to do this is
`zap2.process`::

    import zap2
    zap2.process('INPUT.fits', outcubefits='OUTPUT.fits')

Care should be taken, however, since this case assumes a sparse field, and
better results can be obtained by applying masks.

There are a number of options that can be passed to the code which we describe
here:

Sparse Field Case
-----------------

This case specifically refers to the case where the sky can be measured in the
sky frame itself, using::

    zap2.process('INPUT.fits', outcubefits='OUTPUT.fits')

In both cases, the code will create a resulting processed datacube named
``DATACUBE_ZAP.fits`` in the current directory. While this can work well in the
case of very faint sources, masks can improve the results.

For the sparse field case, a mask file can be included, which is a 2D FITS
image matching the spatial dimensions of the input datacube. Masks are defined
to be >= 1 on astronomical sources and 0 at the position of the sky. Set this
parameter with the ``mask`` keyword ::

    zap2.process('INPUT.fits', outcubefits='OUTPUT.fits', mask='mask.fits')

Filled Field Case
-----------------

This approach also can address the saturated field case and is robust in the
case of strong emission lines, in this case the input is an offset sky
observation. To achieve this, we calculate the SVD on an external sky frame
using the function `zap2.SVDoutput`.

An example of running the code in this way is as follows::

    extSVD = zap2.SVDoutput('Offset_Field_CUBE.fits', mask='mask.fits')
    zap2.process('Source_cube.fits', outcubefits='OUTPUT.fits', extSVD=extSVD)

The integration time of this frame does not need to be the same as the object
exposure, but rather just a 2-3 minute exposure.


Command Line Interface
======================

ZAP2 can also be used from the command line::

    python -m zap2 INPUT_CUBE.fits

More information use of the command line interface can be found with the
command ::

    python -m zap2 -h


Interactive mode
================

ZAP2 can also  be used interactively from within IPython ::

    import zap2
    zobj = zap2.process('INPUT.fits', interactive=True)

The run method operates on the datacube, and retains all of the data and methods
necessary to process a final data cube in a Python class named `~zap2.Zap`. You
can elect to investigate the data product via the `~zap2.Zap` object, and even
reprocess the cube with a different number of eigenspectra per region.
A workflow may go as follows:

.. code-block:: python

  import zap2
  from matplotlib import pyplot as plt

  # allow ZAP2 to run the optimize routine
  zobj = zap2.process('INPUT.fits', interactive=True)

  # plot the variance curves and the selection of the number of eigenspectra used
  zobj.plotvarcurve()

  # plot a spectrum extracted from the original cube
  plt.figure()
  plt.plot(zobj.cube[:,50:100,50:100].sum(axis=(1,2)), 'b', alpha=0.3)

  # plot a spectrum of the cleaned ZAP2 dataproduct
  plt.plot(zobj.cleancube[:,50:100,50:100].sum(axis=(1,2)), 'g')

  # choose just the first 3 spectra for all segments
  zobj.reprocess(nevals=3)

  # plot a spectrum extracted from the original cube
  plt.plot(zobj.cube[:,50:100,50:100].sum(axis=(1,2)), 'b', alpha=0.3)

  # plot a spectrum of the cleaned ZAP2 dataproduct
  plt.plot(zobj.cleancube[:,50:100,50:100].sum(axis=(1,2))), 'g')

  # choose some number of modes by hand
  zobj.reprocess(nevals=[2,5,2,4,6,7,9,8,5,3,5])

  # plot a spectrum
  plt.plot(zobj.cleancube[:,50:100,50:100].sum(axis=(1,2))), 'k')

  # Use the optimization algorithm to identify the best number of modes per segment
  zobj.optimize()

  # compare to the previous versions
  plt.plot(zobj.cleancube[:,50:100,50:100].sum(axis=(1,2))), 'r')

  # identify a pixel in the dispersion axis that shows a residual feature in
  # the original
  plt.figure()
  plt.matshow(zobj.cube[2903,:,:])

  # compare this to the zap2 dataproduct
  plt.figure()
  plt.matshow(zobj.cleancube[2903,:,:])

  # write the processed cube as a single extension FITS
  zobj.writecube('DATACUBE_ZAP.fits')

  # or merge the zap2 datacube into the original input datacube, replacing the
  # data extension
  zobj.writefits(outcubefits='DATACUBE_FINAL_ZAP.fits')

Changelog
=========

.. include:: ../CHANGELOG

API
===

.. autofunction:: zap2.process

.. autofunction:: zap2.SVDoutput

.. autofunction:: zap2.nancleanfits

.. autofunction:: zap2.contsubfits

.. autofunction:: zap2.wmedian

.. autoclass:: zap2.Zap
   :members:

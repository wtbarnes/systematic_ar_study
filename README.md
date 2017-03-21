# systematic_ar_study
The `synthesizAR` package can be used for forward modeling of active regions whose evolution is determined primarily by hydrodynamic simulations of coronal loops. In this study, we want to look at one (or several) AR for a number of different heating functions. Then, we will perform some sort of observational diagnostic on the forward-modeled emission, likely an emission measure reconstruction for selected pixels or a selected group of pixels. By comparing such diagnostics to observations, we can then place constraints on the heating properties.

## Magnetic Field
[Warren et al. (2012)][warren2012] conducted a study of 15 ARs in which they perform an EM analysis on each AR using data from SDO/AIA and Hinode/EIS. We will use this paper as a guide for selecting an AR from which we will extrapolated the magnetic field lines. 

Below is a table of a few candidate ARs from the aforementioned paper. Ideally, we would like to select a very bipolar AR.

| NOAA no. | Date | Center coordinates [arcsec] |
|:--------:|:----:|:------------------:|
| 1109 | 2010 Sep 29 23:51:36 | 361.5, 261.5 |
| 1193 | 2011 Apr 19 13:32:20 | 36.3, 363.5 |


## Heating
As a first pass, we want to look at three different heating frequencies: low-frequency, intermediate-frequency, and high-frequency. Note that low, intermediate, and high are all relative to the loop cooling time.

May want to explore "sandpile" model of Klimchuk and Lopez-Fuentes as well. 

## Emission
We will configure an emission model based on the lines selected by [Warren et al. (2012)][warren2012] as seen in Table 2 of their paper. 

## Observational Diagnostics

[warren2012]: http://adsabs.harvard.edu/abs/2012ApJ...759..141W
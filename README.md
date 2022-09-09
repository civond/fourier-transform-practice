<h1>Fourier Transform Practice</h1>
<div>Please refer to fourierTransform-example1.py to follow along (figures generated in matplotlib.</div><br>

<h2>Creating the signal</h2>
<div>First, we perform a wave convolution using a signal of 50Hz and 120 Hz. Then, we use numpy to introduce random noise into the waveform. This will look like the image below.</div>
<img src="figures/noisySignal.png"></img><br><br>

<h2>Fourier Transform and Filtering</h2>
<div>The next step is to apply a fourier transform using rfft() because we are only interested in the real component of the signal (= faster processesing time!).</div>
<img src="figures/fourierTransform.png"></img><br>

<div>Next, we filter the transformation so that any values under 300 units will be set to zero. The noise will be filtered out and will only leave peaks at 50Hz and 120Hz.</div>
<img src="figures/fourierTransform_filtered.png"></img><br><br>

<h2>Inverse Fourier Transform</h2>
Finally, we then apply a inverse Fourier transform to the transformation, which will retun the signal to its original state, without the noise!
<img src="figures/filteredSignal.png"></img>
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft,rfftfreq,irfft

fig_dir="figures/"
plt.rcParams['figure.figsize'] = [16,10]
plt.rcParams.update({'font.size':18})

#Create a simple signal with two frequencies
data_step = 0.001
t = np.arange(start=0,stop=1,step=data_step)
f_clean = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t) #50 and 120 Hz
f_noise = f_clean + 2.5*np.random.randn(len(t)) #introduce random noise into signal

plt.plot(t, f_noise, color='c', label='Noisy')
plt.plot(t, f_clean, color='k', label='Clean')
plt.legend()
#plt.show() #xaxis = time
plt.savefig(fig_dir+'noisySignal.png')

plt.clf()
n = len(t)
yf = rfft(f_noise)
xf = rfftfreq(n,data_step)
plt.plot(xf,np.abs(yf))
plt.savefig(fig_dir+'fourierTransform.png')
#plt.show() #note that 50 and 120 Hz are our starting frequencies.

plt.clf()
yf_abs = np.abs(yf)
indices = yf_abs>300  # filter out those value under 300 (in other words, filter out yf_abs values under 300)
yf_clean = indices * yf # noise frequency will be set to 0
plt.plot(xf,np.abs(yf_clean))
plt.savefig(fig_dir+'fourierTransform_filtered.png')
#plt.show()
plt.clf()

new_f_clean = irfft(yf_clean)
plt.plot(t,new_f_clean)
plt.ylim(-6,8)
plt.savefig(fig_dir+'filteredSignal.png')
#plt.show()
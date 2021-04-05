import numpy as np
import matplotlib.pyplot as plt


def make_signal(n, freqs):
    t = np.linspace(0, 1, n)
    y = np.zeros_like(t)
    for freq in freqs:
        y += np.sin(freq * np.pi * t)
    return {'t': t, 'y': y}


def extract_samples(signal, part=0.1):
    n = signal['t'].size
    m = int(part * n)
    idx = np.random.choice(n, m, replace=False) # choose from n, m times
    idx.sort()
    return {'t': signal['t'][idx].copy(),
            'y': signal['y'][idx].copy(),
            'idx': idx}

signal = make_signal(n=1000, freqs=[8, 80])
x = signal['t']
y = signal['y']
signal_sub = extract_samples(signal)
x1 = [x[z] for z in signal_sub['idx']]
y1 = [y[z] for z in signal_sub['idx']]


fig, axs = plt.subplots(2)
axs[0].set_title('signal + samples')
axs[0].plot(x,y)
axs[0].plot(x1, y1,'*')
axs[0].legend(['signal','samples'])
axs[1].set_title('si + connected samples')
axs[1].plot(x,y)
axs[1].plot(x1, y1)
axs[1].legend(['signal','connected samples'])
plt.show()

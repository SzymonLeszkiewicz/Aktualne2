import numpy as np
import matplotlib.pyplot as plt
import cvxpy
import scipy.fftpack as spfft

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
axs[1].set_title('si + naive representation')
axs[1].plot(x,y)
axs[1].plot(x1, y1)
axs[1].legend(['signal','connected samples'])
plt.show()

def reconstruct(signal_sub, t_target):
  n = t_target.size
  A = spfft.idct(np.identity(n), norm = 'ortho', axis =0)
  A = A[signal_sub['idx']]

  vx = cvxpy.Variable(n)
  cvxpy.Problem(objective=cvxpy.Minimize(cvxpy.norm(vx, 1)), constraints=[A@vx == signal_sub['y']]).solve()

  x = np.array(vx.value)
  return {'t': t_target, 'y': spfft.idct(x, norm='ortho', axis=0)}

signal_rec = reconstruct(signal_sub, signal['t'])
t1 = signal_rec['t']
y1 = signal_rec['y']
plt.plot(t1, y1)
plt.plot(x, y)
plt.show()

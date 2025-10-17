import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from pathlib import Path

sr = 22050
T = 2.0
samples = int(sr * T)

# Generate sine + noise
t = np.linspace(0, T, samples, endpoint=False)
signal = 0.6 * np.sin(2 * np.pi * 440 * t)
noise = 0.3 * np.random.randn(samples)
mask = (t > 1.0).astype(float)
signal = signal + noise * mask

n_fft = 1024
hop_length = 256
S = np.abs(librosa.stft(signal, n_fft=n_fft, hop_length=hop_length))
S_db = librosa.amplitude_to_db(S, ref=np.max)

fig, ax = plt.subplots(figsize=(10, 4))
img = librosa.display.specshow(S_db, x_axis='time', y_axis='hz', sr=sr, hop_length=hop_length, ax=ax)
ax.set_title('Contoh Spectrogram dengan Noise')
plt.colorbar(img, ax=ax, format='%+2.0f dB')

# Highlight noise region
ax.axvspan(1.0, T, color='white', alpha=0.15)
ax.text(1.05, sr / 8, 'Area noise/tekstur acak', color='white', fontsize=10,
        bbox=dict(boxstyle='round', facecolor='black', alpha=0.6))

Path('output').mkdir(exist_ok=True)
file_path = Path('output/spectrogram_noise_example.png')
plt.tight_layout()
plt.savefig(file_path, dpi=150)
print(file_path)

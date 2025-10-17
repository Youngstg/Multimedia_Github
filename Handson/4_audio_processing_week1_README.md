# 4_audio_processing_week1.ipynb

## Cell 1 – Setup & Imports
- **Kode:** Mengimpor pustaka audio (`librosa`, `soundfile`), numerik (`numpy`, `scipy`), dan visualisasi (`matplotlib`), melengkapi dengan utilitas IPython, `os`, serta `warnings`. Gaya `matplotlib` disetel agar grafis konsisten dan warning dinonaktifkan.
- **Output:** Versi pustaka terdeteksi (Librosa 0.11.0, NumPy 2.2.6, SciPy 1.15.3, Matplotlib 3.10.6) sehingga lingkungan siap untuk eksperimen.

## Cell 3 – Audio Loading Recap
- **Kode:** Menentukan path `data/audio.wav`, memuat audio tanpa mengubah sample rate, menyediakan fallback ketika file tidak tersedia, mengubah ke mono `float32`, dan menampilkan statistik dasar serta waveform.
- **Output:** File berdurasi 63.73 detik pada 24 kHz dengan 1,529,543 sampel, rentang amplitudo -1.0 s.d. 1.0, RMS 0.116, serta plot dan pemutar audio yang memverifikasi sinyal.

## Cell 5 – Resampling Demonstration
- **Kode:** Menetapkan target 16 kHz, melakukan resampling dengan `librosa.resample` (anti-aliasing) dan `scipy.signal.resample`, membandingkan ukuran hasil, mem-plot waveform asli vs hasil, dan menyediakan audio comparison. Hasil `y_16k` disimpan untuk sel berikutnya.
- **Output:** Downsampling 24 kHz -> 16 kHz menghasilkan 1,019,696 sampel (63.73 detik) pada kedua metode; waveform hampir identik dan audio 16 kHz terdengar stabil.

## Cell 6 – Aliasing Check
- **Kode:** Membuat sinyal sintetis berfrekuensi 2 kHz, 10 kHz, dan 15 kHz, melakukan decimation naive versus resampling dengan anti-aliasing, mem-plot STFT dan waveform untuk membedakan artefak, serta menyediakan perbandingan audio.
- **Output:** Komponen di atas 8 kHz terlipat ke pita rendah pada downsampling naive, sedangkan pipeline librosa meredamnya; plot spektrogram memperlihatkan aliasing hanya pada metode naive.

## Cell 8 – Butterworth Filtering
- **Kode:** Mengambil `y_16k`, merancang filter Butterworth order 4 (low-pass 3 kHz, high-pass 300 Hz, band-pass 300–3,000 Hz), menerapkannya dengan `filtfilt`, mem-plot waveform dan spectrogram masing-masing, serta memutar audio hasil.
- **Output:** Tiap filter memotong rentang sesuai target: low-pass menenangkan high-end, high-pass membersihkan low-end, band-pass memusatkan midrange. Audio player menegaskan perubahan tonal.

## Cell 9 – Frequency Response Analysis
- **Kode:** Menggunakan `scipy.signal.freqz` dengan grid logaritmik untuk menghitung magnitude dan fase tiap filter, memplot respons bersama garis cutoff, serta menghitung energi sinyal sebelum dan sesudah filtering.
- **Output:** Low-pass turun ~3 dB di 3 kHz, high-pass bertahan di atas 300 Hz, band-pass menonjolkan pita 300–3,000 Hz. Energi tersisa: low-pass 98.8%, high-pass 52.6%, band-pass 53.3%.

## Cell 10 – Practical EQ Scenarios
- **Kode:** Membangun chain rumble removal (high-pass 80 Hz), vocal isolation (band-pass 85–4,000 Hz), dan notch 50 Hz. Fungsi helper membuat waveform + spectrogram per skenario, kemudian dihitung distribusi energi spektral dan disediakan audio perbandingan.
- **Output:** Rumble removal menaikkan centroid ke 1,524.2 Hz dan menurunkan energi low ke 15.9%; band-pass vokal memusatkan energi mid (82.2%) dan menurunkan centroid ke 891.6 Hz. Suara terdengar lebih bersih dan fokus.

## Cell 11 – Custom 4-Band EQ
- **Kode:** Mendefinisikan gain -3/+2/+4/-1 dB untuk low sampai high, mengaplikasikan filter bertingkat per band, menormalisasi untuk mencegah clipping, lalu membandingkan waveform, spectrogram, dan magnitude response. Analisis spektral memakai utilitas sebelumnya.
- **Output:** Distribusi energi bergeser ke mid (88.6%) dengan penurunan low ke 9.4%. Plot menunjukkan penekanan bass dan penguatan presence, selaras dengan perbedaan audio sebelum-sesudah.

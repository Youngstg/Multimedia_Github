# 5_audio_processing_week2.ipynb

## Cell 1 – Environment Setup
- **Kode:** Memastikan `pyloudnorm` dan `pydub` tersedia, mengimpor seluruh pustaka audio, numerik, dan plotting, menonaktifkan warning, serta menyetel style `matplotlib`.
- **Output:** Versi pustaka (Librosa 0.11.0, NumPy 2.2.6, SciPy 1.15.3, Matplotlib 3.10.6, SoundFile 0.13.1) dikonfirmasi sehingga eksperimen loudness dapat direproduksi.

## Cell 4 – Baseline Stats
- **Kode:** Memuat `audio.wav` pada sample rate asli, mengubah ke mono `float32`, menghitung peak dan RMS (linear dan dBFS), serta mem-plot waveform dengan referensi peak/RMS.
- **Output:** Audio berdurasi 63.73 detik (24 kHz, 1,529,543 sampel) dengan peak 0.00 dBFS dan RMS -18.69 dBFS; plot dan widget audio memastikan materi siap diproses.

## Cell 6 – Loudness Reference
- **Kode:** Menginisialisasi `pyln.Meter` dan menghitung loudness terintegrasi.
- **Output:** Nilai baseline -19.04 LUFS menjadi acuan sebelum normalisasi.

## Cells 9–10 – Gain Control
- **Kode:** Cell 9 mendefinisikan helper peak/RMS/LUFS dan melakukan penyesuaian gain +8 dB dengan guard clipping; Cell 10 memvisualisasikan waveform penuh dan zoom, menampilkan delta metrik, dan menyediakan pemutar audio.
- **Output:** Peak tetap 0 dBFS, namun RMS naik dari -18.69 ke -11.04 dBFS dan LUFS dari -19.04 ke -11.42. Waveform dan audio menunjukkan peningkatan loudness tanpa distorsi.

## Cells 12–13 – Fade In/Out Profiles
- **Kode:** Cell 12 memuat audio lalu membuat fungsi fade linear dan eksponensial (alpha 3.0) dengan durasi 2 detik; Cell 13 mem-plot waveform 6 detik pertama, menampilkan envelope gain, dan menyediakan audio asli vs linear vs eksponensial.
- **Output:** Fade eksponensial bergerak lambat di awal dan cepat di akhir, berbeda dengan linear yang simetris; perbedaan terdengar jelas melalui pemutar audio.

## Cell 15 – Crossfade Dua Lagu
- **Kode:** Memuat `audio.wav` dan `artorias.wav`, menyeragamkan sample rate, membuat fungsi crossfade linear 1 detik, dan menghitung timing transisi.
- **Output:** Crossfade 1.00 detik (24,000 sampel) terjadi pada 62.73–63.73 detik dengan durasi gabungan 102.20 detik; audio hasil menunjukkan transisi halus.

## Cells 17–19 – Kompresor Dinamis
- **Kode:** Cell 17 mengimplementasikan kompresor attack/release berbasis envelope; Cell 18 menerapkannya pada audio; Cell 19 memplot waveform original vs compressed dan menyediakan perbandingan audio.
- **Output:** Plot memperlihatkan puncak lebih rata dan audio terdengar lebih terkendali tanpa perubahan drastis pada karakter.

## Cells 21–23 – Limiter vs Compressor
- **Kode:** Cell 21 mendefinisikan limiter peak, Cell 22 menerapkan kompresor dan limiter ambang -20 dB, Cell 23 memplot perbandingan, menghitung peak/RMS/LUFS, lalu menampilkan audio beserta catatan interpretasi.
- **Output:** Kompresor menghasilkan peak -3.75 dBFS (LUFS -23.71) sedangkan limiter menahan peak hingga -14.12 dBFS (LUFS -27.66); grafik menunjukkan limiter lebih agresif dan audio menegaskan perbedaan.

## Cells 25–27 – Noise Gate
- **Kode:** Cell 25 membangun fungsi noise gate dengan attack/hold/release, Cell 26 menerapkannya (threshold -25 dB), dan Cell 27 memplot waveform, envelope, zoom detail, menghitung persentase gate, serta menyiapkan audio sebelum-sesudah.
- **Output:** Gate terbuka 90.0% dan tertutup 10.0%; noise latar berkurang pada bagian hening sesuai plot dan audio.

## Cells 29–31 – Silence Detection
- **Kode:** Cell 29 mendefinisikan `detect_silence` berbasis RMS frame, Cell 30 menjalankannya (threshold -20 dB, durasi minimal 0.5 s), Cell 31 menampilkan daftar interval, mem-plot highlight, dan menghitung statistik durasi hening.
- **Output:** Terdeteksi 10 segmen >=0.5 s (total 6.19 detik atau 9.7% durasi); waveform dengan highlight membantu mengidentifikasi area untuk editing.

## Cells 33–35 – Auto-Trimming Silence
- **Kode:** Cell 33 mengimplementasikan `auto_trim_silence` dengan padding opsional, Cell 34 menjalankannya (threshold -30 dB, padding 0 ms), Cell 35 mem-print ringkasan durasi, mem-plot waveform original vs trimmed, dan menyediakan audio perbandingan.
- **Output:** Audio dipangkas 0.41 detik (0.21 s di awal, 0.20 s di akhir) sehingga durasi menjadi 63.32 detik; plot overlay dan audio menunjukkan hanya bagian hening yang dihapus.

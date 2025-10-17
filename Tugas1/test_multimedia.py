import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import moviepy.editor as mp
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def test_general_purpose():
    """Test library general purpose: numpy, pandas"""
    print("=" * 50)
    print("1. TESTING GENERAL PURPOSE LIBRARIES")
    print("=" * 50)
    
    # Test NumPy
    print("\nTesting NumPy...")
    try:
        arr = np.random.rand(5, 3)
        print(f"NumPy array shape: {arr.shape}")
        print(f"Array mean: {arr.mean():.4f}")
        print(f"Array max: {arr.max():.4f}")
        result = np.dot(arr, arr.T)
        print(f"Matrix multiplication result shape: {result.shape}")
    except Exception as e:
        print(f"NumPy test failed: {e}")
        return False
    
    # Test Pandas
    print("\nTesting Pandas...")
    try:
        data = {
            'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
            'age': [25, 30, 35, 28, 32],
            'city': ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Yogyakarta'],
            'salary': [5000000, 7500000, 6000000, 5500000, 8000000]
        }
        df = pd.DataFrame(data)
        print(f"DataFrame created with shape: {df.shape}")
        print(f"Average age: {df['age'].mean():.1f}")
        print(f"Average salary: Rp {df['salary'].mean():,.0f}")
        df.groupby('city').agg({'age': 'mean', 'salary': 'sum'})
        print("Group by operations completed")
    except Exception as e:
        print(f"Pandas test failed: {e}")
        return False
    
    print("General Purpose libraries test PASSED")
    return True

def test_audio_processing():
    """Test library audio processing: librosa, soundfile, scipy"""
    print("\n" + "=" * 50)
    print("2. TESTING AUDIO PROCESSING LIBRARIES")
    print("=" * 50)
    
    try:
        import librosa
        import soundfile as sf
        from scipy import signal
        from scipy.io import wavfile
        print("All audio libraries imported successfully")
    except ImportError as e:
        print(f"Audio library import failed: {e}")
        return False
    
    print("\nTesting Audio Processing...")
    try:
        sample_rate = 22050
        duration = 2
        t = np.linspace(0, duration, int(sample_rate * duration), False)
        frequencies = [440, 554.37, 659.25]
        audio_signal = np.sum([np.sin(2 * np.pi * freq * t) for freq in frequencies], axis=0)
        audio_signal = audio_signal / len(frequencies)
        
        print(f"Generated audio signal: {len(audio_signal)} samples at {sample_rate} Hz")
        spectral_centroids = librosa.feature.spectral_centroid(y=audio_signal, sr=sample_rate)[0]
        print(f"Spectral centroid calculated: mean = {np.mean(spectral_centroids):.2f} Hz")
        mfccs = librosa.feature.mfcc(y=audio_signal, sr=sample_rate, n_mfcc=13)
        print(f"MFCC features extracted: shape {mfccs.shape}")
        chroma = librosa.feature.chroma_stft(y=audio_signal, sr=sample_rate)
        print(f"Chroma features extracted: shape {chroma.shape}")
        
        nyquist = sample_rate / 2
        low_freq = 1000 / nyquist
        b, a = signal.butter(4, low_freq, btype='low')
        signal.filtfilt(b, a, audio_signal)
        print("Applied low-pass filter (cutoff: 1000 Hz)")
        
        fft = np.fft.fft(audio_signal)
        freqs = np.fft.fftfreq(len(fft), 1/sample_rate)
        dominant_freq = freqs[np.argmax(np.abs(fft[:len(fft)//2]))]
        print(f"FFT analysis: dominant frequency ≈ {dominant_freq:.1f} Hz")
        print("SoundFile library available for audio I/O operations")
    except Exception as e:
        print(f"Audio processing test failed: {e}")
        return False
    
    print("Audio Processing libraries test PASSED")
    return True

def test_image_processing():
    """Test library image processing: opencv, pillow, scikit-image, matplotlib"""
    print("\n" + "=" * 50)
    print("3. TESTING IMAGE PROCESSING LIBRARIES")
    print("=" * 50)
    
    try:
        import cv2
        from PIL import Image
        from skimage import filters, feature, measure
        print("All image processing libraries imported successfully")
    except ImportError as e:
        print(f"Image processing library import failed: {e}")
        return False
    
    print("\nTesting Image Processing...")
    try:
        img_size = (200, 200, 3)
        synthetic_img = np.random.randint(0, 255, img_size, dtype=np.uint8)
        cv2.rectangle(synthetic_img, (50, 50), (150, 100), (255, 0, 0), -1)
        cv2.circle(synthetic_img, (100, 150), 30, (0, 255, 0), -1)
        print(f"Created synthetic image: {synthetic_img.shape}")
        
        gray_cv = cv2.cvtColor(synthetic_img, cv2.COLOR_BGR2GRAY)
        cv2.Canny(gray_cv, 50, 150)
        print("OpenCV: Converted to grayscale and detected edges")
        
        cv2.GaussianBlur(synthetic_img, (15, 15), 0)
        print("OpenCV: Applied Gaussian blur")
        
        pil_img = Image.fromarray(cv2.cvtColor(synthetic_img, cv2.COLOR_BGR2RGB))
        pil_img.resize((100, 100))
        pil_img.rotate(45)
        print("PIL: Resized to (100, 100) and rotated 45°")
        
        gray_ski = cv2.cvtColor(synthetic_img, cv2.COLOR_BGR2GRAY)
        feature.canny(gray_ski, sigma=1)
        print("Scikit-image: Canny edge detection")
        filters.gaussian(gray_ski, sigma=2)
        print("Scikit-image: Gaussian filter applied")
        
        binary = gray_ski > 100
        labeled_img = measure.label(binary)
        props = measure.regionprops(labeled_img)
        print(f"Scikit-image: Found {len(props)} regions in binary image")
        
        fig, axes = plt.subplots(2, 2, figsize=(10, 8))
        axes[0, 0].imshow(cv2.cvtColor(synthetic_img, cv2.COLOR_BGR2RGB))
        axes[0, 0].set_title('Original Image')
        axes[0, 1].imshow(gray_cv, cmap='gray')
        axes[0, 1].set_title('Grayscale')
        axes[1, 0].imshow(cv2.Canny(gray_cv, 50, 150), cmap='gray')
        axes[1, 0].set_title('Edges (OpenCV)')
        axes[1, 1].imshow(filters.gaussian(gray_ski, sigma=2), cmap='gray')
        axes[1, 1].set_title('Gaussian Filter (Scikit-image)')
        for ax in axes.flat:
            ax.axis('off')
        plt.tight_layout()
        plt.close()
        print("Matplotlib: Created image processing visualization")
    except Exception as e:
        print(f"Image processing test failed: {e}")
        return False
    
    print("Image Processing libraries test PASSED")
    return True

def test_video_processing():
    """Test library video processing: moviepy"""
    print("\n" + "=" * 50)
    print("4. TESTING VIDEO PROCESSING LIBRARIES")
    print("=" * 50)
    
    try:
        from moviepy.editor import VideoClip, ColorClip, concatenate_videoclips
        from moviepy.video.fx.all import resize
        import cv2
        print("MoviePy imported successfully")
    except ImportError as e:
        print(f"Video processing library import failed: {e}")
        return False
    
    print("\nTesting Video Processing...")
    try:
        def make_frame1(t):
            brightness = int(128 + 127 * np.sin(2 * np.pi * t))
            return np.full((100, 100, 3), [brightness, 0, 0], dtype=np.uint8)
        
        def make_frame2(t):
            frame = np.full((100, 100, 3), [0, 0, 100], dtype=np.uint8)
            x = int(50 + 30 * np.sin(4 * np.pi * t))
            y = int(50 + 30 * np.cos(4 * np.pi * t))
            cv2.circle(frame, (x, y), 10, (255, 255, 255), -1)
            return frame
        
        clip1 = VideoClip(make_frame1, duration=2).set_fps(24)
        clip2 = VideoClip(make_frame2, duration=2).set_fps(24)
        print("Created synthetic video clips (2 seconds each at 24 fps)")
        
        resized_clip = resize(clip1, 0.5)
        print("Resized video clip to 50%")
        
        final_clip = concatenate_videoclips([clip1, clip2])
        print(f"Concatenated clips: total duration = {final_clip.duration} seconds")
        
        ColorClip(size=(100, 100), color=(0, 255, 0), duration=1)
        print("Created solid color clip (green, 1 second)")
        
        print("Final clip properties:")
        print(f"  - Size: {final_clip.size}")
        print(f"  - Duration: {final_clip.duration} seconds")
        print(f"  - FPS: {final_clip.fps}")
        
        clip1.close()
        clip2.close()
        final_clip.close()
        resized_clip.close()
    except Exception as e:
        print(f"Video processing test failed: {e}")
        return False
    
    print("Video Processing libraries test PASSED")
    return True

def main():
    print("STARTING COMPREHENSIVE LIBRARY TEST")
    print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python Version: {sys.version}")
    
    results = []
    results.append(("General Purpose", test_general_purpose()))
    results.append(("Audio Processing", test_audio_processing()))
    results.append(("Image Processing", test_image_processing()))
    results.append(("Video Processing", test_video_processing()))
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    for category, result in results:
        status = "PASSED" if result else "FAILED"
        print(f"{category:20} : {status}")
        if result:
            passed += 1
    
    print(f"\nOVERALL RESULT: {passed}/{total} tests passed")
    if passed == total:
        print("ALL TESTS PASSED! Your libraries are working correctly.")
    else:
        print("Some tests failed. Please check the error messages above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

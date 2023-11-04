import numpy as np
import librosa

def noise(data):
    if data.size == 0:
        # Handle the case when data is empty
        return data
    
    noise_amp = 0.035*np.random.uniform()*np.amax(data)
    data = data + noise_amp*np.random.normal(size=data.shape[0])
    return data

def stretch(data, rate=0.8):
    return librosa.effects.time_stretch(data, rate=0.8)

def shift(data):
    shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
    return np.roll(data, shift_range)

def pitch(data, sampling_rate, pitch_factor=0.7):
    return librosa.effects.pitch_shift(data, sr=sampling_rate, n_steps=pitch_factor)

def extract_features(data, sample_rate):
    # # ZCR
    result = np.array([])
    # zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    # result=np.hstack((result, zcr)) # stacking horizontally

    # #Chroma_stft
    # stft = np.abs(librosa.stft(data))
    # chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    # result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally

    # # Root Mean Square Value
    # rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    # result = np.hstack((result, rms)) # stacking horizontally

    # # MelSpectogram
    # mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    # result = np.hstack((result, mel)) # stacking horizontally
    
    #spectral centroid
    # spec_cent=np.mean(librosa.feature.spectral_centroid(y=data, sr=sample_rate).T, axis=0)
    # result = np.hstack((result, spec_cent)) # stacking horizontally
    
    #spectral contrast
    S = np.abs(librosa.stft(data))
    contrast = np.mean(librosa.feature.spectral_contrast(S=S, sr=sample_rate).T, axis=0)
    result = np.hstack((result, contrast)) # stacking horizontally
    
    # #spectral flux
    # onset_env =np.mean( librosa.onset.onset_strength(sr=sample_rate, S=librosa.amplitude_to_db(data, ref=np.max)))
    # result=np.hstack((result,onset_env))
    
    # #mler
    # Mler=mler(rms)
    # result=np.hstack((result,Mler))
    
    # #chroma_sens
    # chroma_cens = np.mean(librosa.feature.chroma_cens(y=data, sr=sample_rate))
    # result=np.hstack((result,chroma_cens))
    
    
    #entropy
    
   # ee=np.round(ent.spectral_entropy(data, sf=100, method='fft'), 2)
    #result=np.np.hstack((result,ee))
    #rmse
    #Rmse=rmse(data)
   # result=np.hstack((result,rmse))
    #spectral roll off
    # spec_rolloff = np.mean(librosa.feature.spectral_rolloff(x, sr=sample_rate)[0])
    # result=np.hstack((result,spec_rolloff))
    
    
    
    
    
    
    
    
    
    
    
    return result

def get_features(path):
    # duration and offset are used to take care of the no audio in start and the ending of each audio files as seen above.
    data, sample_rate = librosa.load(path, duration=2.5, offset=0.6)
    
    # without augmentation
    res1 = extract_features(data,sample_rate)
    result = np.array(res1)
    
    # data with noise
    noise_data = noise(data)
    res2 = extract_features(noise_data,sample_rate)
    result = np.vstack((result, res2)) # stacking vertically
    
    # data with stretching and pitching
    new_data = stretch(data)
    data_stretch_pitch = pitch(new_data, sample_rate)
    res3 = extract_features(data_stretch_pitch, sample_rate)
    # result = np.array(res3)
    result = np.vstack((result, res3)) # stacking vertically
    
    return result
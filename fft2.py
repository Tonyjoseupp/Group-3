import wave
import struct
import numpy
import glob


VECTORIZED_MAGNITUDE = numpy.vectorize(lambda x: x.real**2 + x.imag**2)  #!

def EFreq(fname):
    ((_, _, framerate, total_frames, _, _), wav_data) = wavLoad(fname)  #LHS has a tuple inside another ..1. params  2. waveframes
    nframes = int(framerate / 20)
    frequency_spacing = float(framerate) / nframes
    Flist = []

    for i in range(nframes, total_frames, nframes):
        fft = numpy.fft.fft(wav_data[(i - nframes):i])    
        frequency_magnitudes = VECTORIZED_MAGNITUDE(fft)
        estimated_index = FMaxIndx(frequency_magnitudes[1: nframes/2])
        estimated_frequency = (estimated_index + 1) * frequency_spacing	
        Flist.append(estimated_frequency)
    return Flist

def wavLoad(fname):  # fname is name of a sound file
    wav = wave.open(fname, "r")     
    params = (nchannels, sampwidth,_, nframes,_,_) = wav.getparams()  #loads different parameters of a sound file
    frames = wav.readframes(nframes * nchannels)    #reads listed number of frames
    fmt = "%dB" % (nframes * nchannels) if sampwidth == 1 else "%dH" % (nframes * nchannels) # 'a' if 'condition' else 'b'   # %d is replaced by (nframes * nchannels)

    return (params, struct.unpack_from(fmt, frames)) # returns a fixed number of frames along with a tuple-params containing sound parameters

def FMaxIndx(array):
    m = max(array)
    return [i for i, j in enumerate(array) if j == m][0]

###
files = glob.glob('/home/malu/Downloads/PROJECT/*')   #globing all filenames together -as a single list
l = []
for pth in files:
	
	name = pth.split('/')[5]  #take filename ..ie string followed after 5th '/'
	data = EFreq(pth) 		# estimate freq of 5th string segment
	l.append(name)		# append name of file and estimated Flist 
	l.append(data)		#name is a string , data is the list(frequencie)
	
with open('fft_freq.txt', 'w') as f:    # use instead of f=open('fname','w') and f.close()
	for item in l:			#write name of file first, data list secondly, everything in new lines

		f.write("%s\n" % item)

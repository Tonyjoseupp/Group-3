

import wave
from pydub import AudioSegment
import glob
length= 7.000000000

files = glob.glob('/home/dell/Desktop/Project/PDb/*')

for pth in files:	
	f = wave.open(pth, 'r')
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames / float(rate)
	f.close()
	dur = length - duration
	pad_ms = dur*1000
	silence = AudioSegment.silent(duration=pad_ms)
	audio = AudioSegment.from_wav(pth)

	padded = audio + silence 
	padded.export('/home/dell/Desktop/Project/PDc/'+ pth[31: ], format='wav')
	






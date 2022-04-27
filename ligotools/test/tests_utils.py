import os
import json
import pytest
import numpy as np

from ligotools import readligo as rl
from ligotools import utils as ut

def test_write_wavfile():
	wav_path = "/home/jovyan/Homework/hw06-midoripierce/data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
	assert os.path.isfile(wav_path)

def test_whiten():
	fn_H1 = "/home/jovyan/Homework/hw06-midoripierce/data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')

	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 4096, NFFT = 4*4096)
	psd_H1 = interp1d(freqs, Pxx_H1)
	dt = time_H1[1] - time_H1[0]

	strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
	assert len(strain_H1_whiten) == 131072

def test_reqshift():
	fn_H1 = "/home/jovyan/Homework/hw06-midoripierce/data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')

	Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 4096, NFFT = 4*4096)
	psd_H1 = interp1d(freqs, Pxx_H1)
	dt = time_H1[1] - time_H1[0]

	strain_H1_whiten = ut.whiten(strain_H1,psd_H1,dt)
	strain_H1_shifted = ut.reqshift(strain_H1_whiten,fshift=400,sample_rate=4096)
	assert assert len(strain_H1_whiten) == 131072 
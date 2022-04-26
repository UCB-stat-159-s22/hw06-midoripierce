import os
import json
import pytest
import numpy as np

from ligotools import readligo as rl
from ligotools import utils as ut

def test_write_wavfile():
	wav_path = "/home/jovyan/Homework/hw06-midoripierce/data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
	assert os.path.isfile(wav_path)


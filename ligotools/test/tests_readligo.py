import os
import pytest
import numpy as np
from ligotools import readligo as rl 

def test_loaddata1():
    fn_H1 = "/home/jovyan/Homework/hw06-midoripierce/data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    assert type(strain_H1) == np.ndarray
    
def test_loaddata2():
    fn_H1 = "/home/jovyan/Homework/hw06-midoripierce/data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    assert type(time_H1) == np.ndarray
    assert type(chan_dict_H1) == dict

def test_loaddata3():
	fn_L1 = "/home/jovyan/Homework/hw06-midoripierce/data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
    assert type(strain_L1) == np.ndarray

def test_loaddata4():
	fn_L1 = "/home/jovyan/Homework/hw06-midoripierce/data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
    assert type(time_L1) == np.ndarray
    assert type(chan_dict_L1) == dict

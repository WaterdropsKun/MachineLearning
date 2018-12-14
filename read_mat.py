import scipy.io as sio
import numpy as np


load_fn = "./Resource/AFW_134212_1_0_pts.mat"
load_data = sio.loadmat(load_fn)
print(load_data['pts_2d'])
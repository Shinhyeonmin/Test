from torch.utils.data.dataset import Dataset
import torch
from cnn_model_2 import Cnn_Model
from data14 import NKDataset
from tensorboardX import SummaryWriter
import argparse
import time
import os
import torchvision.datasets as mdatset
import torchvision.transforms as transforms


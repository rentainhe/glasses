import unittest
import torch
import torch.nn as nn
from eyes.nn.blocks.residuals import ResidualAdd, ResidualCat
from eyes.nn.blocks import Lambda

def test_add():
    x = torch.tensor(1)
    add_one = Lambda(lambda x: x + 1)
    adder = ResidualAdd(nn.Identity())
    # 1 + 1
    assert adder(x) == 2
    adder = ResidualAdd(nn.Identity(), shortcut=add_one)
    # 1 + 1 + 1
    assert adder(x) == 3

def test_concat():
    x = torch.tensor([1])
    catter = ResidualCat(nn.Identity())
    assert catter(x).sum() == 2


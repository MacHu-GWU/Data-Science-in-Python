#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
if sys.platform == "darwin":
    import matplotlib
    matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

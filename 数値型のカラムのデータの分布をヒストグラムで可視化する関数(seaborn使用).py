import sys,os
import gc
from pathlib import Path
import glob
import re
import pickle
import warnings
import re

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns
%matplotlib inline

def disp_hist(df, col):
    '''
    関数内容
    ・数値型のカラムのデータの分布をヒストグラムで可視化する関数(seaborn使用)
    Input
    ・df：データフレーム
    ・col:データフレームのカラム
    関数使用方法
    for col in df.columns.tolist():
        disp_hist(df, col)
    '''   
    try:
        plt.figure()# グラフの重複を防ぐために追加
        sns.distplot(df[col])
        plt.title('↓' + col + 'カラムの値の分布' + '↓')
        
    except:
        print(col+'はデータ型が整数型か浮動小数点型ではないか、もしくは欠損値が含まれているためにヒストグラムを描画できません')

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

def ax_disp_hist(df):
    '''
    関数内容
    ・数値型のカラムのデータの分布をヒストグラムで連続的に可視化する関数
    Input
    ・df：データフレーム
    ・col:データフレームのカラム
    関数使用方法
    ax_disp_hist(df)
    '''
    import math
    # 小数点以下を切り上げ
    fig, axes = plt.subplots(math.ceil(len(df.columns.tolist())/2), 2, figsize=(15,80))
    # 二次元データのaxesを一次元データに変換
    one_dimension_axes = axes.ravel()
    # 各カラムのデータの分布をヒストグラムで連続的に可視化
    for ax, col in zip(one_dimension_axes, df.columns.tolist()):
        try:
            ax.hist(df[col],color='g')
            ax.set_title('↓↓'+col+'カラムの値の分布↓↓')

        except:
            ax.set_title('↓↓'+col+'カラムの値の分布↓↓')
            print(col+'はデータ型が整数型か浮動小数点型ではないか、もしくは欠損値が含まれているためにヒストグラムを描画できません')
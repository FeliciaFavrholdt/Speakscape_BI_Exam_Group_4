import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def init_environment():
    sns.set_theme(style="whitegrid", palette="deep")
    folders = ["../data", "../models", "../plots", "../reports"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("Environment initialized.")

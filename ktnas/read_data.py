import pandas as pd
import os

def read_microwave1():
    
    df = pd.read_excel("data/Microwave1/microwave.xlsx")
    
    return df


if __name__ == '__main__':

    df = read_microwave1()
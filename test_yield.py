import pytest
import pandas as pd

def rate(x):
    return (x == 1).mean()


def test_wafer_yield_meets_threshold():

    df = pd.read_csv('wafer_yield.csv', sep=',', header=0)


    bad = df[df['yield_rate'] < df['threshold']]

    assert bad.empty, f"以下wafer良率不达标：\n {bad[['wafer_id', 'yield_rate', 'threshold']]}"


def test_lot_yield_calculation():
    df = pd.read_csv('die_test_data.csv')

    lot_yield = df.groupby('lot_id')['bin_code'].apply(rate)


    assert (lot_yield>0.6).all(), f"以下lot良率不达标：\n {lot_yield}"

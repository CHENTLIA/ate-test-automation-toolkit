import pandas as pd

import pytest


def test_voltage_within_spec():
    df = pd.read_csv('voltage.csv')

    df['voltage'] = df['voltage'].astype(float)

    lower, upper = 12.345 - 0.05, 12.345 + 0.05

    outliers = df[(df['voltage'] < lower) | (df['voltage'] > upper)]

    fail_rate = len(outliers) / len(df)

    assert fail_rate <= 0.1, f"超规格比例{fail_rate:.1%}，超过10%阈值"

from hamilton.function_modifiers import extract_columns
import pandas as pd


@extract_columns(*["spend", "signups"])
def raw_dataset() -> pd.DataFrame:
    """Pretend this is a function that loads a raw dataset."""
    index = pd.date_range('20230101', '20230110')
    return pd.DataFrame(
        index=index,
        data={
            "signups": [1, 10, 50, 100, 200, 400, 700, 800, 1000, 1300],
            "spend": [10, 10, 20, 40, 40, 50, 100, 80, 90, 120],
        })


def acquisition_cost_rolling_mean_7(spend: pd.Series) -> pd.Series:
    """Rolling 7 day average spend."""
    return spend.rolling(window=7, min_periods=1).mean()

import pandas as pd
import numpy as np

# Create DataFrame with specified columns and data types
df = pd.DataFrame({
    'warehouse_id': pd.Categorical([]),
    'service_area_id': pd.Series([], dtype='object'),
    'block_start_datetime_utc': pd.Series([], dtype='datetime64[ns]'),
    'block_start_datetime_local': pd.Series([], dtype='datetime64[ns]'),
    'duration': pd.Series([], dtype='float32'),
    'guaranteed_earnings_price_per_hr': pd.Series([], dtype='float32'),
    'block_length': pd.Series([], dtype='float32'),
    'block_start_wave': pd.Series([], dtype='object'),
    'wave_mins': pd.Series([], dtype='int16'),
    'promisewindow': pd.Categorical([]),
    'promisewindownumber': pd.Series([], dtype='int16'),
    'sum_metric_rlp_adds': pd.Series([], dtype='int64'),
    'avg_metric_rlp_adds': pd.Series([], dtype='int64'),
    'max_metric_rlp_adds': pd.Series([], dtype='int64'),
    'min_metric_rlp_adds': pd.Series([], dtype='int64'),
    'avg_max_min_metric_rlp_adds': pd.Series([], dtype='int64'),
    'sum_checked_in_blocks': pd.Series([], dtype='int64'),
    'sum_attended_blocks': pd.Series([], dtype='int64'),
    'sum_bwnd_blocks': pd.Series([], dtype='int64'),
    'sum_surged_blocks': pd.Series([], dtype='float64'),
    'sum_extended_blocks': pd.Series([], dtype='int64')
})

# Add derived columns
df['BWND_happened'] = (df['sum_bwnd_blocks'] > 0).astype(int)
df['RLP_happened'] = (df['sum_metric_rlp_adds'] > 0).astype(int)

print(df.dtypes)
print(f"DataFrame shape: {df.shape}")
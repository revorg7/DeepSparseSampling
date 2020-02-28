import pandas as pd
from typing import List, Tuple, Text
import glob
import os
from bsuite.logging import csv_logging
from bsuite import sweep



def load_one_result_set(results_dir: Text) -> pd.DataFrame:
  """Returns a pandas DataFrame of bsuite results stored in results_dir."""
  data = []
  for file_path in glob.glob(os.path.join(results_dir, '*.csv')):
    _, name = os.path.split(file_path)
    # Rough and ready error-checking for only bsuite csv files.
    if not name.startswith(csv_logging.BSUITE_PREFIX):
      print('Warning - we recommend you use a fresh folder for bsuite results.')
      continue

    # Then we will assume that the file is actually a bsuite file
    df = pd.read_csv(file_path)
    file_bsuite_id = name.strip('.csv').split(csv_logging.INITIAL_SEPARATOR)[1]
    bsuite_id = file_bsuite_id.replace(csv_logging.SAFE_SEPARATOR,
                                       sweep.SEPARATOR)
    df['bsuite_id'] = bsuite_id
    df['results_dir'] = results_dir
    data.append(df)
  df = pd.concat(data, sort=False)
  return df

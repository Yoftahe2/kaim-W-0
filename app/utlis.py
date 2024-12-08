import pandas as pd
def load_data(file) :
    # Load data from a file-like object(i.e, like uploading csv file )
    return pd.read_csv(file)
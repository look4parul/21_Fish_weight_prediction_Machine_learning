import pandas as pd
def prep_data(df):

    df = pd.get_dummies(df, drop_first = True)
    print(df.head())
    X = df[['Length3', 'Height', 'Width', 'Species_Parkki', 'Species_Perch',
       'Species_Pike', 'Species_Roach', 'Species_Smelt', 'Species_Whitefish']].values
    # X = df[['Length3', 'Height', 'Width']].values
    y = df[["Weight"]].values
    #  print("Values of X are: ", X[:5])
    return X, y
def prep_data(df):

    #df = df.assign(hw=df["Height"] * df["Width"])

    X = df [['Length3', 'Height', 'Width']].values
    #X_log = df[["Height", "Width", "hw"]].values
    y = df["Weight"].values
   #  print("Values of X are: ", X[:5])

    return X, y
def prep_data(df):

    #df = df.assign(hw=df["Height"] * df["Width"])

    X = df [['Length1', 'Length2', 'Length3', 'Height', 'Width']].values
    #X = df[["Height", "Width", "hw"]].values
    y = df["Weight"].values
   #  print("Values of X are: ", X[:5])

    return X, y
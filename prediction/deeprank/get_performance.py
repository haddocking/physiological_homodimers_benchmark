import sys
import pandas as pd

def perf_summary(df, many_filter=False):
    
    if many_filter :
        df = df[df.MANY_overlap == 0]
        print ("#### Performance on this data set excluding overlapping with the MANY dataset:\n")
    else:
        print("#### Performance on this data set:\n")

    size_complex_list = df.shape[0]
    size_physiological = df[df.truth == 1].shape[0]
    size_non_physiological = df[df.truth == 0].shape[0]
    
    size_complex_list_no_failures = df[df.pred.isin([0,1])].shape[0]

    bio_and_phy = df[(df.pred == 1) & (df.truth == 1)].shape[0]
    bio_and_non_phy = df[(df.pred == 1) & (df.truth == 0)].shape[0]
    cry_and_phy = df[(df.pred == 0) & (df.truth == 1)].shape[0]
    cry_and_non_phy = df[(df.pred == 0) & (df.truth == 0)].shape[0]

    success_rate_all = round((bio_and_phy+cry_and_non_phy)/float(size_complex_list)*100,3)
    success_rate_nofail = round((bio_and_phy+cry_and_non_phy)/float(size_complex_list_no_failures)*100,3)
    
    print(f"Size of complex list: {size_complex_list}")
    print(f"Size of complex list processed : {size_complex_list_no_failures}")
    print(f"Size of Physiological list: {size_physiological}")
    print(f"Size of Non Physiological list: {size_non_physiological}")
    print(f"Predicted as BIO and Physiological: {bio_and_phy}")
    print(f"Predicted as BIO and Non-Physiological: {bio_and_non_phy}")
    print(f"Predicted as CRYSTAL and Physiological: {cry_and_phy}")
    print(f"Predicted as CRYSTAL and Non-Physiological: {cry_and_non_phy}")
    print("\n")
    print(f"Success rate (considering unprocessed data): {success_rate_all}%")
    print(f"Success rate (omitting unprocessed data): {success_rate_nofail}%\n")


if __name__ == "__main__":
    
    try:
        path_df = sys.argv[1]
        df = pd.read_csv(path_df, sep = ' ')
        perf_summary(df)
        perf_summary(df, many_filter=True)
    except: 
        raise ("input file could not be proccessed")

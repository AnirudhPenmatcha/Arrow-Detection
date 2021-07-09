import pandas as pd

def main():
        to_append_df = pd.read_csv('test images & csv/test.csv')
        prev_df = pd.read_csv('test images & csv/right_test_labels.csv')
        updt_csv = prev_df.append(to_append_df, ignore_index = True)
        print(to_append_df)
        updt_csv.to_csv('test_new.csv', index=None)
        print('Successfully converted xml to csv.')

main()

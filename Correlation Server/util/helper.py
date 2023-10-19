import traceback

class Helper:
    def __init__(self):
        pass

    def make_table_data(self, df):
        try:
            table_data = [list(df.iloc[row].values) for row in range(len(df))]
            table_col = df.columns.to_list()
            return table_data, table_col
        except Exception as err:
            # raise Exception("Data frame has empty!")
            traceback.print_exc()
            raise Exception("Data frame has empty!")
# Importing necessary libraries.
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


class Correlation_report:
    """This algorithm helps to find very strong correlation variables, strong correlation variables,
    moderate correlation variables, weak correlation variables, very weak correlation variables, and
    defined ranges correlation variables."""

    def __init__(self, dataframe):
        num_df = dataframe.select_dtypes(exclude=object)
        self.corr_df = num_df.corr()

    def _vsc(self, r):
        """This is a condition for find very strong correlation pairs."""
        vsc = ((1 >= r) & (r >= 0.95)) | ((-0.95 >= r) & (r >= -1))
        return vsc

    def _sc(self, r):
        """This is a condition for find strong correlation pairs."""
        sc = ((0.95 > r) & (r >= 0.70)) | ((-0.70 >= r) & (r > -0.95))
        return sc

    def _mc(self, r):
        """This is a condition for find moderate correlation pairs."""
        mc = ((0.70 > r) & (r >= 0.50)) | ((-0.50 >= r) & (r > -0.70))
        return mc

    def _wc(self, r):
        """This is a condition for find weak correlation pairs."""
        wc = ((0.50 > r) & (r >= 0.25)) | ((-0.25 >= r) & (r > -0.50))
        return wc

    def _vwc(self, r):
        """This is a condition for find very weak correlation pairs."""
        vwc = ((0.25 > r) & (r > -0.25) & (r != 0))
        return vwc

    def _nc(self, r):
        """This is a condition for find no correlation pairs."""
        nc = (r == 0)
        return nc

    def __remove_null(self, reducied_df):
        """This method helps to return the appropriate data frame."""
        col_ls = []
        index_ls = []
        value = []
        for col in reducied_df.columns:
            for null, index in zip(reducied_df[col].isnull(), reducied_df.index):
                if null == False:
                    col_ls.append(col)
                    index_ls.append(index)
                    value.append(reducied_df.loc[col, index])
        ans_df = pd.DataFrame(dict(First_Variable=col_ls, Second_Variable=index_ls, correlation_value=value))
        ans_df['bool_corr'] = ans_df['correlation_value'].duplicated()
        ans_df = ans_df.where(ans_df['bool_corr'] == False)
        ans_df.dropna(inplace=True)
        ans_df.reset_index(drop=True, inplace=True)
        ans_df.drop(labels="bool_corr", axis=1, inplace=True)
        return ans_df

    def very_strong_corr(self):
        """This method helps to find the very strong correlation pairs.
           Returns
           -------
           Correlation Pairs : Data Frame
                It returns the correlation pairs between -/+ 1 to -/+ 0.95 correlation values.
        """
        result = self.corr_df[self._vsc(self.corr_df)]
        return self.__remove_null(result)

    def strong_corr(self):
        """This method helps to find the strong correlation pairs.
           Returns
           -------
           Correlation Pairs : Data Frame
                It returns the correlation pairs between -/+ 0.95 to -/+ 0.70 correlation values.
        """
        result = self.corr_df[self._sc(self.corr_df)]
        return self.__remove_null(result)

    def moderate_corr(self):
        """This method helps to find the moderate correlation pairs.
           Returns
           -------
           Correlation Pairs : Data Frame
                It returns the correlation pairs between -/+ 0.70 to -/+ 0.50 correlation values.
        """
        result = self.corr_df[self._mc(self.corr_df)]
        return self.__remove_null(result)

    def weak_corr(self):
        """This method helps to find the weak correlation pairs.
           Returns
           -------
           Correlation Pairs : Data Frame
                It returns the correlation pairs between -/+ 0.50 to -/+ 0.25 correlation values.
        """
        result = self.corr_df[self._wc(self.corr_df)]
        return self.__remove_null(result)

    def very_weak_corr(self):
        """This method helps to find the very weak correlation pairs.
           Returns
           -------
           Correlation Pairs : Data Frame
                It returns the correlation pairs between -0.25 to 0.25 correlation values.
        """
        result = self.corr_df[self._vwc(self.corr_df)]
        return self.__remove_null(result)

    def no_corr(self):
        """This method helps to find the no correlation pairs.
           Returns
           -------
           Correlation Pairs : Data Frame
                It returns the no correlation pairs.
        """
        result = self.corr_df[self._nc(self.corr_df)]
        return self.__remove_null(result)

    def customize_corr(self, lower_range=-1, upper_range=1):
        """This method helps to find the correlation pairs in the defined range.
            Parameters
            ----------
            lower_range : float_value
                          The lower correlation value, which gets the correlation pairs above that value.
                          The default, lower_range is -1.
            upper_range : float_value
                          The upper correlation value, which gets the correlation pairs below that value.
                          The default, upper_range is +1.

            Returns
            -------
            Correlation Pairs : Data Frame
                 It returns the correlation pairs between given lower and upper correlation values.

            Notes
            -----
            The lower range is always smaller than the upper range, and these range should be between -1 to 1.

        """
        # if lower_range < upper_range:
        #     if -1 <= lower_range and upper_range <=1:
        if -1 <= lower_range < upper_range <= 1:
            result = self.corr_df[(upper_range >= self.corr_df) & (self.corr_df >= lower_range)]
            return self.__remove_null(result)
        else:
            print("The lower range is always smaller than the upper range, and these range should be between -1 to 1.")
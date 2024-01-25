import unittest
import os
import pandas as pd
from excel_operations import read_excel, manipulate_data, write_to_excel_with_formulas

class TestExcelOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.input_file_path = 'test_input.xlsx'
        cls.output_file_path = 'test_output.xlsx'

        df = pd.DataFrame({
            'Quantity': [10, 20, 30],
            'UnitPrice': [100, 200, 300]
        })
        df.to_excel(cls.input_file_path, index=False)

    def test_read_excel(self):
        df = read_excel(self.input_file_path)
        self.assertEqual(len(df), 3)
        self.assertTrue('Quantity' in df)
        self.assertTrue('UnitPrice' in df)


    def test_manipulate_data(self):
        df = read_excel(self.input_file_path)
        manipulated_df = manipulate_data(df)

        self.assertEqual(len(manipulated_df), 3)
        self.assertTrue('Total' in manipulated_df)
        self.assertTrue('TotalWithVAT' in manipulated_df)

        expected_total_series = pd.Series([1000, 4000, 30*300], name='Total')
        pd.testing.assert_series_equal(manipulated_df['Total'],expected_total_series,check_names=True )

    def test_write_to_excel_with_formulas(self):
        df = read_excel(self.input_file_path)
        manipulated_df = manipulate_data(df)
        write_to_excel_with_formulas(manipulated_df, self.output_file_path)
        self.assertTrue(os.path.exists(self.output_file_path))

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.input_file_path)
        os.remove(cls.output_file_path)
        

if __name__ == '__main__':
    unittest.main()
    

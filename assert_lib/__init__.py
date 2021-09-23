from reg_writer.regression_sheet_writer import RegressionSheet
import sys

write_results = False
reg_sheet_path = ''

for arg in sys.argv:
    if '--write-results=' in arg:
        write_results = True
        reg_sheet_path = arg.split('=')[1]
        print(f'Reg sheet path - {reg_sheet_path}')

reg_sheet = RegressionSheet(path=reg_sheet_path)
reg_sheet.load_regression_file()
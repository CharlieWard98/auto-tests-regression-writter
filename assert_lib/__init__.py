from reg_writer.regression_sheet_writer import RegressionSheetWriter
import sys

write_results = False
reg_sheet_path = ''

for arg in sys.argv:
    if '--write-results=' in arg:
        write_results = True
        reg_sheet_path = arg.split('=')[1]

if write_results:
    reg_sheet = RegressionSheetWriter(path=reg_sheet_path)
    reg_sheet.load_regression_file()
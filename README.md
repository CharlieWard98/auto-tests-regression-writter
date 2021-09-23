# Auto test regression writter POC
 
This repo is a working POC showing how regression test results could be written directly to a regression test file from the automation tests

## Requirements
- Python
- Pip
    - unittest
    - openpyxl
- Example command - `python main.py --write-results=C:\Code\auto-tests-regression-writter\Windows.xlsx`

## Practicalities
### What needs to change?
- Each regression test on the reression test excel sheet would need to be assigned a UID - see `Windows.xlsx` as an example
- The regression test sheet would need to be stored on S3 for GoCD to access
- Each `self.assert...` function call in the current automation tests would need to be replaced with the `assert_lib` equivalent - these are very simple to implement our own version
- Each `assert...` function from the `assert_lib` is passed the conditions to check, the UID of the regression test being tested and a message - see `tests/test_basic.py` as an example
- I imagine default behaviour will be for the `assert_lib` to **not**  write results to a regression test sheet - only for release builds (See below)

### Release Builds
- Release build downloads the regression test sheet from S3 and names appropriately for the given OS
- Release build passes flags when running the automation tests
    - Flag to specify location and name of regression sheet to write to
- The tests run as usual, populating the regression test sheet with Pass/Fail results and messages
- GoCD publishes the regression tests sheet as an artifact - this can be downloaded and will act as a starting point for the regression tests for said platform

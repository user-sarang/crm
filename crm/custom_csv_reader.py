from openpyxl import load_workbook


# Read file
def read_csv(filename)
wb = load_workbook(filename, read_only=True)
ws = wb.active()

from openpyxl import load_workbook

# Load the Excel workbook
wb = load_workbook('sample.xlsx')

# Select the active sheet (or specify a sheet name: wb['Sheet1'])
sheet = wb.active

# Read a specific row (e.g., row 3, since indexing starts from 1)
row_index = 3  # Adjust based on your requirement

# Extract values from the row
row_values = [cell.value for cell in sheet[row_index]]

# Print the values in the row
print(row_values)

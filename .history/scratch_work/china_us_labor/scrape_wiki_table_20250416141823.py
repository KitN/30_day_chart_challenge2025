from bs4 import BeautifulSoup
import csv
import re

def get_indent_level(cell_text):
    # Detect padding levels based on "style" attribute with "padding-left"

    match = re.search(r'padding-left:\s*(\d+)em', cell_text)
    if match:
        indent_level = int(match.group(1))  # Extract the number of "em"
    else:
        indent_level = 0  # Default to 0 if no padding is found
    return indent_level, cell_text.strip()

# Load your HTML
with open('scratch_work\china_us_labor\BLSTable.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

rows = []
for tr in soup.find_all('tr'):
    cells = tr.find_all(['td', 'th'])
    if not cells:
        continue
    raw_first_col = cells[0].get_text()
    indent_level, cleaned_text = get_indent_level(raw_first_col)

    row_data = [cleaned_text]
    row_data.extend(cell.get_text(strip=True) for cell in cells[1:])
    rows.append((indent_level, row_data))

# Build hierarchy columns
csv_rows = []
hierarchy_stack = [''] * 10  # Assuming max 10 levels deep

for indent_level, data in rows:
    hierarchy_stack[indent_level] = data[0]
    # Clear deeper levels
    for i in range(indent_level + 1, len(hierarchy_stack)):
        hierarchy_stack[i] = ''
    hierarchy_columns = hierarchy_stack[:indent_level + 1]
    csv_rows.append(hierarchy_columns + data[1:])

# Save to CSV
with open('scratch_work/china_us_labor/USBLScounts.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in csv_rows:
        writer.writerow(row)

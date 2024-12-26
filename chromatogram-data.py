import pandas as pd
import xlsxwriter

# Create DataFrame with the chromatogram data
data = {
    'Retention Time': [5.857, 13.987, 18.405],
    'Area': [426149, 446130, 649939],
    'Area %': [28.00, 29.31, 42.70],
    'Height': [38420, 44914, 61971],
    'Height %': [26.44, 30.91, 42.65],
    'Compound': ['Catechin', 'Rutin', 'Quercetin']
}

df = pd.DataFrame(data)

# Create totals row
totals = {
    'Retention Time': 'Totals',
    'Area': 1522218,
    'Area %': 100.00,
    'Height': 145305,
    'Height %': 100.00,
    'Compound': ''
}

# Export to Excel
with pd.ExcelWriter('Flavonoids_50.xlsx', engine='xlsxwriter') as writer:
    # Write the main data
    df.to_excel(writer, sheet_name='Flavonoids 50', index=False)
    
    # Get the workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Flavonoids 50']
    
    # Add title
    title_format = workbook.add_format({
        'bold': True,
        'font_color': 'red',
        'font_size': 14
    })
    worksheet.write('A1', 'Flavonoids 50', title_format)
    
    # Add subtitle
    subtitle_format = workbook.add_format({
        'font_color': 'red',
        'align': 'center'
    })
    worksheet.merge_range('A2:F2', '(Catechin, Rutin, Quercetin)', subtitle_format)
    
    # Move data down to accommodate title and subtitle
    df.to_excel(writer, sheet_name='Flavonoids 50', startrow=3, index=False)
    
    # Add totals row
    row_position = len(df) + 4  # +4 because of title, subtitle, and header
    worksheet.write(row_position, 0, totals['Retention Time'])
    worksheet.write(row_position, 1, totals['Area'])
    worksheet.write(row_position, 2, totals['Area %'])
    worksheet.write(row_position, 3, totals['Height'])
    worksheet.write(row_position, 4, totals['Height %'])
    
    # Add borders to totals row
    border_format = workbook.add_format({'border': 1})
    worksheet.conditional_format(row_position, 0, row_position, 4, 
                               {'type': 'no_blanks', 'format': border_format})
    
    # Adjust column widths
    worksheet.set_column('A:A', 15)  # Retention Time
    worksheet.set_column('B:B', 12)  # Area
    worksheet.set_column('C:C', 10)  # Area %
    worksheet.set_column('D:D', 12)  # Height
    worksheet.set_column('E:E', 10)  # Height %
    worksheet.set_column('F:F', 15)  # Compound

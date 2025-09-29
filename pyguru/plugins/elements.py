import json

from pyguru import PyGuru


def export_spreadjs_table(pyguru: PyGuru,  resource_id: dict) -> list[dict]:
    element = pyguru.elements.get_by_id(resource_id)
    data = json.loads(element['data'])
    spread = json.loads(data['spread'])
    sheets = []
    for sheet_name, sheet_data in spread.get('sheets', {}).items():
        sheet_table = sheet_data['data'].get('dataTable', [])
        sheet_rows = [
            [d.get('value', '') for d in sheet_table[row_idx].values()]
            for row_idx in sheet_table
        ]
        sheets.append(
            {
                'name': sheet_name,
                'rows': sheet_rows
            }
        )
    return sheets

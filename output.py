# output.py
from tabulate import tabulate

def display_table(data):
    headers = ["Total Views", "Accession Number", "Athena ID", "Thumbnail Url", "Tombstone"]
    table = [[item['views'], item['accession_number'], item['athena_id'], item['thumbnail'], item['tombstone']] for item in data]
    print(tabulate(table, headers=headers, tablefmt="grid"))

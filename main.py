from cli import parse_arguments
from ga4_api import fetch_artwork_pages
from cma_api import get_artwork_details
from output import display_table
from config import PROPERTY_ID

def main():
    args = parse_arguments()

    # Fetch top artwork data from Google Analytics
    analytics_data = fetch_artwork_pages(
        property_id=PROPERTY_ID,
        start_date=args.start_date,
        end_date=args.end_date,
        limit=args.top,
    )

    # Fetch additional details from CMA API
    enriched_data = []
    for item in analytics_data:
        details = get_artwork_details(item["accession_number"])
        if details:
            enriched_data.append({
                "views": item["views"],
                "accession_number": item["accession_number"],
                "athena_id": details["athena_id"],
                "thumbnail": details["thumbnail"],
                "tombstone": details["tombstone"],
            })

    # Display results
    display_table(enriched_data)

if __name__ == "__main__":
    main()

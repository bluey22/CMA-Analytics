# ga4_api.py

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
from google.analytics.data_v1beta.types import GetMetadataRequest
import re

def list_dimensions_and_metrics(property_id):
    client = BetaAnalyticsDataClient()
    request = GetMetadataRequest(name=f"properties/{property_id}/metadata")
    metadata = client.get_metadata(request)

    print("Available Dimensions:")
    for dimension in metadata.dimensions:
        print(f"Name: {dimension.api_name}, Description: {dimension.description}")

    print("\nAvailable Metrics:")
    for metric in metadata.metrics:
        print(f"Name: {metric.api_name}, Description: {metric.description}")

def fetch_artwork_pages(property_id, start_date, end_date, limit, page_size=50):
    client = BetaAnalyticsDataClient()
    data = []
    total_fetched = 0  # To use for paging the next query

    while len(data) < limit:
        # Fetch the next chunk of data
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name="pagePath")],
            metrics=[Metric(name="screenPageViews")],
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            order_bys=[{"desc": True, "metric": {"metric_name": "screenPageViews"}}],
            limit=page_size,
            offset=total_fetched,  # Offset for paging
        )
        response = client.run_report(request)

        # Stop if no more rows are available
        if not response.rows:
            break

        # Process rows
        for row in response.rows:
            page_path = row.dimension_values[0].value
            views = int(row.metric_values[0].value)

            # Match URLs with the format /art/{number.number} and exclude non-artwork paths (like /art/collections/...)
            if re.match(r"^/art/\d+\.\d+$", page_path):
                accession_number = page_path.split("/art/")[-1]
                data.append({"accession_number": accession_number, "views": views})

                # Stop if we have enough data
                if len(data) >= limit:
                    break

        # Update total fetched rows
        total_fetched += len(response.rows)

    return data

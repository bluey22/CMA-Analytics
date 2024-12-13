# cli.py
import argparse
from datetime import datetime, timedelta

def parse_arguments():
    parser = argparse.ArgumentParser(description="CMA Google Analytics CLI Application")
    parser.add_argument(
        "--start-date",
        type=str,
        default=(datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d"),
        help="Start date in YYYY-MM-DD format (default: past 90 days)."
    )
    parser.add_argument(
        "--end-date",
        type=str,
        default=datetime.now().strftime("%Y-%m-%d"),
        help="End date in YYYY-MM-DD format (default: today)."
    )
    parser.add_argument(
        "--top",
        type=int,
        choices=[5, 10, 25],
        default=5,
        help="Number of top artworks to retrieve (default: 5)."
    )
    return parser.parse_args()

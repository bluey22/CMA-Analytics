# CMA Analytics
This Python command-line application retrieves and visualizes analytics data for artwork from the Cleveland Museum of Art. It fetches data from Google Analytics and the CMA Open Access API, allowing users to view statistics, metadata, and thumbnails of the most viewed artworks.

# Features
Retrieve artwork analytics with customizable date ranges and limits.
Display artwork information in a tabular format or as a graph.
Automatically fetch thumbnails and metadata from the CMA API.

# Prerequisites
Python 3.9 or higher
pip (Python package manager)
client_secrets.json for interacting with the Ga4 API, and the PROPERTY_ID stored in a config.py file you will make

# Set Up
```bash
git clone https://github.com/your-username/cma-analytics.git
cd cma-analytics
# Create virtual environment
# On Windows
python -m venv env
.\env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

# The application supports the following command-line arguments:
`--start-date`: Start date for the data range in YYYY-MM-DD format (default: past 90 days).

`--end-date`: End date for the data range in YYYY-MM-DD format (default: today).

`--top`: Number of top artworks to retrieve (5, 10, or 25, default: 5).

`--output`: Output format (table or graph, default: table).

Example:
```bash
python main.py --start-date 2024-01-01 --end-date 2024-12-01 --top 10 --output table
```


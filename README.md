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

# Set environmental var
$env:GOOGLE_APPLICATION_CREDENTIALS= "path/to/json/creds" #Windows
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

# TODO
* Display images in a lightweight gui app
* Display data for each artwork leading back to Jan 1st, 2024

# Example Result

```bash
python main.py --start-date 2024-12-01 --end-date 2024-12-12         
+---------------+--------------------+-------------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Total Views |   Accession Number |   Athena ID | Thumbnail Url                                                       | Tombstone                                                                                                   
                                                                                                                                                                                         |
+===============+====================+=============+=====================================================================+======================================================================================================================================================================================================================================================================================================+
|          4242 |            1997.16 |      159858 | https://clevelandart.org/art/1997.164                               | The Bundle, 1994 or 1995. Janusz Walentynowicz (American, b. 1956). Cast glass and paint; overall: 50 x 39.8 cm (19 11/16 x 15 11/16 in.). The Cleveland Museum of Art, Gift of Robert and Ann Friedman 1997.164                                                                                     |
+---------------+--------------------+-------------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|           363 |            1976.2  |      148758 | https://openaccess-cdn.clevelandart.org/1976.2/1976.2_web.jpg       | The Crucifixion of Saint Andrew, 1606–7. Caravaggio (Italian, 1571–1610). Oil on canvas; framed: 233.5 x 184 x 12 cm (91 15/16 x 72 7/16 x 4 3/4 in.); unframed: 202.5 x 152.7 cm (79 3/4 x 60 1/8 in.). The Cleveland Museum of Art, Leonard C. Hanna Jr. Fund 1976.2                               |
+---------------+--------------------+-------------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|           331 |            2020.72 |      376243 | https://clevelandart.org/art/2020.72                                | Androgyny (6 Men + 6 Women), 1982, printed 1999. Nancy Burson (American, b. 1948). Gelatin silver print; image: 22.9 x 20.8 cm (9 x 8 3/16 in.); framed: 48.1 x 44.5 cm (18 15/16 x 17 1/2 in.). The Cleveland Museum of Art, The Jane B. Tripp Charitable Lead Annuity Trust 2020.72 © Nancy Burson |
+---------------+--------------------+-------------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|           315 |            1922.11 |       92937 | https://openaccess-cdn.clevelandart.org/1922.1133/1922.1133_web.jpg | Stag at Sharkey's, 1909. George Bellows (American, 1882–1925). Oil on canvas; framed: 110 x 140.5 x 8.5 cm (43 5/16 x 55 5/16 x 3 3/8 in.); unframed: 92 x 122.6 cm (36 1/4 x 48 1/4 in.). The Cleveland Museum of Art, Hinman B. Hurlbut Collection 1922.1133                                       |
+---------------+--------------------+-------------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|           314 |            1965.23 |      141639 | https://openaccess-cdn.clevelandart.org/1965.233/1965.233_web.jpg   | Twilight in the Wilderness, 1860. Frederic Edwin Church (American, 1826–1900). Oil on canvas; framed: 124 x 185 x 13 cm (48 13/16 x 72 13/16 x 5 1/8 in.); unframed: 101.6 x 162.6 cm (40 x 64 in.). The Cleveland Museum of Art, Mr. and Mrs. William H. Marlatt Fund 1965.233                      |
+---------------+--------------------+-------------+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```
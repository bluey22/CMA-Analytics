# CMA Analytics
This Python command-line application retrieves and visualizes analytics data for artwork from the Cleveland Museum of Art. It fetches data from Google Analytics and the CMA Open Access API, allowing users to view statistics, metadata, and thumbnails of the most viewed artworks.

Features
Retrieve artwork analytics with customizable date ranges and limits.
Display artwork information in a tabular format or as a graph.
Automatically fetch thumbnails and metadata from the CMA API.
Prerequisites
Python 3.9 or higher
pip (Python package manager)
Setup Instructions
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/cma-analytics.git
cd cma-analytics
Create a Virtual Environment
Create and activate a virtual environment to isolate project dependencies:

bash
Copy code
# On Windows
python -m venv env
.\env\Scripts\activate

# On macOS/Linux
python3 -m venv env
source env/bin/activate
Install Dependencies
Use pip to install all required dependencies from requirements.txt:

bash
Copy code
pip install -r requirements.txt
Run the Application
Execute the main script with the desired options:

bash
Copy code
python main.py --start-date 2024-01-01 --end-date 2024-12-01 --top 10 --output graph
Usage
The application supports the following command-line arguments:

--start-date: Start date for the data range in YYYY-MM-DD format (default: past 90 days).
--end-date: End date for the data range in YYYY-MM-DD format (default: today).
--top: Number of top artworks to retrieve (5, 10, or 25, default: 5).
--output: Output format (table or graph, default: table).
Example:

bash
Copy code
python main.py --start-date 2024-01-01 --end-date 2024-12-01 --top 10 --output table

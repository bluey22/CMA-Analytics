# cma_api.py
import requests

def get_artwork_details(accession_number):
    base_url = "https://openaccess-api.clevelandart.org/api/artworks/"
    response = requests.get(f"{base_url}{accession_number}")
    if response.status_code == 200:
        data = response.json().get("data", {})
        images = data.get("images", {})

        if not images: 
            thumbnail_url = data.get("url", "Thumbnail not available")
        else: 
            web = images.get("web", data.get("url", "Thumbnail not available"))
            thumbnail_url = web.get("url", "Thumbnail not available")

        return {
            "athena_id": data.get("athena_id", "N/A"),
            "tombstone": data.get("tombstone", "N/A"),
            "thumbnail": thumbnail_url,
        }
    return None

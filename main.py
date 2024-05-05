import argparse
import requests
import json
# Define the base URL for the SubDL API
BASE_URL = "https://api.subdl.com/api/v1/subtitles"
# Define the prefix for subtitle download links
LINK_PREFIX = "https://dl.subdl.com"
def search_subtitles(api_key, film_name=None, file_name=None, sd_id=None, imdb_id=None,
                     tmdb_id=None, season_number=None, episode_number=None, type=None,
                     year=None, languages=None, subs_per_page=10):
    # Construct the query parameters based on provided arguments
    params = {
        "api_key": api_key,
        "film_name": film_name,
        "file_name": file_name,
        "sd_id": sd_id,
        "imdb_id": imdb_id,
        "tmdb_id": tmdb_id,
        "season_number": season_number,
        "episode_number": episode_number,
        "type": type, # movie or tv
        "year": year,
        "languages": languages, #seperate them by comma
        "subs_per_page": min(subs_per_page, 30)  # Limit subs_per_page to maximum 30
    }

    # Make the GET request to the SubDL API
    response = requests.get(BASE_URL, params=params)

    # Parse the JSON response
    if response.status_code == 200:
        return response.json()
    else:
        return {"status": False, "error": f"Request failed with status code {response.status_code}"}

def main():
    parser = argparse.ArgumentParser(description="Search for movie or TV show subtitles using SubDL API")
    parser.add_argument("api_key", type=str, help="Your SubDL API key")
    parser.add_argument("--film-name", type=str, help="Search by film name")
    parser.add_argument("--file-name", type=str, help="Search by file name")
    parser.add_argument("--sd-id", type=str, help="Search by SubDL ID")
    parser.add_argument("--imdb-id", type=str, help="Search by IMDb ID")
    parser.add_argument("--tmdb-id", type=str, help="Search by TMDB ID")
    parser.add_argument("--season-number", type=int, help="Specific season number for TV shows")
    parser.add_argument("--episode-number", type=int, help="Specific episode number for TV shows")
    parser.add_argument("--type", choices=["movie", "tv"], help="Type of content (movie or tv)")
    parser.add_argument("--year", type=int, help="Release year of the movie or TV show")
    parser.add_argument("--languages", type=str, help="Comma-separated language codes for subtitle languages")
    parser.add_argument("--subs-per-page", type=int, default=10, help="Limit of subtitles per page (max 30)")

    args = parser.parse_args()

    # Call the search_subtitles function with parsed arguments
    result = search_subtitles(api_key=args.api_key,
                              film_name=args.film_name,
                              file_name=args.file_name,
                              sd_id=args.sd_id,
                              imdb_id=args.imdb_id,
                              tmdb_id=args.tmdb_id,
                              season_number=args.season_number,
                              episode_number=args.episode_number,
                              type=args.type,
                              year=args.year,
                              languages=args.languages,
                              subs_per_page=args.subs_per_page)

    # Print the formatted JSON response
    if result["status"]:
        for subtitle in result["subtitles"]:
            if "url" in subtitle:
                subtitle["download_link"] = LINK_PREFIX + subtitle["url"]

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

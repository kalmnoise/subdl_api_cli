simple python script to utilize subdl API
to get your API KEY sign up in subdl.com then you'll find it withing your account settings
use example:

1: Search subtitles for a movie:

python main.py YOUR_API_KEY --film-name "Inception" --type movie --languages EN,AR,FR

2: Search subtitles for a tv series:

python main.py YOUR_API_KEY --film-name "Game of Thrones" --type tv --season-number 1 --episode-number 1 --languages EN

NOTE: for now as I tried lots of series have no recorded season-number and episode number so it will be shown as zeroes 
better not to use season number and episode number like this:
python main.py YOUR_API_KEY --film-name "Game of Thrones" --type tv --languages EN

result:
{
  "status": true,
  "results": [
    {
      "sd_id": 1300025,
      "type": "tv",
      "name": "Game of Thrones",
      "imdb_id": "tt0944947",
      "tmdb_id": 1399,
      "first_air_date": "2011-04-17T00:00:00.000Z",
      "year": 2011
    },
    {
      "sd_id": 1307941,
      "type": "tv",
      "name": "Untitled Game of Thrones Prequel",
      "imdb_id": "tt6857128",
      "tmdb_id": 85863,
      "first_air_date": "2021-12-31T00:00:00.000Z",
      "year": 2021
    },
    {
      "sd_id": 1609982,
      "type": "tv",
      "name": "Aut\u00f3psia Game Of Thrones",
      "imdb_id": "",
      "tmdb_id": 138757,
      "first_air_date": "2020-04-14T00:00:00.000Z",
      "year": 2020
    },
    {
      "sd_id": 1642226,
      "type": "tv",
      "name": "Game of Thrones: The Iron Anniversary",
      "imdb_id": "",
      "tmdb_id": 206584,
      "first_air_date": "2021-04-05T00:00:00.000Z",
      "year": 2021
    }
  ],
  "subtitles": [
    {
      "release_name": "example release name1",
      "name": "SUBDL.com::game.of.thrones.sixth.season.tv.20161689020.zip",
      "lang": "english",
      "author": "Hougangkid",
      "url": "/subtitle/2506211-1689020.zip",
      "season": 0,
      "episode": 0,
      "download_link": "https://dl.subdl.com/subtitle/example_link.zip"
    },
    {
      "release_name": "example release name2",
      "name": "SUBDL.com::game.of.thrones.sixth.season.tv.20161689020.zip",
      "lang": "english",
      "author": "Hougangkid",
      "url": "/subtitle/2506211-1689020.zip",
      "season": 0,
      "episode": 0,
      "download_link": "https://dl.subdl.com/subtitle/example_link.zip"
    },
    .........etc
  ]
}






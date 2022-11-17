# [AnimepaheAPI](https://github.com/xenmods/AnimepaheAPI)

##### Search and download anime from Animepahe in Python!



## Installing

```bash
pip install git+https://github.com/xenmods/AnimepaheAPI
```

## Usage<br /><br />

#### Search for anime by keywords

```python
from Animepahe.animepahe import AnimepaheAPI
animepahe = AnimepaheAPI()
data = animepahe.search('one piece')
print(data)
```

<details>
 <summary> Example Result</summary>

```json
{
    "success": true,
    "results": [
        {
            "id": 4,
            "title": "One Piece",
            "type": "TV",
            "episodes": 0,
            "status": "Currently Airing",
            "season": "Fall",
            "year": 1999,
            "score": 8.67,
            "poster": "https://i.animepahe.com/posters/355e6e3127aa31f0d806114169b52c4fb6da4b87df7f9c1809b9e3de97b8aac5.jpg",
            "session": "976aa970-111b-6867-e060-7f06e6c8e4c6"
        },
        {
            "id": 437,
            "title": "Onegai\u2606Teacher",
            "type": "TV",
            "episodes": 12,
            "status": "Finished Airing",
            "season": "Winter",
            "year": 2002,
            "score": 7.12,
            "poster": "https://i.animepahe.com/posters/5178a146e5e3eada89f65aa3e8e2cca51f4c315b92951252e3453932c29fd664.jpg",
            "session": "0dfb8040-d0e2-7f41-b71b-f0895c363de6"
        },
        {
            "id": 3939,
            "title": "One Outs",
            "type": "TV",
            "episodes": 25,
            "status": "Finished Airing",
            "season": "Fall",
            "year": 2008,
            "score": 8.34,
            "poster": "https://i.animepahe.com/posters/90620fc22663baa10a37ee79931f3f6b0cfbe98a2aaf093fda813723905256fb.jpg",
            "session": "f90c29ee-caa3-4b81-e70b-a79e26e89e58"
        },
        {
            "id": 18,
            "title": "One Punch Man",
            "type": "TV",
            "episodes": 12,
            "status": "Finished Airing",
            "season": "Fall",
            "year": 2015,
            "score": 8.51,
            "poster": "https://i.animepahe.com/posters/ca4e9a20a5e5bd8b887801ab0246702f.jpg",
            "session": "7692d7c0-81ab-0700-3370-d2eec3698a6b"
        },
        {
            "id": 1614,
            "title": "One Room",
            "type": "TV",
            "episodes": 12,
            "status": "Finished Airing",
            "season": "Winter",
            "year": 2017,
            "score": 5.56,
            "poster": "https://i.animepahe.com/posters/4a4816af92d705ac367672d429514cab.jpg",
            "session": "6f8c45ca-0ada-1001-bd30-e35fe16acd10"
        },
        {
            "id": 2622,
            "title": "One Room Second Season",
            "type": "TV",
            "episodes": 12,
            "status": "Finished Airing",
            "season": "Summer",
            "year": 2018,
            "score": 6.1,
            "poster": "https://i.animepahe.com/posters/013251858732440421e5248253b538c8.jpg",
            "session": "325068fa-ba35-47e9-aa18-8afa2ec939d1"
        },
        {
            "id": 3225,
            "title": "One Punch Man 2nd Season",
            "type": "TV",
            "episodes": 12,
            "status": "Finished Airing",
            "season": "Spring",
            "year": 2019,
            "score": 7.48,
            "poster": "https://i.animepahe.com/posters/53878e7b08a721700132813d495fa64e.jpg",
            "session": "6a841a30-e0c3-7602-8e89-7e333e8b4e5d"
        },
        {
            "id": 4111,
            "title": "One Room Third Season",
            "type": "TV",
            "episodes": 12,
            "status": "Finished Airing",
            "season": "Fall",
            "year": 2020,
            "score": 6.46,
            "poster": "https://i.animepahe.com/posters/4cda78212a85bfbddaf39a57be0558cacacb3c26b9dcaf30daf00c698b220742.jpg",
            "session": "9b4af934-8dfc-f61e-34c3-9ec69423e8ba"
        }
    ]
}
```

</details><br />

#### We can use that data to get a release!

```python
from Animepahe.animepahe import AnimepaheAPI
animepahe = AnimepaheAPI()
release = animepahe.get_release('976aa970-111b-6867-e060-7f06e6c8e4c6', episode=69) # we got the session from animepahe.search()
print(release)
```

<details><br />
 <summary> Example Result</summary>

```json
{
    "success": true,
    "result": {
        "episode": 69,
        "snapshot": "https://i.animepahe.com/snapshots/d4f6542eb38d4c0f062090f0988c03b87e6f0a970d6cf032806a6eb66d968452.jpg",
        "duration": "00:24:00",
        "session": "26cae04bdb5238679e42824b45ec3f5fb12b1718b9cabeef7b69fbc5933b588d"
    }
}
```

</details><br />


#### Now using the session from the release, we can get the download link

```python
from Animepahe.animepahe import AnimepaheAPI
animepahe = AnimepaheAPI()
download = animepahe.get_download_links('26cae04bdb5238679e42824b45ec3f5fb12b1718b9cabeef7b69fbc5933b588d') # we got the session from animepahe.release()
print(download)
```


<details>
 <summary> Example Result</summary>

```json
{
    "success": true,
    "results": [
        {
            "quality": "720",
            "size": "103.22 MB",
            "audio": "japanese",
            "link": "https://pahe.win/CPAHb"
        },
        {
            "quality": "1080",
            "size": "181.55 MB",
            "audio": "japanese",
            "link": "https://pahe.win/pMvix"
        }
    ]
}
```

</details><br /><br />



## Note

- The API cannot generate direct download links as Kwik has a "DRM" system (really not a DRM but since we're having issues with it, we're going to act like it is one).
- To stream/download the m3u8 is also quite troublesome due to the above mentioned "DRM" system, hence, we need to use the "kwik" url (not kwik.cx but the url from which we extracted the m3u8) as the referer in the download header.

</br></br>
## Information

- All the research, for making this library possible, is entirely done by myself.
- This is just a fun project for me. I use it myself.
- Please star this project and feel free to fork and make changes!
- I will update it soon with more features.
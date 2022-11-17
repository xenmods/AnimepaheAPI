from AnimepaheAPI.animepahe import AnimepaheAPI
import json

animepahe = AnimepaheAPI()

# search for any anime
data = animepahe.search('one piece')
if data['success']:
    print(json.dumps(data, indent=4))

# get release of the anime using session
release = animepahe.get_release('976aa970-111b-6867-e060-7f06e6c8e4c6', episode=69) # we got the session from animepahe.search('one piece')
print(json.dumps(release, indent=4))

# get download from the release using session
download = animepahe.get_download_links('26cae04bdb5238679e42824b45ec3f5fb12b1718b9cabeef7b69fbc5933b588d')
print(json.dumps(download, indent=4))

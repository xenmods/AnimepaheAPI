import requests
from . import utils

class AnimepaheAPI():


    def __init__(self):
        self.API_URL = "https://animepahe.com/api?m="
        self.session = requests.Session()


    def search(self, args: str) -> dict:
        if args == '':
            raise ValueError('No arguments given')
        url = f"{self.API_URL}search&q={args.replace(' ', '&')}"
        resp = self.session.get(url)
        if resp.status_code != 200:
            resp.raise_for_status()
        resp = resp.json()
        result = {'success': True, 'results': resp['data']}
        return result

    def get_release(self, releaseid: str, episode: int = 1) -> dict:
        if releaseid == '':
            raise ValueError('No releaseid given!')
        url = f"{self.API_URL}release&id={releaseid}&sort=episode_asc"
        firstcall = self.session.get(url)
        if firstcall.status_code:
            firstcall.raise_for_status()
        firstcall = firstcall.json()
        if episode > firstcall['total']:
            raise ValueError('The episode given is greater than total episodes of the anime!')
        if firstcall['last_page'] == 1:
            result = {'success': True, 'result': {}}
            for file in firstcall['data']:
                if file['episode'] == episode:
                    result['result']['episode'] = file['episode']
                    result['result']['snapshot'] = file['snapshot']
                    result['result']['duration'] = file['duration']
                    result['result']['session'] = file['session']
                    break
            return result
        page = utils.get_exact_page(episode, firstcall['last_page'], firstcall['total'])
        url = f"{self.API_URL}release&id={releaseid}&sort=episode_asc&page={page}"
        resp = self.session.get(url)
        if resp.status_code:
            resp.raise_for_status()
        resp = resp.json()
        result = {'success': True, 'result': {}}
        for file in resp['data']:
            if file['episode'] == episode:
                result['result']['episode'] = file['episode']
                result['result']['snapshot'] = file['snapshot']
                result['result']['duration'] = file['duration']
                result['result']['session'] = file['session']
                break
        return result
            

    def get_download_links(self, session: str) -> dict:
        if session == '':
            raise ValueError('Invalid session id!')
        url = f"{self.API_URL}links&id={session}&p=kwik"
        resp =  self.session.get(url)
        if resp.status_code != 200:
            resp.raise_for_status()
        resp = resp.json()
        qualities = []
        filesizes = []
        audios = []
        kwiklinks = []
        for file in resp['data']:
            quality = list(file)[0]
            qualities.append(quality)
            size = file.get(quality).get('filesize')
            filesizes.append(utils.convert_size(size))
            audios.append('japanese' if file.get(quality).get('audio') == 'jpn' else 'english')
            kwiklinks.append(file.get(quality).get('kwik_pahewin'))
        results = [{'quality': qualities[i], 'size': filesizes[i], 'audio': audios[i], 'link': kwiklinks[i]} for i in range(len(qualities))]
        return {'success': True, 'results': results}

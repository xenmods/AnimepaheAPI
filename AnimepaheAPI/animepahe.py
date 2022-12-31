import requests
from . import utils
from bs4 import BeautifulSoup

class AnimepaheAPI():


    def __init__(self):
        self.API_URL = "https://animepahe.com/api?m="
        self.session = requests.Session()


    def search(self, args: str) -> dict:
        if not args:
            raise ValueError('No arguments given')
        url = f"{self.API_URL}search&q={args.replace(' ', '&')}"
        resp = self.session.get(url)
        if resp.status_code != 200:
            resp.raise_for_status()
        resp = resp.json()
        result = {'success': True, 'results': resp['data']}
        return result

    def get_release(self, releaseid: str, episode: int = 1) -> dict:
        if not releaseid:
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
        if not session:
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
            kwiklinks.append(file.get(quality).get('kwik'))
        directUrls = []
        for kwik in kwiklinks:
            headers = {'Referer':'https://animepahe.com/'}
            resp = requests.get(kwik, headers=headers)
            soup = BeautifulSoup(resp.content, 'html.parser')
            script = soup.find_all('script')[6].get_text().split('Plyr')[1].split('.split')[0].split('|')
            print(script)
            finalUrl = f"https://{script[-2]}-{script[-3]}.{script[-4]}.{script[-5]}.{script[-6]}/hls/{script[-8]}/{script[-9]}/{script[-10]}/owo.m3u8"
            directUrls.append(finalUrl)
            
        results = [{'quality': qualities[i], 'size': filesizes[i], 'audio': audios[i], 'url': directUrls[i]} for i in range(len(qualities))]
        return {'success': True, "headers": {"Referer":"https://kwik.cx/"}, 'results': results}

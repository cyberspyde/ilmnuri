import requests, threading, urllib.parse, asyncio
from bs4 import BeautifulSoup 

def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)
    return wrapped

archive_url = "https://ilmnuri.net/Abdulloh/Ramazon_2012/"
  
def get_audio_links(): 
    r = requests.get(archive_url) 
    soup = BeautifulSoup(r.content,'html5lib') 
    links = soup.findAll('a') 
    audio_links = [archive_url + link['href'] for link in links if link['href'].endswith('mp3')] 

    return audio_links 

@background
def download_audio(link):
    fn = link.split('/')[-1] 
    fn = urllib.parse.unquote(fn)
    print(link)
    r = requests.get(link)
    with open(fn, 'wb') as f:
        f.write(r.content)

if __name__ == "__main__": 
    audio_links = get_audio_links() 
    for link in audio_links:
        download_audio(link)

import requests
import sys
from time import sleep
from tqdm import tqdm

#url = 'https://www.vladtime.ru/uploads/posts/2018-03/1522438548_evropeyskaya-koshka-dikiy-kot.jpg'

def download(url) :
    response = requests.get(url, stream = True)
    fileName = url.split('/')[-1]
    fileSize = int(response.headers.get('content-length')) 

    progress = tqdm(iterable = response.iter_content(1024), 
                    desc = f'Downloading "{fileName}"', 
                    total = fileSize, 
                    unit = 'B', 
                    unit_scale = True, 
                    unit_divisor = 1024)
    with open(fileName, 'wb') as file :
        for chunk in progress.iterable :
            sleep(1)
            file.write(chunk)
            progress.update(len(chunk))

def main() :
    if len(sys.argv) > 1 :
        url = sys.argv[1]
        download(url)
        print('File has been downloaded successfully')
    else : print('Error when downloading a file\n')

if __name__ == '__main__' :
    main()

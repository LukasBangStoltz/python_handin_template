import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
class TextComparer:
    def __init__(self, url_list = []):
        self.url_list = url_list

    def download(self, url, filename):
        
        try:
           r = requests.get(url)
           with open(filename, "a") as file:
               file.write(r.text)
        except:
            raise Exception("Given url not found")   

    def multi_download(self):
        with ThreadPoolExecutor(max_workers=20) as executor:
            for url in self.url_list:
                executor.submit(self.download(url, url.split(".")[1]))   
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.url_list)==0:
            raise StopIteration
        return self.url_list.pop()            

    


tc = TextComparer(["https://www.facebook.com", "https://www.google.com"])
tc.multi_download()
print([x for x in tc])




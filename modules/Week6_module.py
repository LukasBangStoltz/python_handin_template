import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import random
class TextComparer:
    def __init__(self, url_list = []):
        self.url_list = url_list
        self.filenames = []

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
                self.filenames.append(url.split(".")[1])

              

    def __iter__(self):
        return self
    def __next__(self):
        if len(self.url_list)==0:
            raise StopIteration
        return self.url_list.pop()            

def urllist_generator(self):
    while len(self.url_list) != 0:
        yield self.url_list.pop()        

def avg_vowels(text):
    vowels = "aeiouyæøå"
    words_in_text = len(text.split(" "))
    amount_of_vowels = 0
    for char in text:
        if char in vowels:
            amount_of_vowels += 1

    avg_vowels_in_text = amount_of_vowels/words_in_text
    return avg_vowels_in_text


def hardest_read(tc_object, workers=multiprocessing.cpu_count()):
    with ProcessPoolExecutor(workers) as ex:
        avg_vowel_array = []
        for f in tc_object.filenames:
            with open(f) as file_object:
                contents= file_object.read()    
                avg_vowel_array.append(avg_vowels(contents))
        return (max(avg_vowel_array))    
            
    


"hej med dig"
tc = TextComparer(["https://www.facebook.com", "https://www.google.com","https://www.github.com", "https://www.instagram.com", "https://www.youtube.com", "https://www.tiktok.com", "https://www.vimeo.com", "https://www.amazon.com" ])
tc.multi_download()

print(hardest_read(tc))










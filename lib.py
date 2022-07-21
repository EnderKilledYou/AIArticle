import re
import textacy
import spacy
import html2text
import requests

# python -m spacy download en_core_web_lg on first run
nlp = spacy.load('en_core_web_lg')
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


def download_site(url):
    h = html2text.HTML2Text()
    x = requests.get(url, headers=headers)
    return clean_non_alpha(h.handle(x.text)).strip()

def test_text_levenshtein(text_1,text_2):
    return textacy.similarity.edits.levenshtein(text_1, text_2)
def test_text_ngrams(text_1,text_2):
    return textacy.similarity.edits.levenshtein(text_1, text_2)

def test_text_hybrid(text_1,text_2):
    return textacy.similarity.hybrid.token_sort_ratio(text_1,text_2)

def test_text(text_1, text_2):
    return {
        'hybrid':test_text_hybrid(text_1, text_2),
        'ngrams':test_text_ngrams(text_1, text_2),
        'levenshtein': test_text_levenshtein(text_1, text_2),
        'spacy': test_text_spacy(text_1, text_2),
    }



def test_text_spacy(text_1, text_2):
    doc1 = nlp(text_1)
    # print(list(doc1.noun_chunks))
    doc2 = nlp(text_2)
    # print(list(doc2.noun_chunks])
    return doc1.similarity(doc2)


def clean_non_alpha(text_1):
    return text_1
    # text_2 = re.sub(r'^https?:\/\/.*[\r\n]*', '', text_1, flags=re.MULTILINE)
   # return re.sub("[^a-zA-Z]", " ", text_2)




def test_sites(url1, url2):
    return test_text(download_site(url1), download_site(url2))


if __name__ == "__main__":
    print('starting test 1')

    score = test_sites('https://ohiobuckeyeplumbing.com', 'https://buckeyepropertysolutions.com')
    print(['https://ohiobuckeyeplumbing.com', 'https://buckeyepropertysolutions.com',score])

    score = test_sites('https://www.pinstrikes9.com', 'https://secure.meriq.com/pinstrikes9/')
    print(['https://www.pinstrikes9.com', 'https://secure.meriq.com/pinstrikes9/',score])

    score = test_sites('https://www.novakconstruction.com', 'https://carpenterkessel.com')
    print(['https://www.novakconstruction.com', 'https://carpenterkessel.com',score])

    score = test_sites('http://www.arcadeodyssey.com', 'https://www.playcasinomiami.com')
    print(['http://www.arcadeodyssey.com', 'https://www.playcasinomiami.com',score])

    print('starting test 2 (hard)')
    score = test_sites('http://cabinetrydesignsd.com', 'https://californiaplumbingsd.com')
    print(['http://cabinetrydesignsd.com', 'https://californiaplumbingsd.com',score])

    print('starting test 3 (not)')
    score = test_sites('https://ohiobuckeyeplumbing.com', 'https://ceontime.com')
    print(['https://ohiobuckeyeplumbing.com', 'https://ceontime.com',score])

    score = test_sites('https://www.pinstrikes9.com', 'https://www.1440foundation.org')
    print(['https://www.pinstrikes9.com', 'https://www.1440foundation.org',score])

    score = test_sites('https://www.novakconstruction.com', 'https://www.funpawcare.com')
    print(['https://www.novakconstruction.com', 'https://www.funpawcare.com',score])

    print('starting test 4 (hard)')
    score = test_sites('http://www.arcadeodyssey.com', 'https://fundimensionusa.com')
    print(['http://www.arcadeodyssey.com', 'https://fundimensionusa.com',score])

    score = test_sites('http://cabinetrydesignsd.com', 'https://www.hmlanding.com')
    print(['http://cabinetrydesignsd.com', 'https://www.hmlanding.com',score])

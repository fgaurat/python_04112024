import requests
from bs4 import BeautifulSoup

def main():
    url = "https://logs.eolem.com/"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = soup.find_all('a')

    
    good_links = [a["href"] for a in all_a if a["href"].endswith('.log')]
    print(good_links)
    
    # for a in all_a:
    #     if a["href"].endswith('.log'):
    #         print(a["href"])

    for good_link in good_links:
        url_log =url+good_link
        response = requests.get(url_log) 
        with open(good_link,'w') as f:
            f.write(response.text)

if __name__=='__main__':
    main()
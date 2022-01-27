from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os
import urllib.request as req


def set_up_soup(link: str) -> BeautifulSoup:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def parse_image_links(soup: BeautifulSoup) -> list:
    results = soup.find_all('div', {'class': 's-item__wrapper clearfix'})
    results.remove(results[0])
    images = []
    for i in results:
        images.append(i.find('img', {'class': 's-item__image-img'})['src'])
    return images


def download_image(links: list, name: str) -> None:
    folder_path = "E:\\pokemonImageData\\" + str(name) + "\\"
    if os.path.isdir(folder_path):
        list_len = os.listdir(folder_path)
        num_files = len(list_len)
        for i in range(len(links)):
            image_path = folder_path + str(name) + '#' + str(num_files + i) + '.png '
            req.urlretrieve(links[i], image_path)
    else:
        os.mkdir(folder_path)
        list_len = os.listdir(folder_path)
        num_files = len(list_len)
        for i in range(len(links)):
            image_path = folder_path + str(name) + '#' + str(num_files + i) + '.png '
            req.urlretrieve(links[i], image_path)


def main() -> None:
    search = 'gengar 20/62'
    link = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + str(search) + '&_sacat=0&LH_TitleDesc=0&_ipg=200'
    driver = webdriver.Firefox(executable_path=r'E:\geckodriver.exe')
    driver.get(link)
    soup = set_up_soup(link)
    images_links = parse_image_links(soup)
    name = 'Fossil Gengar'
    download_image(images_links, name)
    driver.close()


if __name__ == '__main__':
    main()

import requests
import sys


def grab_img_by_url_from_file(file_path):
    if file_path:
        with open(file_path, 'r') as reader:
            for img_url in reader.readlines():
                print(img_url, end='')
                try:
                    response = requests.get(img_url)
                    img_data = response.content
                    download_img(img_data, img_url)
                except:
                    print("Oops!", sys.exc_info()[0], "occurred.")


    else:
        print("filepath not exist")


def download_img(img_data, img_url):
    img_filename = img_url.split("/")[-1]
    with open("imgs/" + img_filename, 'wb') as handler:
        handler.write(img_data)


if __name__ == '__main__':
    file_path = "img_urls.txt"
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    grab_img_by_url_from_file(file_path)

#!/usr/bin/env python
# coding=utf-8
# Filename: html_downloader.py
# Created by iFantastic on 2017/7/1
# Description: Kaggle竞赛的源码，用来抓取图片的网络爬虫

import sys
import os
import json
from concurrent.futures import ThreadPoolExecutor
from urllib import urlretrieve


def download_images(urls, storage_path, index):
    if index % 1000 == 0:
        print("Tried downloading {} images, {} downloaded".format(index,
                                                                  len(os.listdir(os.path.dirname(storage_path)))))
    storage_dir = os.path.dirname(os.path.abspath(storage_path))
    if not os.path.exists(storage_dir):
        try:
            os.makedirs(storage_dir)
        except OSError as err:
            print("Error: {}".format(err))
    if os.path.exists(storage_path):
        return 2
    for url in urls:
        try:
            urlretrieve(url, storage_path)
            return 1
        except:
            continue


if __name__ == "__main__":

    download_file = str(sys.argv[1])

    with open(download_file) as fh:
        data = json.load(fh)
        directory_name = download_file.split(".")[1]
        directory_name += "_images"
        download_input_list = [(image['url'],
                                os.path.join(os.path.abspath(directory_name),
                                            (image['imageId'] + ".jpg"))) for image in data['images']]
        urls_list = [x[0] for x in download_input_list]
        path_names = [x[1] for x in download_input_list]
        indexes = [i for i in range(1, len(path_names)+1)]
        print("Downloading {} images of the {} dataset".format(len(path_names),
                                                                directory_name.split("_")[0]))
        with ThreadPoolExecutor(10) as executor:
            executor.map(download_images, urls_list, path_names, indexes)

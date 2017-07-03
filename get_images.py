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
    """下载图片并保存

    :param urls: 图片的url地址列表
    :param storage_path: 图片保存路径
    :param index: 图片保存的文件名
    :return: 1：；2：
    """
    if index % 1000 == 0:
        print("Tried downloading {} images, {} downloaded".format(index, len(os.listdir(os.path.dirname(storage_path)))))
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

    # download_file = str(sys.argv[1])
    download_file = "fgvc4_iMat.validation.data.json"

    # {
    #     "license": {
    #         "name": "Attribution-NonCommercial License",
    #         "id": "3",
    #         "url": "http://creativecommons.org/licenses/by-nc/4.0/"
    #     },
    #     "annotations": [
    #         {
    #             "taskId": "1",
    #             "imageId": "1",
    #             "labelId": "1"
    #         },
    #         {
    #             "taskId": "2",
    #             "imageId": "1",
    #             "labelId": "2"
    #         },
    #         ]
    #     "images": [
    #         {
    #             "imageId": "1",
    #             "url": [
    #                 "https://s-media-cache-ak0.pinimg.com/originals/15/b0/92/15b092d8bc5816f23a45e7b0736a3088.jpg"
    #             ]
    #         },
    #         {
    #               "imageId": "181",
    #               "url": [
    #                 "http://casterco.us/wp-content/uploads/2017/02/baby-blue-wedding-gown-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg",
    #                 "http://media.glamour.com/photos/5695ba1493ef4b09520e8929/master/w_743%2Cc_limit/weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg",
    #                 "http://media.glamour.com/photos/5695ba1493ef4b09520e8929/master/w_743,c_limit/weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg",
    #                 "http://modernweddings.net/wp-content/uploads/2017/03/latest-baby-blue-wedding-dresses-ideas.jpg",
    #                 "http://storyweek.org/wp-content/uploads/2016/11/weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main-blue-wedding-dress.jpg",
    #                 "http://thebridesdress.net/wp-content/uploads/2016/11/blue-wedding-dresses-wedding-gowns-baby-pale-blue-wedding-dresses.jpg",
    #                 "http://theradionic.com/wp-content/uploads/2017/02/stylish-design-ideas-light-blue-wedding-dress-wonderfull-blue-wedding-dresses-gowns-baby-pale.jpg",
    #                 "http://theradionic.com/wp-content/uploads/2017/02/valuable-idea-pale-blue-wedding-dress-contemporary-decoration-blue-wedding-dresses-gowns-baby-pale.jpg",
    #                 "http://theweddingstyle.net/wp-content/uploads/2017/01/blue-wedding-dresses-wedding-gowns-baby-pale-blue-wedding-dresses-0.jpg",
    #                 "http://theweddingstyle.net/wp-content/uploads/2017/01/blue-wedding-dresses-wedding-gowns-baby-pale-blue-wedding-dresses.jpg",
    #                 "http://weddingcafeny.com/wp-content/uploads/imgp/baby-blue-wedding-dresses-5-5755.jpg",
    #                 "http://weddingdress-bridalgowns.com/wp-content/uploads/2016/11/baby-blue-wedding-gown-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg",
    #                 "http://www.dearweddingdress.com/wp-content/uploads/2016/11/Inspiring_baby_blue_wedding_gown.jpg",
    #                 "http://www.groffart.com/wp-content/uploads/2017/01/Baby-Blue-Wedding-Gown-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg",
    #                 "http://www.wedding3.com/wp-content/uploads/2016/11/amusing-blue-wedding-dress-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main-2015.jpg",
    #                 "http://www.wedding3.com/wp-content/uploads/2016/11/appealing-blue-wedding-gowns-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main-2016.jpg",
    #                 "http://www.wedding3.com/wp-content/uploads/2016/11/marvelous-blue-wedding-dresses-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main-2016.jpg",
    #                 "http://www.weddingandfavors.com/wp-content/uploads/2016/11/Inspiring_baby_blue_wedding_gown.jpg",
    #                 "http://www.weddingdress-bridalgowns.com/wp-content/uploads/2016/11/baby-blue-wedding-gown-weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg",
    #                 "https://media.glamour.com/photos/5695ba1493ef4b09520e8929/master/w_743,c_limit/weddings-2015-06-1-blue-wedding-dresses-wedding-gowns-pale-baby-blue-0625-instagram-gabridellabridal-main.jpg"
    #               ]
    #         }
    #     ],
    #     "info": {
    #         "year": "2017",
    #         "version": "1",
    #         "contributor": "Xiao Zhang, Yang Song, Yuan Li",
    #         "description": "The dataset is created for the iMaterialist competition in the 4th FGVC workshop in conjunction with CVPR 2017. It has a total of 84,187 product images and 381 labels including training, validation and test set.",
    #         "dateCreated": "5-15-2017",
    #         "url": "https://sites.google.com/corp/view/fgvc4/competitions/imaterialist?authuser=0"
    #     }
    # }

    with open(download_file) as fh:
        data = json.load(fh)
        # 字符串拼接成validation_images
        directory_name = download_file.split(".")[1]
        directory_name += "_images"

        # [(url列表, 保存路径), 保存文件名]
        download_input_list = [(image['url'], os.path.join(os.path.abspath(directory_name), (image['imageId'] + ".jpg"))) for image in data['images']]
        urls_list = [x[0] for x in download_input_list]
        path_names = [x[1] for x in download_input_list]
        indexes = [i for i in range(1, len(path_names)+1)]
        print("Downloading {} images of the {} dataset".format(len(path_names), directory_name.split("_")[0]))
        with ThreadPoolExecutor(10) as executor:
            executor.map(download_images, urls_list, path_names, indexes)

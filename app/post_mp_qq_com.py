import os
import shutil

import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, request, Request

__base_dir = 'post.mp.qq.com'
mp_qq = Blueprint(__base_dir, __name__)


@mp_qq.route('/dl')
def dl():
    return render_template('mp_qq.html')


@mp_qq.route('/dl_to_disk')
def download_to_disk():
    url = request.query_string
    if url is None:
        return "参数为空"

    url = bytes.decode(url)
    url = url[url.index('=') + 1:]
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    video_src = soup.find(id='video-play').get('data-video-src')
    title = soup.find(id='mod-common').get('data-article-title')
    video = requests.get(video_src, stream=True)

    if not os.path.exists(__base_dir):
        os.mkdir(__base_dir)
    file = open('{}/{}.mp4'.format(__base_dir, title), 'wb')
    shutil.copyfileobj(video.raw, file)
    return 'download ok'

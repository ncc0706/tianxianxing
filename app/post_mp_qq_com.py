from flask import Blueprint, render_template

mp_qq = Blueprint('post.mp.qq.com', __name__)


# _base_dir = 'post.mp.qq.com'
#
# url = 'http://post.mp.qq.com/kan/nvideo/2500523864-5975c30d62b272aw-shg_1083162092_1047_26879eb73d9546c1a957bf63dd4cvide.html?_wv=2281701505&sig=0088d007af4c3ea6e2d0ab6251fd506f&time=1546704590&web_ch_id=105'
#
# r = requests.get(url)
#
# soup = BeautifulSoup(r.text, 'html.parser')
#
# video_src = soup.find(id='video-play').get('data-video-src')
# title = soup.find(id='mod-common').get('data-article-title')
# video = requests.get(video_src, stream=True)
#
# if not os.path.exists(_base_dir):
#     os.mkdir(_base_dir)
# file = open('{}/{}.mp4'.format(_base_dir, title), 'wb')
# shutil.copyfileobj(video.raw, file)


@mp_qq.route('/dl')
def dl():
    return render_template('mp_qq.html')

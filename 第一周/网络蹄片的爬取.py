import requests
import os
def picture_spider():
    """
    网络图片链接的格式：http://www.example.com/picture.jpg
    获取图片地址的方式：右键图片-->复制文件地址
    :return:
    """
    url = 'https://cdn.pixabay.com/photo/2019/08/16/20/18/ceramic-4410990_960_720.jpg'
    root = "F://Spider_picture/"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        else:
            print('文件夹已经存在')
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print("文件已经存在")
    except:
        print('download_failure')


def video_spider():
    """
    网络视频链接的格式：http://www.example.com/picture.MP4
    获取视频地址的方式：右键视频-->复制文件地址（好看视频为例）
    :return:
    """
    url = 'https://vd3.bdstatic.com/mda-jh6fuawmpe2t5qc7/sc/mda-jh6fuawmpe2t5qc7.mp4'
    # url = 'https://vd3.bdstatic.com/mda-jh6fuawmpe2t5qc7/sc/mda-jh6fuawmpe2t5qc7.mp4?' \
    #        'auth_key=1566452384-0-0-9a3ec0266e653c60fa34b35d8a0c4402&bcevod_channel=searchbox_feed&pd=unknown&abtest=all'
    root = "F://Spider_video//"
    path = root + '哪吒.mp4'
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        else:
            print('文件夹已经存在')
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print('文件保存成功')
        else:
            print("文件已经存在")
    except:
        print('download_failure')

video_spider()

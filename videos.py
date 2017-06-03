import numpy as np
import tensorflow as tf
import youtube_dl
import pafy
import sys


def Length(url):
    try:
        video = pafy.new(url)
        return video.length
    except:
        return -1



path = sys.argv[1]
for example in tf.python_io.tf_record_iterator(path):
    result = tf.train.Example.FromString(example)
    v_id = result.features.feature["video_id"].bytes_list.value[0].decode("utf-8")
    tags = list(result.features.feature["labels"].int64_list.value)
    length = Length("https://www.youtube.com/watch?v={}".format(v_id))

    print(v_id)

    if length == -1 or length > 150:
        continue

    try:
        ydl_opts = {'format':'135+140'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                "https://www.youtube.com/watch?v={}".format(v_id), download=True)
    except:
        continue


    f = open("save.txt", "a")
    tags_str = ','.join([str(t) for t in tags])
    f.write("{} [{}] [{}]\n".format(v_id, tags_str, meta['title'], meta['description']))
    f.close()

# Sample-Youtube-Video-Downloader

## Description:

Downloads sample Youtube videos from [Youtube-8M](https://research.google.com/youtube8m/), and stores information (title, description and tags; could be extended via `youtube-dl` metadata options to extract more info) in a text file.

## Dependencies:

* Numpy
* Pafy
* Tensorflow (CPU-only version adequate)
* Youtube-dl

## Setup

You can automatically download the videos-urls as Tensorflow Records with the script (`download.py`, located at the "Download" page of YT-8m) provided on their page. You will run the script to download the training data (from the "Video-level features dataset") with the instructions on their site (the ones right at the bottom of the page) and you will download many tf_records files (for example, `train0_.tfrecord`). After you've downloaded them, run `videos.py`, passing as argument the records file you want to extract. The videos and extracted info will be stored in that directory.

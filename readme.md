# AVSBench-semantic Dataset Readme

### Files

* `v1s.zip` , `v1m.zip`, `v2.zip` (all required): extracted frames, annotated labels, audio
  * `file- audio.wav` : audio in video
  * `dir- frames`: extracted frames from raw video (1 fps)
  * `dir- labels_rgb`: annotated frames in RGB format
  * `dir- labels_semantic `: annotated frames in Label Index format
* `metadata.csv`(required): metadata file
  * `vid`: YouTube video id
  * `uid`: unique data (video segment) id
  * `s_min` , `s_sec`: start time of video segment in YouTube video
  * `a_obj`: label of sounding object(s)
  * `split`: dataset split from (train, val, test)
  * `label`: data source id from (v1s, v1m, v2)
* `label2idx.json` (required): label to index mapping
* `raw_video_data.zip` (option, ~210GB): raw video data



### Download Links

- Baidu Netdisk: https://pan.baidu.com/s/16GOnun4A79ffCDMCXMvI0w?pwd=ez4i (ez4i)
- Dropbox: https://www.dropbox.com/sh/oaeiylix0jjjawu/AAApc245zlwF5f5EqVz_Ym8Ua?dl=0
- OneDrive: https://1drv.ms/u/s!AmFC2hZytlk8goBZ1Qbl2D1GYRQmcQ?e=EPMzOC

Note: `raw_video_data.zip` is only available in Baidu Netdisk. 



### Useful Links

* **Arxiv Paper**: https://arxiv.org/abs/2301.13190
* **Project Page**: http://www.avlbench.opennlplab.cn
* **Github Repo**: https://github.com/OpenNLPLab/AVSBench



### MD5 checksum

* `v1s.zip` 5bc92469e021833d156e01be3817cca0
* `v1m.zip` af46c657786098f53e82c1c36ea64980
* `v2.zip` 85164ddd0896501f2fe4ae1dc405f1b3
* `raw_video_data.zip`  55c89c8da35a36ed6c1f5555f38d65a6



### Updates

**Latest Version:  Jan 9, 2022. Public V0.1**

1. v0.1 <Jan 9, 2022>: initial publication



### Copyright

**[Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/)**


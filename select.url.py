#! /usr/bin/env python3

from qutescript import userscript
import rofi 
import youtube_dl


@userscript
def sorter(request):
    if 'youtube' in request.url and 'watch' in request.url:
        # res = []
        # ydl_opts = {}
        # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #     meta = ydl.extract_info(
        #         request.url, download=False) 
        #     formats = meta.get('formats', [meta])
        #     for f in formats:
        #         res.append(f)

        # res = [f for f in res if f.get('height', 0) <= 1080 or f.get('height', 0) >= 720]
        # r = rofi.Rofi()
        # i, key = r.select(
        #     'YTDL Format',
        #     [f['format'] for f in res])

        # request.send_command(
        #     "message-info 'playing " +
        #     request.url.split('/')[3] +
        #     " at " + str(res[i]['height']) + "p'"
        # )
        request.send_command(f'spawn mpv --ytdl-format="best[height<1100]" {request.url}')
    else:
        request.send_command('open ' + request.url)



if __name__ == '__main__':
    sorter()

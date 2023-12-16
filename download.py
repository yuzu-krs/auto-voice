import tkinter as tk
from tkinter import simpledialog
from yt_dlp import YoutubeDL
import os
import subprocess

def get_youtube_url():
    root = tk.Tk()
    root.withdraw()

    url = simpledialog.askstring("YouTube URL", "ダウンロードしたいYouTube動画のURLを入力してください:")

    return url

def run_inference(input_file):
    # コマンドの組み立て
    command = f"python inference.py -i \"{input_file}\""
    
    # コマンドを実行
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"エラーが発生しました: {e}")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

def main():
    # YouTubeからのダウンロード
    url = get_youtube_url()
    urls = [url]
    ydl_opts = {
        "format": "mp3/bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download(urls)

    # ダウンロードした mp3 ファイルに対して inference.py を実行
    latest_mp3 = None
    for filename in os.listdir():
        if filename.endswith(".mp3"):
            print(f"Running inference for: {filename}")
            run_inference(filename)
            latest_mp3 = filename

    # 最後にダウンロードした mp3 ファイルを削除
    if latest_mp3:
        os.remove(latest_mp3)

if __name__ == "__main__":
    main()
from pytube import YouTube

def index_post():

   yt = video_url = str("https://www.youtube.com/watch?v=QsZ0g61Ymhc")
   yt = YouTube(yt)
   print("1")
   video = yt.streams.filter(only_audio = True).first()
   print("2")
   destination = '.'
   out_file = video.download(output_path = destination)

def main():
    index_post()

if __name__ == "__main__":
    main()

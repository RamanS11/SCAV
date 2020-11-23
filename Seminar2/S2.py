import os
import shutil

def cut(time1, time2, in_name, out_name):
    # Cut the video two times, one from time1 and go on, and the other in the opposite way, and then we have
    os.system("ffmpeg -ss " + time1 + " -i "+in_name+" -to " + time2 + " -c copy "+out_name)
    os.system("ffmpeg -i "+in_name+" -ss " + time1 + " -to " + time2 + " -c copy "+out_name)

def YUV_hist(video):

    os.system('ffplay '+video+' -vf "split=2[a][b], [b]histogram, format = yuva444p[hh], [a][hh]overlay"') # Get the histogram and display both.

def resize(video):

    scale = ['1280x720', '640x480', '360x240', '160x120']           # Create arrays to iterate over them.
    out = ['BBB_cut_1280x720.mp4', 'BBB_cut_640x480.mp4', 'BBB_cut_360x240.mp4', 'BBB_cut_160x120.mp4']
    aux = 0

    for i in scale:                                             # Iterate over the arrays and store the videos with different qualities.
        os.system('ffmpeg -i '+ video +' -vf scale='+ i +' '+ out[aux])
        aux += 1


def change_audio_codec(video, codec, out_video):

    os.system('ffmpeg -i '+ video +' -acodec '+codec+' -vcodec copy '+out_video)


def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Cut 10 seconds of the video")
    print("2. Show the histogram in YUV alongside the video")
    print("3. Resize Videos with different qualities")
    print("4. Change the codec")
    print("5. Exit")
    print(67 * "-")

def main():

    time1 = "05:25"
    time2 = "05:35"
    in_name = 'BBB_short.mp4'
    out_name = 'cut_BBB.mp4'

    loop = True

    while loop:  # While loop which will keep going until loop = False
        print_menu()  # Displays menu
        choice = int(input("Enter your choice [1-5]: "))

        if choice == 1:
            print("Cut 10 seconds of the video")
            cut(time1, time2, in_name, out_name)
        elif choice == 2:
            print("Show the histogram in YUV alongside the video")
            YUV_hist(out_name)
        elif choice == 3:
            print("Resize Videos with different qualities")
            resize(out_name)
        elif choice == 4:
            print("Change the codec")
            codec = 'mp3'
            o_name = 'BBB_codec_changed.mp4'
            change_audio_codec(out_name, codec, o_name)
        elif choice == 5:
            print("Menu 5 has been selected")
            loop = False  # This will make the while loop to end as not value of loop is set to False
        else:
            print("Wrong option selection. Enter any key to try again..")


main()

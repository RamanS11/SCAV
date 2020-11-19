import os

def get_Codecs(video_info, summary):

    file = open(video_info, 'r')                # Open the file with all the video information.
    z = 'Stream'
    summary.write("Codecs used in the video :\n")

    for line in file:                           # Find the codecs used by searching where the line starts with a 'Stream' string.
        if z in line:
            summary.write(line)                 # Copy the information in the text file that store this information

    file.close()                                # Close the information file.

def get_Info(video_info, summary):

    file = open(video_info, 'r')                # Open the file with all the video information.
    z = 'Duration'
    summary.write("Other relevant information:\n")

    for line in file:                           # Find relevant information related to Duration, bit rate ... by searching the line that starts with 'Duraton'.
        if z in line:
            summary.write(line)                 # Copy the information in the text file that store this information
            break

    file.close()                                # Close the information file.

def store_info(vid_name, file):
    path = os.path.split(os.getcwd())               # Go to get the video information at the SCAV directory.
    os.chdir(str(path[0]))
    os.system('ffmpeg -i '+vid_name+' 2> '+file)    # Create a file that stores all the video information.

def main():

    vid_name = 'BBB.mp4'
    out_file = 'info_BBB.txt'
    summary_file = 'summary_info.txt'

    store_info(vid_name, out_file)              # Call the function that creates the information file.
    os.system("touch "+summary_file)            # Create a file where we will store a short version of the video information.

    summary = open(summary_file, 'w')           # Open the file previously created and fill with the important information
    get_Codecs(out_file, summary)
    get_Info(out_file, summary)
    summary.close()                             # Close the file.

    os.system("rm "+out_file)                   # Delate the large text file with all the video information.
    path = os.path.split(os.getcwd())                       # Go to get the summary with the video information and move it
    os.system('mv '+summary_file+' '+os.getcwd()+'/Lab2')   # to Lab2 directory.

main()

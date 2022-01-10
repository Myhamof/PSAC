# PSAC - PS avatar creator:
much easier to create custom avatars for the PS
# requirements:
1. python 3
2. wand
3. in windows "ImageMagick" you to install it follow the instruction from this link "https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows" and on Linux "libmagickwand-dev" or you can just use the colab
# useage:
you have 2 options:
1. running localy on your computer
2. use google colab
# running localy on your computer:
1. create a new folder
2. create a copy of the image you want as your avatar and put it in the folder (the program will overwrite the file and convert it to 440 * 440)
3. rename it to "avatar.png" (The program assume you using a .png file and will crash if you use another extension, you can just change the extension to .png and the program will convert it to real png when needed)
4. after you start the program you can just type the path to the image or just drag and drop the image on the console.
5. the program will close and the folder will populate with the avatar file.
#google colab
1. run the cells
2. on the third cell upload the image (the program asume you are using .png file, rename the extention if needed the program will rencode it as a real png file)
3. wait for it to finish and using the next cell download all the images as a zip file

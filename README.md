# OpenCV-Air-Canvas

This is an air canvas built exclusively through python opencv. This lets us take real-life colored pens/markers, and allows us to draw that color on a webcam feed. The utility in this is limited in its current state, but as a concept, air canvases are a demonstration of activities that have traditionally required touch to perform. My hope is that this project can inspire me, and others, to create more accessible means of human input.

# Some Limitations

There are currently a lot of limitations of this air canvas:

- There are only some types of colors supported, and only more vibrant colors are really responsive.
- The brightness, and background, must be optimal for this to work the best.
- There is no convenient way to save the work, we must use the snipping tool to screenshot the frame that the canvas is on, or we must quit our application (by pressing q) and it will save our image then. I will work on a keylogger to take some input to save the image during use.

# Dependencies

This can be built on any python version 3.7+, and using the following packages:

- OpenCV-python (4.5.5.62 is my version)
- numpy (1.20+ is fine)

# Contact

Please contact me at andrewjych@gmail.com if you want to collaborate or suggest improvements to this project, or others. I am always available to talk code or whatever else with you.

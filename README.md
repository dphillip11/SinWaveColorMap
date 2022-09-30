# SinWaveColorMap

A tool for manipulating sin waves to produce color map LUTs that can be applied to graphs and images. The tool relies on matplotlib for the GUI and openCV for saving the colormap thus avoiding some awkward file formats.

As part of my work on the mandelbrot web app I utilised a simple trick for producing randomised color maps. I decided a graphical representation of this might be nice.

You can use this tool to create custom cuslor maps by tweaking the parameters of three sine waves, one for each of the RGB values. 

![screenshot1](https://user-images.githubusercontent.com/109744044/193224448-00ebc326-10cf-4151-bd17-b32e244e1b5c.jpg)

The colormap is easily saved and applied to images or graphs as can be seen in the next screenshot
![Screenshot2](https://user-images.githubusercontent.com/109744044/193224465-135b5fe2-6577-4b7e-afce-c078d75f3224.jpg)

## About:

The main challenge encountered in this project was gaining familiarity with the matplotlib library. I chose this library as the GUI is more or less intended for the purpose of maniulating graphical data and sliders and buttons are convenient to add. I chose to wrap all of the individual wave properties into a wave class that can then simplify running a number of tasks including generating values using the function attributed to the wave and its parameters, generating a 2D line object for each line and updating the parameters as necessary. It would also be easily facilitated by this design to add alternative functions that could be used to create different results, maybe some step functions, linear or asympototic functions could be interesting or maybe allowing the user to draw a line manually would allow for more control.

The update function that is called when a change happens on the display is based on mouse movement. I chose this over slider movement simply to neaten the code but given sufficiently large images it would be wise to change this. I made this choice because the intention is for the colormap to be created not necessarily applied. It is however possible to save a colormapped image withing the program by setting the check_LUT save parameter to 1. 

The tool is intended primarily for data scientists as opposed to artists in that it can be useful to have attractive graphs when presenting information and it is best if they adhere to some color scheme. As a branch from my Numbabrot project however it can be applied to images of the mandelbrot set, I have seen good software that actually does exactly this. In its current format however I think the tool offers greater utility. I also enjoy the tactile nature of color manipulation in this format whilst hopefully still being approachable, of course photo editing software incorporates a more varied use of color tools but possibly at the expense of accessibility. The libraries chosen are likely familiar to many data scientists using python.

A potential road for further development may be in converting the tool into a graphical way of tuning a PID filter reliant upon steady feedback from onboard sensors.

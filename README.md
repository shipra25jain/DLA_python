# DLA_python
Diffusion Limited Aggregation for point attractor
A breif explanation about DLA can be found here : http://paulbourke.net/fractals/dla/
The attached file DLAgif.py generates gif which simulates DLA for the given input image
dimensions, number of iterations and stickiness.
Default parameters :
Image Dimension(d) = 201
Number of iterations(n) = 5000
Stickiness(s) = 1
In order to generate gif with different parameters, run the simulateDLA.py with command line
arguments :
Python simulateDLA.py -d 501 -s 0.5 -n 20000
The dlaoutput.png image will be saved on the system

To estimate the stickiness for DLA simulation, use “estimateStickiness.py” with input image file path as
command line argument :
python estimateStickiness.py -f dlaoutput.png

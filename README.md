<!DOCTYPE html>
<html>
<head>
<title>Pose Estimation Classifier</title>
</head>
<body>

<h1>Pose Estimation Classifier</h1>

<p>This Python script estimates whether a person in an image is sitting or standing based on pose landmarks. It uses the MediaPipe library for pose estimation.</p>

<h2>Requirements</h2>
<ul>
<li>Python 3.x</li>
<li>OpenCV</li>
<li>MediaPipe</li>
</ul>

<h2>Installation</h2>
<p>You can install the required packages using pip:</p>
<pre>pip install opencv-python-headless mediapipe</pre>

<p>Clone the Repository:</p>
<pre>git clone https://github.com/tejasram2003/Pose_Estimation.git</pre>

<h2>Usage</h2>
<p>To run the script, use the following command:</p>
<code>python main.py --image_path path_to_image.jpg --threshold threshold_value</code>

<p><strong>--image_path</strong>: Path to the input image.</p>
<p><strong>--threshold</strong>: Threshold for classifying sitting or standing (default is 0.1).</p>

<p>The script will display the annotated image with the classification result. The image will be annotated with the output and saved in a directory named 'Outputs'.</p>

<h2>Example</h2>

<p><strong>Sitting:</strong></p>
<pre>python main.py --image_path images/sitting.jpg --threshold 0.1</pre>

<img src="https://ik.imagekit.io/tejasram/sitting.png?updatedAt=1694442950156" width="350" alt="sample output">

<p><strong>Standing:</strong></p>
<pre>python main.py --image_path images/standing.jpg --threshold 0.1</pre>

<img src="https://ik.imagekit.io/tejasram/standing.png?updatedAt=1694442950062" width="350" alt="sample output">


<h2>Customization</h2>
<p>You can customize the script by adjusting the threshold value in the code to achieve the desired classification sensitivity.</p>

<h2>Acknowledgments</h2>
<ul>
<li><strong><a href="https://mediapipe.dev/" style="text-decoration: none;">MediaPipe</a></strong>: Used for pose estimation.</li>
</ul>

<h2>Contact</h2>
<p>If you have any questions or suggestions, feel free to contact me at <a href="mailto:tejasram03@gmail.com">tejasram03@gmail.com</a>.</p>

</body>
</html>

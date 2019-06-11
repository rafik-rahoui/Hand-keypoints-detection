# Hand-keypoints-detection

 
<div align="center">
   <img src="/HKD.gif", width="300">
</div>
<br>
<br>
<h2>The pipeline:</h2>
<h4> My process of detecting hand keypoints with a camera respects the following architucture :</h4>
 <div align="center">
    <img src="/pipeline.jpg", width="1000">
 </div>
<br>
<br>

<p>⁃ The image is grabbed by the camera;</p>
<p>⁃ A first deep learning model detects the hand on the image and estimates the coordinates of the box around it (done by retraining tensorflow object detection API on hand detection, you could also achieve it by building a custom deep learning model);</p>
<p>⁃ A second deep learning regression model takes the image inside the box and estimates the coordinates of all hand keypoints (achieved by transfert learning from a resnet34 with a custom head).</p>

<br>
<br>
<h2>Hand detection :</h2>
retraining a tensorflow's object detection model (trained on COCO dataset) on hand detection dataset. I picked MobileNet_v2 for speed.
In case you are using Open Image dataset, I wrote a custom script to convert the data to the required format.
<br>
<br>
<h2>keypoints detection:</h2>
Fine-tining a resnet34 model with Fastai. the full code in the note book.

<h2>Citing this work:</h2>
If you use this code and would like to cite this work, use the below:
<br>
rafik Rahoui: Hand keypoints detection using Convolutional Neural Networks, https://github.com/rafik-rahoui/HKPD

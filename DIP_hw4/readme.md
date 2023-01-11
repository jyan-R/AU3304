### Dependency
*Image Processing and Computer Vision Toolbox*

### Algorithm Execution Process
1.	Determine the area of motherboard in the template image, construct a template bounding box.
2.	Convert the rgb-images into grayscale.
3.	Apply KAZE to find key points and extract their feature vectors on video-capture images and the template image.
4.	Apply nearest neighbor algorithm to match the two feature vectors set. 
5.	Estimate the geometric transform and eliminate the wrong matches.
6.	Transform the template bounding box and bound the motherboard in the test image.

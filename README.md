<h1>Overview</h1>
This was a project I did for a class in image processing. 

Basically it uses a trained neural network to recognize the gestures. I started off with collecting image datasets from online resources. Then I created a script to generate my own data. The scripts will standardize all the collected and covered data to 32x32 resolution with a canny filter applied for gesture feature enhancement.

Once the data is collected and standardized, it is used for training the neural network created with Tensorflow. And then this trained model is saved as a JSON file.

Finally this training data is used to make live predictions.

<h3>Description of Files :</h3>

Converter.py:  used for converting pre existing datasets that can be found on kaggle and elsewhere. The parameters in the converter script can be changed and set to different standard. However it would be better to set a uniform standard throughout your data by accordingly adjusting the parameters of the rest of the scripts.

data-generator.py: used for generating custom data. This script will create directories for all the letters under the ‘train’ and ‘test’ folders. Just change switch between the two to store the collected data in the corresponding folders.
Once this script is run, a single standardized and processed 32x32 frame can be collected by pressing the corresponding button on the keyboard. Like for example if you are collecting data for ‘a’, just make the shape and press the key ‘A’ on your keyboard and it’ll save that frame under the (train or test)/a/frame1.

train.py -  Once all the data is ready and well placed in the previously created directory system, simple run this script to train the neural network. Make sure you change the number of training and test images in the commented regions. You can also tweak the neural network as you wish to get better accuracy.

The trained model will be saved as a JSON file.

predict.py -  This script will use the saved model data to make predictions with data being captured from a webcam via OpenCV. 

All the scripts are customizable and 

model-asl-bw.h5, model-asl-bw.json - Saved model for making predictions - used around 10,000 training images and 4000 test images with an accuracy of about 96% and validation accuracy of about 86%.
As I mentioned tweaking the Neural Network might yield better results.
NOTE:  Training these networks on potato computer will take a lot of time. Took me a decent amount of time to train this model even though I used tensorflow-gpu.

<h3>Future Work:</h3>
- I would like to add j and z
- Imporve accuracy under variable environmental conditions
- Implement it in a Python based embedded system like Anki Cozmo/Vector to help people learn ASL.

Let me know if you have any question or queries at vakarahmed59(at)gmail(dot)com.

# YOLO Object Detection using cvzone

This Python script utilizes the YOLO (You Only Look Once) model from Ultralytics, along with the cvzone library, for real-time object detection on video frames captured by the computer's camera.

## Requirements
- Python 3.6 or higher
- Install required libraries using the following:
  ```bash
  pip install opencv-python
  pip install cvzone
  pip install torch
  pip install numpy
  pip install torchvision
Usage
Make sure you have the required Python libraries installed.
Download the YOLO model weights file ("best.pt") and place it in the same directory as this script. You can find the weights file here.
Run the script, and a window will appear showing the video feed from your camera with object detection results overlaid.

Google Drive Dataset
To use your Google Drive as a dataset source, follow these steps:

Open the Colab notebook provided click [here](https://colab.research.google.com/drive/1fKqnTzuA_wGMzEiFRN5T_BwBgTWXcvna#scrollTo=87JOCmVGWDBj)

Mount your Google Drive using the following code snippet:

python
Copy code
from google.colab import drive
drive.mount('/content/drive')
Upload your dataset to Google Drive. Ensure that your dataset is organized appropriately.

Update the code in the provided Colab notebook to point to your dataset location on Google Drive.

For example:

python
Copy code
dataset_path = '/content/drive/MyDrive/Your_Dataset_Folder'
Replace "Your_Dataset_Folder" with the actual folder name where your dataset is located.

Continue with the notebook's instructions to train your model using the provided dataset.

Data Explanation
The dataset is organized in the Google Drive folder specified in the YAML file. The structure of the dataset should follow these guidelines:

Training Data: The training images should be located in the directory specified by the train field in the YAML file (../train/images). These images should cover a variety of scenarios and examples of the object you want to detect (in this case, an 'eye').

Testing Data: Similarly, the testing images should be in the directory specified by the test field in the YAML file (../test/images). This set of images is used to evaluate the model's performance on data it hasn't seen during training.

YAML File Explanation
The YAML file (../drive/MyDrive/eye-detection) contains configuration information for the YOLO model. Here's an explanation of the key fields:

path: This specifies the directory path where your dataset is located. In this case, it is set to ../drive/MyDrive/eye-detection.

train: Specifies the relative path from the dataset path to the directory containing training images. In this example, it is set to ../train/images.

test: Specifies the relative path from the dataset path to the directory containing testing images. In this example, it is set to ../test/images.

nc: Stands for the number of classes. In your case, it's set to 1, indicating that you're detecting one class ('eye').

names: Provides the names of the classes. In this case, there's only one class, and it is named 'eye'.

Make sure to replace the placeholder names and paths with the actual folder and file names you are using in your project. Additionally, the Colab notebook provided seems to guide users on how to mount Google Drive and train the model using the specified dataset.



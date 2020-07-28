# Voice-assisted-home-automation

Online mobile application which helps the users to operate their electrical appliances from anywhere they can.


## Prerequisites

- Flutter git Repository 
- Android SDK installed on computer for android build
- Android emulator or a developer options enabled android device for android build
- IOS emulator or IOS device for IOS build
- Firebase project for Firestore database


## How to run Flutter App:

- First, to get all the packages required to run the flutter app, run command 'flutter get packages' in the terminal.
- Once it is completed, attach a android device or emulator.
- Now run command 'flutter run' in the folder where pubspec.yaml is present
- Now you just have to wait for few minutes(sometimes it take more time) to build the android build and install apk in the connected device
- Press 'r' to hot-reload the app and updating the modifications into the installed build apk in the device
- Press 'R' to restart the app

## Libraries required to run the python file:

- face-recognition
- docopt
- dlib
- sklearn
- firebase_admin

## How to run python file:

- First, we need to install all the required libraries.
- Once, the installation is completed run command 'python face_recognize.py -d train_dir -i test_image.jpg' in the terminal
- After the execution, name of the identified person is sent to firestore database.

 

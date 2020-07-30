# Voice-assisted-home-automation

Online mobile application which helps the users to operate their electrical appliances from anywhere they can.


## Prerequisites

- Flutter git Repository 
- Android SDK installed on computer for android build
- Android emulator or a developer options enabled android device for android build
- IOS emulator or IOS device for IOS build
- Firebase project for Firestore database
- Node.js for notifications
- Run npm install -g firebase-tools for installing firebase CLI.

## How to run Flutter App:

- First, to get all the packages required to run the flutter app, run command 'flutter get packages' in the terminal.
- Once it is completed, attach a android device or emulator.
- Now run command 'flutter run' in the folder where pubspec.yaml is present
- Now you just have to wait for few minutes(sometimes it take more time) to build the android build and install apk in the connected device
- Press 'r' to hot-reload the app and updating the modifications into the installed build apk in the device
- Press 'R' to restart the app

## How to run the notification app

- After installing firebase CLI , run the command 'firebase login' in the command prompt
- Then login into the account in which you have created your firebase project following the instructions given in the command prompt
- After the login is successfully completed , create a folder for the notification app
- Go into the app folder and run the command 'firebase init'
- In the command prompt, it will ask to select the existing project press enter 
- choose javascript as the coding language 
- press enter then few files will be created in the folder
- Go to the functions folder and write the code in the index.js file using any editor of your choice
- After completion of writing the code go to the functions folder in the app and run 'firebasae deploy' in the command prompt.

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

 

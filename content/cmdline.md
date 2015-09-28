Title: Creating Android Application via Command Line
Date: 2014-12-04 10:59
Modified: 2014-12-04 10:59
Category: Android
Tags: android
Slug: andoridcmd
Authors: Vengatesh.S
<!-- Summary: Creating and Building android application -->

Android application can be can be created either by using IDE or via Command Line interface.

####Requirements:
* Android SDK
* IDE (Eclipse or Android Studio)  or
* Text Editor

####Setting up the Work Environment:
1. Download Android SDK:
First you have to download the latest version of the Android SDK which is available in http://developer.android.com/sdk/index.html

2. Adding PATH to Environment Variable:
Extract the Android SDK in a specific location. And add the following directories to the PATH environment variable.
	* /path/to/android/sdk/tools
	* /path/to/android/sdk/platform-tools

####Creating an Android Project:
To create a new android project, open a command-line and type:

   android create project --target <Target ID>
                --name <project_name>
                --path path/to/your/project
                --activity <activity_name>
                --package <package_name>
                        --gradle (optional)
                        --gradle-version <version> (optional)

* `target` - build target for your application
* `name` - is the name for your project
* `path` - location of your project
* `activity` - is the name for your default activity
* `package` - is the package namespace for your project    

#####Example:

   android create project --target android-21
                        --name HelloWorld
                        --path .
                        --activity MainActivity
                        --package com.example.helloworld 

####Creating Android Virtual Device:
Android Virtual Device Manager provides a graphical user interface in which you can create and manage Android Virtual Devices (AVDs), which are required by the Android Emulator.

To Create Android Virtual Device:

   android create avd --name <emulator name>
                    --target <target ID>

* `emulator name` is the name assigned to AVD
* `target ID` is android API version 

#####Example:

    android create avd --name Lollipop
                    --target android-21		

####Starting AVD:
To start the created AVD, run the following command:

   emulator -avd <emulator-name>

#####Example:

   emulator -avd Lollipop

####Building Android Project:
To build your Android Project in debug mode:
1. Open a command-line and navigate to the root of your project directory.
2. Use Ant to compile your project in debug mode:

   ant debug


This creates your debug `.apk` file inside the project bin/ directory, named `<your_project_name>-debug.apk`.

####Installing .apk file in emulator:
Before installing .apk file in emulator, make sure that Android emulator is running and then install the .apk file.

    adb install <.apk file>



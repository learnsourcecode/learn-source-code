Title: Building Mobile apps using Cordova
Date: 2014-12-10 03:17
Modified: 2014-12-10 03:17
Category: Android
Tags: android
Slug: cordova
Authors: Vengatesh.S
<!-- Summary: Creating and Building Mobile apps using Web Technologies -->

Apache Cordova is an open source mobile development framework. It allows you to develop mobile application using web technologies such as HTML, CSS and JavaScript. Using Cordova APIs you can able to create apps without any native code such as Java, Ojective-C etc., Instead of using native code, Cordova uses the HTML, CSS and JavaScript to develop mobile apps.

####Supported Platforms:
Cordova Supports various platforms like:

* iOS
* Android
* Blackberry
* Windows Phone
* Bada
* Symbian

####Requirements:
* Node.js
* Cordova packages
* Command Line Interface

####Setting up the Environment:
* Download and install Node.js.
* Using `npm` install the Cordova package.

  sudo npm install -g cordova

####Creating an App:
Go to the directory where you want to create your project and run the following command:

   cordova create Hello com.example.hello HelloWorld

* `Hello` specifies the name of the directory.
* `com.example.hello` specifies the package name of your project.
* `HelloWorld` specifies the Application name of your project.

After creating, your project will contains various files and directories namely:

* `config.xml` is the configuration file of your project source.
* `platforms` is the directory which contains all you added platforms.
* `plugins` contains all your added cordova plugins
* `www` is the source directory which contains HTML,CSS and JavaScript files.

####Adding Platforms to your project:
Before building your project, you need to make sure you have already installed supported SDKs and then you need to specify the target platforms using the following commands:

    $ cordova platform add ios
    $ cordova platform add android
    $ cordova platform add blackberry10
    $ cordova platform add firefoxos

Run this command to list all your targeted platforms:

    $ cordova platforms list

You can also remove the target platforms using:

    $ cordova platform remove ios

####Build:
To Build your project, create a HTML file called `index.html` and place it in the directory `www`.

Run the following command to build the project:

    $ cordova build


To install or run your project:

   $ cordova run --emulator


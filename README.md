Write about plugin usage in here  and put images in the image folder only .
Try to be very descriptive and make sure each and every functionality of that task is included. 
Mentioned below instructions will give you the files that will be chnage according to your plugin.
NOTE:Please delete me and add description of your plugin on this README File. FOR this plugin skeleton we are using xlr plugin. 

======================================================================================
Ingredients for plugin development  
Plugin Development all start with a Repository creation in your local system .There are some standards enforced by the XebiaLabs for the naming conventions as follows 
If your repository is a plugin for XL Deploy, the repository name should start with xld. 
If your repository is a plugin for XL Release, the repository name should start with xlr. 
If your repository is a plugin, the repository name should end with plugin 
For example: xld-openshift-plugin, xlr-sonar-plugin, xlr-servicenow-plugin(include tile dasboard) 
 
Each repository must include license in the root repo or in the source folder. Folder structure looks like as below 
xld-plugin_name-plugin/src/main/license/xebialabs_community.license 
xlr-plugin_name-plugin/src/main/license/xebialabs_community.license 
 
 ==================================================================================
Gradle/wrapper(folder) : Using a Gradle wrapper ensures that the same Gradle version is used for build or travis-ci(Xebialabs CI tool for plugin build). You can copy gradle wrapper from any existing plugin in community or create one with same contents as shown below. This folder consists of two files: 

gradle-wrapper.jar  (copy from existing plugin) 
gradle-wrapper.properties : 
  
distributionBase=GRADLE_USER_HOME 
distributionPath=wrapper/dists 
zipStoreBase=GRADLE_USER_HOME 
zipStorePath=wrapper/dists 
distributionUrl=https\://services.gradle.org/distributions/gradle-2.7-all.zip 

=======================================******=========================================
image folder(optional) : It’s a clean way to put screenshots of the plugin interaction with XL tools and configurations in a single place .  
 ============================================================================
.gitignore :  .gitignore ignore these file in the build process. Contents as follow: 
.gradle 
.idea 
build 
xlr-plugin_name-plugin.iml 
src/downloads/* 
*.ipr 
*.iws 
Supervisord.log 
NOTE: no change needed, remains same. 
===============================**********===================================
 
settings.gradle:  settings.gradle consist of rootProject name as follow: 
rootProject.name = 'xlr-plugin_name-plugin' 
========================================================================
gradlew(unix) and gradle.bat (windows):  These are gradle startup script for unix and windows . Copy both the files as it is from one of the existing plugin. 
=========================================*******====================================== 
README.md:  Describe the functionality provided by the plugin.
====================================================********============================  
build.gradle:  build.gradle is a build configuration script. The build script defines a project and its tasks . Make sure to change the version to the plugins existing version depends if it is new plugin or extended one. 
===============================================*********================================== 
.travis.yml file :  Non-xebia developer can ignore this part . Go to Travis CI and log in with your GitHub account. After you log in, you’ll see the community plugins being built. The build configuration is located in the .travis.yml file in each repository. Copy this file from existing plugin and change plugin name to the name of the plugin. 
file: build/libs/xlr-plugin_name-plugin-x.x.x.jar   
 repo: xebialabs-community/xlr-plugin_name-plugin

 
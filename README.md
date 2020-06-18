# Automation of Stacky Bird
Python program to automate the mobile app of Stacky Bird

# Setup
## Android Platform Tools
### Mac OS X
This was an absolute nightmare to get working on my oldschool Macbook Pro  
The "plug and play" method below didn't work initially for me:
```brew cask install android-platform-tools```
So I had to use:
```<code>```
Then I had to amend the bash profile on my mac.  First I opened the bash_profile in my 
usual code editor by running the below in my terminal:  
```code \~/.bash_profile```
Then below my other exports (I had a couple for Python), I added the following two lines:  
```
export PATH=~/Library/Android/sdk/tools:$PATH  
export PATH=~/Library/Android/sdk/platform-tools:$PATH
```

## Debugging Mode

## Screen Mirroring


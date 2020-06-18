# Automation of Stacky Bird
Python program to automate the mobile app of Stacky Bird

# Setup
## Android Platform Tools
### Mac OS X
This was an absolute nightmare to get working on my oldschool Macbook Pro  
The "plug and play" method below didn't work initially for me:  
```
brew cask install android-platform-tools  
```  
So I had to use:
```
<code>  
```  
Then I had to amend the bash profile on my mac.  First I opened the bash_profile in my  
usual code editor by running the below in my terminal:  
```
~/.bash_profile  
```  
Then below my other exports (I had a couple for Python), I added the following two lines:  
```  
export PATH=~/Library/Android/sdk/tools:$PATH  
export PATH=~/Library/Android/sdk/platform-tools:$PATH  
```  
Then returning back to the terminal, I ran:  
```  
source ~/.bash_profile  
```

## Debugging Mode
In order for the adb program to be able to read the android device, debugging mode needs to be switched on.  Simply:  
- [ ] Go to Settings  
- [ ] Go to About Phone
- [ ] Go to Software Information
- [ ] Click on Buid Number 7 times
- [ ] Return to Settings menu and scroll further down to Developer Options
- [ ] Activate USB debugging
- [ ] Optional - Activate Pointer location so you can see x,y co-ordinates

## Screen Mirroring
There are a number of ways to get this working on Windows, Mac OS X and Linux.  The most popular seems to be:  
- scrcpy
- GenyMotion
- Vysor
- Apowermirror  
I could only get the last one working easily.  I had installation issues with scrcpy (again, oldschool Macbook Pro and compatiblity issues...) and I read a whole list of adb client/server incompatibilities with GenyMotion.  Again, I also had issues with Vysor by being stuck at a "Waiting for decoder" issue so I abandoned that ship as well.  


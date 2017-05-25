#Summary

Adds a command to Sublime Text 3 that replaces all curly single and double quotes with straight single and double quotes, respectively.

#Installation: 

Make new folder `Straight Quotes` in  `<user>/Library/Application Support/Sublime Text 3/Packages/`.  Dump all these files into it.

#Usage

Summon the command window `Command + Shift + P`. Type `Straight Quotes`.  Hit `Enter`.  Your open document will be fixed.

#Troubleshoot

##"Straight Quotes" is not listed in the command window.

	* Package might not be installed in the right directory.  There are many package directories, some for zipped packages, some not.  Refer to Installation instructions.

	* If ST3 sees a syntax error (in the *.py file) it will hide the package from you.  Edit and save the *.py.  If you fix the syntax error the package will immediately appear when you hit save, no need to quit and reopen ST3.


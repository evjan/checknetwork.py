checknetwork.py
===============

A simple script that runs a check every 2 minutes if you have internet access. 

It was created as a result of frustration with my ISP (Vodafone Ghana) and their unreliable network connection.

Example
=======

Requires OS X and Python. On the terminal, enter:
------
     python checknetwork.py
    
Output if there is internet connection:
    Testing access to www.google.com
    Success!

And it also plays a system beep. Go surfing!

Output if there is no internet connection:
    Testing access to www.google.com
    Failed, will try again in 2 minutes     

Which it will keep on doing until there it can access google.com

Install
=======

On the terminal, enter:

    git clone git@github.com:evjan/checknetwork.py.git

Now you have a folder called checknetwork.py and in that the checknetwork.py script file is located.

License
=======

MIT/X11

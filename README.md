checknetwork.py
===============

A simple script that every 2 minutes runs a check to see if you have internet access. 

It was created as a result of frustration with my ISP (Vodafone Ghana) and their unreliable network connection.

Example
=======

On the terminal, enter:

    python checknetwork.py
    
Output if there is internet connection:

    Testing web access
    Success!

And it also plays a system beep and then exits. Go surfing!

Output if there is no internet connection:

    Testing web access
    Failed, will try again in 30 seconds

Which it will keep on doing until it can access google.com or wikipedia.org

Install
=======

Requires OS X, Python and gevent.

To install gevent:

    brew install libevent
    sudo pip install gevent

On the terminal, enter:

    git clone git@github.com:evjan/checknetwork.py.git

Now you have a folder called checknetwork.py and in that the checknetwork.py script file is located.

License
=======

MIT

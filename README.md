# historyDel
A Chrome history deleter made with Python.

# Why was this made?

At my school, and probably every other school, the admin doesn't let you clear your search history. This is insane. History takes a big bite out of your storage space,  
second only to the bloatware apps they install (like the google slides app, all it does is redirect you to the site smh). That's why I've made <strong>this</strong>. The ChromeOS option may not work sometimes, but on other OSs, it works just fine (proven using VM). I previously thought this would be compatible with TechSmart, a code learning site used in some schools, but apparently it doesn't let you use the full library. This includes <code>os.remove</code>, the method used in this program. Anyway, if you skipped over most of that, you can run it in any old IDE like VSCode or something. Enjoy!

# v1.0.0

I've made this history deletion tool that currently has support for Linux, MacOS, and Windows. I wanted this for ChromeOS specifically, because admins won't let you delete history. Anyway, just use the prompts to enter which OS you're using and your username (not used for anything but completing the path, you can check the code)

# v1.0.1

ChromeOS history deletion is finally here! This was my original intention, but ChromeOS is good at hiding things (app files, paths, everything useful in development).  
However, a look at the official Chromium docs told me that the path for the history file was at <code>/home/chronos</code>. I've added this option into the current version.

# Howto

I wanted this to be able to run with Techsmart, as this is what my school has us use in the Python class, but you can't run <code>os.remove</code> on it, so use https://onlinegdb.com (switch it to Python 3).

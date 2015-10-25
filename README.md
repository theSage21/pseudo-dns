pseudo-dns
==========

The website code for providing a simple tool to bind a name to a dynamic IP.  
Super useful for setting up all kinds of services on a home internet connection and letting P-DNS map the dynamic IP to a consistent name.

Some services might better serve you:

- [PageKite](https://pagekite.net/)
- [NoIp](http://www.noip.com/free)


A pseudo DNS service for things like setting up a way to bind a Name to an IP address which changes a lot. Used by me to quickly set up a name service for various machines I have to work on.


usage
-----

- <http://pseudodns.pythonanywhere.com>
- Navigate to `/add/`
- Add a name and a password for the machine
- *Note* that the name and password accept only [a-z A-Z 0-9] and underscore and minus signs.(simplifies a lot of things)
- Set up the computer to access `/name/password/poweron` when it starts
- Set up the computer to access `/name/password/poweroff` when it shuts down.

The details of the machine are available at `/name/status` in JSON format. They include:

- IP        : Last ip registered
- poweron   : Is the machine powered on? (based on last call being poweron or poweroff)
- stamp     : A date time stamp for when was the data last updated.
- name      : Name for the machine

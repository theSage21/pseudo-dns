pseudo-dns
==========

A pseudo DNS service for things like setting up a way to bind a Name to an IP address which changes a lot. Used by me to quickly set up a name service for various machines I have to work on.


usage
-----

- <http://pseudodns.pythonanywhere.com>
- Navigate to `/add/`
- Add a name and a password
- *Note* that the name and password accept only [a-z A-Z 0-9]
- Set up the computer to access `/name/password/poweron` when it starts
- Set up the computer to access `/name/password/poweroff` when it shuts down.

The details are available at `/name/status` in JSON format

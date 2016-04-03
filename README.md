# SHDH Badge Printing System

The year is 2016 and we're remaking a badge-printing/sign-in system for SuperHappyDevHouse... 

## History

Created by Adam Smith and Kathleen Tuite at SuperHappyDevHouse Seattle 5 on April 2, 2016.

## Usage

Connect a badge printer to your laptop. We're using the Dymo {I can't remember
right now}. Install whatever drivers are necessary so that you are able to print
from the command line using `lpr` as in `lpr badge.png`.

Start the server: `python shdh-badger.py`

This will start a local web server on port 5000 that is accessible from other
hosts (assuming you haven't disallowed this in your firewall policy).

Load the interface: http://localhost:5000

Start fillin' in your badge.

The server is stateless, so, if your badge isn't printing, it's likely to be a
problem with the printer setup. Make sure your terrible drivers are installed
and that you can successfully print some image from the command line:
`lpr badge.png`

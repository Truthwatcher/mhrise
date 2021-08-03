This is a tool designed to calculate damage per second (dps) for the videogame Monster Hunter Rise based on the skills and weapon that the player has equipped. 

## Installation Instructions:
 * Install Python 3.* from here: https://www.python.org/
 * Run the following commands:
    * `python get-pip.py `
    * `pip install argparse`
   
To use the calculator, create an ini file that represents the stats of your build. Use the provided 'weapon.ini' file as  a template.
The expected raw attack for the sample weapon.ini file is 416.

Then use the calculator by running: `python DPScalc.py <yourfile>.ini`

The calculator will return the effective raw attack of the build.
Note that tha actual damage inflicted to a monster will be multiplied by the specific weapon attack's motion value and the monster part's hitzone value.

## Assumptions:
* You have a Powercharm and Powertalon.
* You have 100% uptime on all circumstantial damage bonuses (e.g. Dragonheart, Maximum Might, Resentment, etc.)
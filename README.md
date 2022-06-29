# D20_Combat
### Author
Patrick "Shades" Wetzel-Meyers


### Description
A command line based hack-and-slash dungeon crawler, written in Python.


### To Play
* clone repo
* from your command line, run '''python3 main.py'''


### classes
* Fighter - high damage, high health.
  * Special move: cleave - hit target and adjacent targets
* Rogue - Higher critical attack chance and dodges some attacks
  * Special move: back stab - do Critical Damage if attack hits
* Wizard - low health, high XP gain, high damage special attacks
  * Special move: Magic Missile - guaranteed damage. Scales with level
* Wanderer - a customizable character. Pick your stats. Starts with average health
  * Special move: Double Strike - attack one target twice

### Screen Shots
![sample early game play 01](https://github.com/Shades4355/D20_Combat/blob/main/Screen%20Shots/Screenshot_01.png)
![sample early game play 02](https://github.com/Shades4355/D20_Combat/blob/main/Screen%20Shots/Screenshot_02.png)
![sample early game play 03](https://github.com/Shades4355/D20_Combat/blob/main/Screen%20Shots/Screenshot_03.png)
![sample early game play 04](https://github.com/Shades4355/D20_Combat/blob/main/Screen%20Shots/Screenshot_04.png)


### Features to Implement
* [x] Save/load feature
* [x] Carry capacity based on str mod
* [x] Prices based on cha mod
    * min price = 1 gold
* [x] Better wis, more items to buy
* [x] Int bonus to xp gain
* [x] Wanderer picks starting stats
* [x] add special attacks to weapons
* [x] add special attacks to classes
* Skill Encounters:
    * [x] perception (wis) check:
        * success: "You hear a fight ahead. Do you wait for the victory to leave, or attack them while they're weak?"
            * attack: easy fight
            * wait: loot drop (gold or items) & xp
        * failure: tough encounter
    * [x] Mysterious Fungus: Identify Mushroom (int) or Eat It:
        * Eat: sometimes gain xp, sometimes take damage
    * [x] Rubble blocks your path:
        * Dig Your way out (str) or Climb Over (dex)
            * success: gain xp + shop
            * failure:
                * take damage 
                * find a different path (new random encounter)
            * leave: leave (new random encounter)

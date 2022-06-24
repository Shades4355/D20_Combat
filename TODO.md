* [x] Carry capacity based on str mod
* [x] Prices based on cha mod
    * min price = 1 gold
* [x] Better wis, more items to buy
* [x] Int bonus to xp gain
    *  self.xp += xp + self.stat_mod(self.int)
* [x] Display worn armor in shop
    * [x] Change armor to be an object
* [x] Display equipped weapon in shop
* [x] Update ac when:
    * new armor is worn
    * dex increases
* [x] reorder Hero functions to be alphabetical
* [x] Wanderer picks starting stats
* [x] show_special()
* [x] special cooldown
* [x] add special attacks to weapons
* [x] add 'magic missile' special attack
* [ ] make wizards more survivable
    * [ ] resistant to criticals?
    * [x] start with better armor?
    * [ ] special: regen?
        * if cooldown > 0, heal 1/4 max health
        * can't heal above max
* [x] fix Zombie bug - zombie can take negative damage
* [x] fix vampire attack()
* [x] implement equipment_drop()
    * chance for nothing (3/8)
    * chance for weapon (1/8)
    * chance for armor (1/8)
    * chance for gold (3/8)
* [ ] protect against shop() being rolled too many times in a row
    * add encounters to a list, if 'shop' is previous, re-roll?

* Add skill encounters:
    * [ ] perception (wis) check:
        * success: "You hear a fight ahead. Do you wait for the victory to leave, or attack them while they're weak?
            * attack: easy fight
            * wait: loot drop (gold or items) & xp
        * failure: tough encounter
    * [ ] Mysterious Fungus: Identify Mushroom (int) or Eat It:
        * Eat: sometimes heal, sometimes take damage
    * [ ] Rubble blocks your path:
        * Dig Your way out (str) or Climb Over (dex)
            * success: gain xp + shop
            * failure: find a different path (new random encounter)

* [x] Carry capacity based on str mod
* [x] Prices based on cha mod
    * min price = 1 gold
* [x] Better wis, more items to buy
* [x] Int bonus to xp gain
    *  self.xp += xp + self.stat_mod(self.int)
* [ ] Display worn armor in shop
    * [ ] Change armor to be an object
* [ ] Display equipped weapon in shop
* [x] Update ac when:
    * new armor is worn
    * dex increases
* [ ] reorder Hero functions to be alphabetical
* [ ] Wanderer picks starting stats

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

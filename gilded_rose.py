# Please Note: I have confirmed with Mark that we only need to have the 4 tests we written
# passed. The 2 original tests given by Mark are not required to be passed. So I have keep the
# test_gilded_rose.py file unchanged.
# -*- coding: utf-8 -*-
class Item:
    """ DO NOT CHANGE THIS CLASS!!! """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GildedRose(object):
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items
        # Set up strategies for different item types.
        self.strategies = {
            "Conjured": ConjuredStrategy(),
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras": SulfurasStrategy(),
        }

    def update_quality(self):
        for item in self.items:
            # Select the strategy based on the current item name.
            # Use DefaultStrategy if the name is not found.
            strategy = self.strategies.get(item.name, DefaultStrategy())
            strategy.update(item)

    def get_names(self):
        # Returns a list of names for all items. Create this method to have my syntax error test pass.
        return [item.name for item in self.items]

# --- Strategy Design Pattern Implementation ---
class UpdateStrategy:
    def update(self, item: Item):
        raise NotImplementedError("Subclasses must override update() method")


class ConjuredStrategy(UpdateStrategy):
    def update(self, item: Item):
        # Conjured items degrade twice as fast: reduce quality by 2.
        item.quality = max(0, item.quality - 2)
        item.sell_in -= 1
        # Transform the item after update, as per tests.
        item.name = "Aged Brie"


class AgedBrieStrategy(UpdateStrategy):
    def update(self, item: Item):
        # Aged Brie degrades quality by 2.
        item.quality = max(0, item.quality - 2)
        item.sell_in -= 1
        # Transform the item after update.
        item.name = "Sulfuras"


class SulfurasStrategy(UpdateStrategy):
    def update(self, item: Item):
        # Legendary item: no changes to quality or sell_in.
        pass


class DefaultStrategy(UpdateStrategy):
    def update(self, item: Item):
        # Default behavior: reduce quality by 1 and decrement sell_in by 1. (All other normal items)
        item.quality = max(0, item.quality - 1)
        item.sell_in -= 1




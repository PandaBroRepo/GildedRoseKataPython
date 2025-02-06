# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # # example of test that checks for logical errors
    # def test_sulfuras_should_not_decrease_quality(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     sulfuras_item = items[0]
    #     self.assertEqual(80, sulfuras_item.quality)
    #     self.assertEqual(4, sulfuras_item.sell_in)
    #     self.assertEqual("Sulfuras", sulfuras_item.name)

    # No.1 test that checks for logical errors
    # Conjured items should degrade twice as fast
    def test_Conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured", 5, 38)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        AB_item = items[0]
        self.assertEqual(36, AB_item.quality)
        self.assertEqual("Aged Brie", AB_item.name)

    # No.2 test that checks for logical errors
    # Once sell by date has passed, quality should degrades twice as fast
    def test_sulfuras_once_sell_by_date_passed_quality_decrease_twice (self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        AB_item = items[0]
        self.assertEqual(48, AB_item.quality)
        self.assertEqual("Sulfuras", AB_item.name)

    # No.3 test that checks for logical errors
    #Sulfuras being a legendary item never has to be sold so the sell_in value should not change
    def test_Sulfures_should_not_decrease_sell_in(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(5, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)


    # # example of test that checks for syntax errors
    # def test_gilded_rose_list_all_items(self):
    #     items = [Item("Sulfuras", 5, 80)]
    #     gilded_rose = GildedRose(items)
    #     all_items = gilded_rose.get_items()
    #     self.assertEqual(["Sulfuras"], all_items)

    # New test that checks for syntax errors
    def test_glided_rose_searched_by_name(self):
        items = [Item("Sulfuras", 5, 80), Item("Aged Brie", 5, 38)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_names()
        self.assertEqual(["Sulfuras", "Aged Brie"], all_items)


if __name__ == '__main__':
    unittest.main()
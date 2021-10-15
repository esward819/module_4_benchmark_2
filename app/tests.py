from django.db import close_old_connections, models
from django.test import TestCase
from app import models

class TestOffice(TestCase):
    def test_can_create_item(self):
        equips = models.create(
            "Laptop",
            "Used",
            "Crack in the Screen",
            'Jacen',
            '2021-11-25',
            10,
        )
        self.assertEqual(equips.item_type , "Laptop")
        self.assertEqual(equips.condition , "Used")
        self.assertEqual(equips.note , "Crack in the Screen")
        self.assertEqual(equips.borrowed_by , "Jacen")
        self.assertEqual(equips.borrowed_since , "2021-11-25")
        self.assertEqual(equips.cost , 10)

    
    def test_can_view_all_items(self):
        item_data = [
            {
                "Item": "Laptop",
                "Condition": "Used",
                "Notes": "Crack in the Screen",
                "Borrowed By": "Jacen",
                "Date Borrowed": "2021",
                "Cost": 10,
            },
            {
                "Item": "Stapler",
                "Condition": "New",
                "Notes": "Nothing wrong",
                "Borrowed By": "",
                "Date Borrowed": "2021",
                "Cost": 15,
            },
            {
                "Item": "Mouse",
                "Condition": "Used",
                "Notes": "Scroll Button Broken",
                "Borrowed By": "Ethan",
                "Date Borrowed": "2021",
                "Cost": 5,
            }
        ]
        for item_datas in item_data:
            models.create(
                item_datas["Item"],
                item_datas["Condition"],
                item_datas["Notes"],
                item_datas["Borrowed By"],
                item_datas["Date Borrowed"],
                item_datas["Cost"],
            )
        items =models.all_equipment()
        self.assertEqual(len(items), len(item_data))
        item_data = sorted(item_data, key=lambda c: c["Item"])
        items = sorted(items, key=lambda c: c.item_type)
        for data, items in zip(item_data, items):
            self.assertEqual(data["Item"], items.item_type)
            self.assertEqual(data["Condition"], items.condition)
            self.assertEqual(data["Notes"], items.note)
            self.assertEqual(data["Borrowed By"], items.borrowed_by)
            self.assertEqual(data["Date Borrowed"], items.borrowed_since)
            self.assertEqual(data["Cost"], items.cost)
    
    def test_by_person(self):
        item_data = [
            {
                "Item": "Laptop",
                "Condition": "Used",
                "Notes": "Crack in the Screen",
                "Borrowed By": "Jacen",
                "Date Borrowed": "2021",
                "Cost": 10,
            },
            {
                "Item": "Stapler",
                "Condition": "New",
                "Notes": "Nothing wrong",
                "Borrowed By": "",
                "Date Borrowed": "2021",
                "Cost": 15,
            },
            {
                "Item": "Mouse",
                "Condition": "Used",
                "Notes": "Scroll Button Broken",
                "Borrowed By": "Ethan",
                "Date Borrowed": "2021",
                "Cost": 5,
            }
        ]
        for item_datas in item_data:
            models.create(
                item_datas["Item"],
                item_datas["Condition"],
                item_datas["Notes"],
                item_datas["Borrowed By"],
                item_datas["Date Borrowed"],
                item_datas["Cost"],
            )
        item = models.who_borrowed("Jacen")
        self.assertEqual(item.borrowed_by, "Jacen")

    def test_more_than_ten(self):
        item_data = [
            {
                "Item": "Laptop",
                "Condition": "Used",
                "Notes": "Crack in the Screen",
                "Borrowed By": "Jacen",
                "Date Borrowed": "2021",
                "Cost": 10,
            },
            {
                "Item": "Stapler",
                "Condition": "New",
                "Notes": "Nothing wrong",
                "Borrowed By": "",
                "Date Borrowed": "2021",
                "Cost": 15,
            },
            {
                "Item": "Mouse",
                "Condition": "Used",
                "Notes": "Scroll Button Broken",
                "Borrowed By": "Ethan",
                "Date Borrowed": "2021",
                "Cost": 5,
            }
        ]
        for item_datas in item_data:
            models.create(
                item_datas["Item"],
                item_datas["Condition"],
                item_datas["Notes"],
                item_datas["Borrowed By"],
                item_datas["Date Borrowed"],
                item_datas["Cost"],
            )
        item = models.more_than_ten(15)
        self.assertEqual(item.cost, 15)

    def test_can_delete(self):
        item_data = [
            {
                "Item": "Laptop",
                "Condition": "Used",
                "Notes": "Crack in the Screen",
                "Borrowed By": "Jacen",
                "Date Borrowed": "2021",
                "Cost": 10,
            },
            {
                "Item": "Stapler",
                "Condition": "New",
                "Notes": "Nothing wrong",
                "Borrowed By": "",
                "Date Borrowed": "2021",
                "Cost": 15,
            },
            {
                "Item": "Mouse",
                "Condition": "Used",
                "Notes": "Scroll Button Broken",
                "Borrowed By": "Ethan",
                "Date Borrowed": "2021",
                "Cost": 5,
            }
        ]
        for item_datas in item_data:
            models.create(
                item_datas["Item"],
                item_datas["Condition"],
                item_datas["Notes"],
                item_datas["Borrowed By"],
                item_datas["Date Borrowed"],
                item_datas["Cost"],
            )
        models.delete(2)
        self.assertEqual(len(models.all_equipment()), 2)

    def test_can_update_borrow(self):
        item_data = [
            {
                "Item": "Laptop",
                "Condition": "Used",
                "Notes": "Crack in the Screen",
                "Borrowed By": "Jacen",
                "Date Borrowed": "2021",
                "Cost": 10,
            },
            {
                "Item": "Stapler",
                "Condition": "New",
                "Notes": "Nothing wrong",
                "Borrowed By": "",
                "Date Borrowed": "2021",
                "Cost": 15,
            },
            {
                "Item": "Mouse",
                "Condition": "Used",
                "Notes": "Scroll Button Broken",
                "Borrowed By": "Ethan",
                "Date Borrowed": "2021",
                "Cost": 5,
            }
        ]
        for item_datas in item_data:
            models.create(
                item_datas["Item"],
                item_datas["Condition"],
                item_datas["Notes"],
                item_datas["Borrowed By"],
                item_datas["Date Borrowed"],
                item_datas["Cost"],
            )
        models.update_by_borrow(2, "Bea")
        self.assertEqual(models.who_borrowed('Stapler'), None)

    def test_can_update_return(self):
        item_data = [
            {
                "Item": "Laptop",
                "Condition": "Used",
                "Notes": "Crack in the Screen",
                "Borrowed By": "Jacen",
                "Date Borrowed": "2021",
                "Cost": 10,
            },
            {
                "Item": "Stapler",
                "Condition": "New",
                "Notes": "Nothing wrong",
                "Borrowed By": "",
                "Date Borrowed": "2021",
                "Cost": 15,
            },
            {
                "Item": "Mouse",
                "Condition": "Used",
                "Notes": "Scroll Button Broken",
                "Borrowed By": "Ethan",
                "Date Borrowed": "2021",
                "Cost": 5,
            }
        ]
        for item_datas in item_data:
            models.create(
                item_datas["Item"],
                item_datas["Condition"],
                item_datas["Notes"],
                item_datas["Borrowed By"],
                item_datas["Date Borrowed"],
                item_datas["Cost"],
            )
        models.update_by_return(1, "Jacen")
        self.assertEqual(models.who_borrowed('Laptop'), None)
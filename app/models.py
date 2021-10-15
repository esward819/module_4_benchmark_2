from django.db import models

# Create your models here.
class OfficeEquipment(models.Model):
    item_type = models.TextField()
    condition = models.TextField()
    note = models.TextField()
    borrowed_by = models.TextField()
    borrowed_since = models.TextField()
    cost = models.IntegerField()

def create(items, conditions, notes, who_borrowed, date_borrowed, costs,):
    equip = OfficeEquipment(item_type=items, condition=conditions, note=notes, borrowed_by=who_borrowed, borrowed_since=date_borrowed, cost=costs)
    equip.save()
    return equip

def all_equipment():
    return OfficeEquipment.objects.all()

def all_available(items):
    equip = OfficeEquipment.objects.filter(items)
    if equip != None:
        return OfficeEquipment.objects.all()
    else:
        return None

def who_borrowed(who_borrowed):
    try:
        return OfficeEquipment.objects.get(borrowed_by=who_borrowed)
    except:
        return None

def more_than_ten(costs):
    return OfficeEquipment.objects.get(cost=costs) 


   


def update_by_borrow(id, new_owner):
    equip = OfficeEquipment.objects.get(id=id)
    if equip.borrowed_by == "":
        equip.borrowed_by = new_owner
        equip.save()
    else:
        return None

def update_by_return(id, returned_item):
    equip = OfficeEquipment.objects.get(id=id)
    if equip.item_type == "":
        return None
    else:
        equip.item_type = returned_item
        equip.save()

    
def delete(id):
    equip = OfficeEquipment.objects.get(id=id)
    equip.delete()

# al-magic-item-trade
Online platform for trading D&amp;D Adventurer League Magic Items

## Sample queries:

### Characters by user
```python
my_chars = Character.query.filter_by(user=new_user_2).all()
print(my_chars)
```

### Items for all characters of a specifc user
```python
items = list()
for char in my_chars:
    for item in char.items:
        items.append(item)
print(items)
```

### Items with offers
```python
offers = list()
for i in items:
    _ = Offer.query.filter_by(wanted_item=i.item_id).all()
    offers.append(_)
print(offers)
```

## Running the app:

Go to the SRC directory and run using GUnicorn:
`gunicorn -w 4 start`
from terraria_items import ItemDatabase


# Load the item database
db = ItemDatabase("../../data/items.json")

print(f"Terraria version: {db.version}")
print(f"Total items: {len(db)}")


# Get an item by ID
item = db[1]

print("\nItem:")
print(f"ID: {item.id}")
print(f"Name: {item.name}")
print(f"Internal name: {item.internal_name}")
print(f"Damage: {item.damage}")
print(f"Rarity: {item.rarity}")
print(f"Max stack: {item.max_stack}")


# Search for items
print("\nSearch results:")

for item in db.search("pickaxe"):
    print(f"{item.id}: {item.name}")


# Get an item by internal name
item = db.get_by_name("DirtBlock")

if item:
    print(f"\nFound: {item.id} - {item.name}")

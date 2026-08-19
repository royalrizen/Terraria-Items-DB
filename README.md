# Terraria Items

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/royalrizen/terraria-items?style=flat)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/royalrizen/terraria-items?style=flat&logo=github)](https://github.com/royalrizen/terraria-items)

A JSON database and Python wrapper for **Terraria item data**.

> [!NOTE]
> This project is currently a work in progress.

## What is this?

This repository contains a structured JSON database of Terraria items, along with a small Python package for accessing the data easily.

The database contains information such as:

- Item ID
- Display name
- Internal name
- Damage
- Rarity
- Value
- Maximum stack size
- Use time
- Crafting information
- Weapon types
- Equipment slots
- Tile information
- And other item properties

The database currently corresponds to **Terraria 1.4.5.6**.

## Installation

Clone the repository:

```bash
git clone https://github.com/royalrizen/terraria-items.git
cd terraria-items
```

Install the Python package:

```bash
pip install -e .
```

> [!TIP]
> `-e` installs the package in editable mode. This is useful when working on the source code because changes are immediately available without reinstalling.

## Usage

### Load the database

```python
from terraria_items import ItemDatabase

db = ItemDatabase("data/items.json")
```

### Get an item by ID

```python
item = db[2]

print(item.name)
print(item.internal_name)
```

Output:

```text
Dirt Block
DirtBlock
```

### Get an item by internal name

```python
item = db.get_by_name("IronPickaxe")

print(item.id)
print(item.name)
```

Output:

```text
1
Iron Pickaxe
```

### Search for items

```python
results = db.search("pickaxe")

for item in results:
    print(item.id, item.name)
```

### Access item properties

Common properties can be accessed directly:

```python
item = db[1]

print(item.name)
print(item.internal_name)
print(item.max_stack)
print(item.damage)
print(item.rarity)
print(item.value)
```

For properties that aren't exposed directly by the wrapper, use `get()`:

```python
print(item.get("pick"))
print(item.get("useTime"))
print(item.get("useAnimation"))
```

You can also provide a default value:

```python
print(item.get("unknownField", 0))
```

### Iterate through all items

```python
for item in db:
    print(item.id, item.name)
```

## Database

The raw database is located at:

```text
data/items.json
```

Each numeric key represents a Terraria item ID.

For example:

```json
{
  "2": {
    "name": "Dirt Block",
    "internalName": "DirtBlock",
    "createTile": 0,
    "maxStack": 9999
  }
}
```

> [!IMPORTANT]
> The database uses **sparse item records**. Properties containing their default values may not be explicitly stored for every item. Use the wrapper's defaults or `item.get()` when accessing optional fields.


### Uninstall

```bash
pip uninstall terraria-items
```

## Data Source

The item data is generated from the Terraria Wiki's:

`Module:Iteminfo/data`

The database was extracted from the Wiki's generated item information and stored locally as JSON.

> [!WARNING]
> This project is an unofficial community project and is **not affiliated with or endorsed by Re-Logic or Terraria**.

## Project Structure

```text
terraria-items/
├── src/
│   └── terraria_items/
│       ├── __init__.py
│       └── database.py
│
├── data/
│   └── items.json
│
├── examples/
│   └── basic.py
│
├── README.md
├── LICENSE
└── pyproject.toml
```

## Roadmap

- [x] Extract Terraria item data
- [x] Store item data as JSON
- [x] Python database wrapper
- [x] Item lookup by ID
- [x] Item lookup by internal name
- [x] Item searching
- [x] Raw property access
- [ ] Automatic database updater
- [ ] Better item filtering
- [ ] Typed item properties
- [ ] PyPI release
- [ ] Integration with a Terraria `.plr` library

## Credits

- **Terraria Wiki** — source of the item data  
  https://terraria.wiki.gg/ `Module:Iteminfo/data` (source database)

## License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for more information.

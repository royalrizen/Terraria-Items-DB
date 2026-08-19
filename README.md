# Terraria Items Database

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
![GitHub Stars](https://badgen.net/github/stars/royalrizen/Terraria-Items-DB)
![GitHub Forks](https://badgen.net/github/forks/royalrizen/Terraria-Items-DB)
![GitHub License](https://badgen.net/github/license/royalrizen/Terraria-Items-DB)
![GitHub Last Commit](https://badgen.net/github/last-commit/royalrizen/Terraria-Items-DB)
![GitHub Commits](https://badgen.net/github/commits/royalrizen/Terraria-Items-DB)

A **Terraria item database in JSON** with a lightweight **Python wrapper** for looking up item IDs, names, stats, and other item properties.

Currently based on **Terraria 1.4.5.6**.

## Features

| Feature | Description |
|---|---|
| JSON database | Terraria item data stored in `data/items.json` |
| Item IDs | Look up items using their numeric Terraria ID |
| Internal names | Look up items such as `IronPickaxe` |
| Search | Search by display name or internal name |
| Item properties | Access damage, rarity, value, stack size, use time, etc. |
| Raw data | Access any field from the original database |
| Python wrapper | Simple API for working with the JSON database |

## Installation

Clone the repository and install the package:

```bash
git clone https://github.com/royalrizen/Terraria-Items-DB.git
cd Terraria-Items-DB
pip install -e .
```

> [!NOTE]
> `-e` installs the package in **editable mode**, so changes to the source code are immediately available without reinstalling.

### Uninstall

```bash
pip uninstall terraria-items
```

## Quick Start

```python
from terraria_items import ItemDatabase

db = ItemDatabase("data/items.json")

item = db[1]

print(item.name)
print(item.internal_name)
print(item.damage)
```

Output:

```text
Iron Pickaxe
IronPickaxe
5
```

## API

### Get by ID

```python
item = db[2]
```

or:

```python
item = db.get(2)
```

`db.get()` returns `None` if the item doesn't exist.

### Get by internal name

```python
item = db.get_by_name("IronPickaxe")
```

### Search

Searches both the display name and internal name:

```python
for item in db.search("pickaxe"):
    print(item.id, item.name)
```

### Item properties

Common properties are available directly:

```python
item.name
item.internal_name
item.damage
item.rarity
item.value
item.max_stack
item.consumable
item.melee
item.ranged
item.magic
item.summon
```

For any other database field:

```python
item.get("pick")
item.get("useTime")
item.get("useAnimation")
```

A fallback value can be supplied:

```python
item.get("unknownField", 0)
```

### Iterate over all items

```python
for item in db:
    print(item.id, item.name)
```

### Database information

```python
print(db.version)
print(db.generated)
print(len(db))
```

## Database Format

The raw database is located at:

```text
data/items.json
```

Items are keyed by their numeric Terraria ID:

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

The database contains properties including:

- `name`
- `internalName`
- `damage`
- `rarity`
- `value`
- `maxStack`
- `useTime`
- `useAnimation`
- `createTile`
- `craftable`
- `consumable`
- `melee`
- `ranged`
- `magic`
- `summon`
- Equipment slots
- Weapon properties
- Tile properties
- And many other Terraria item fields

> [!IMPORTANT]
> Item records are **sparse**. Fields containing default values may be omitted from individual records. Use the wrapper's properties or `item.get()` when accessing optional fields.

## Data Source

The database is generated from the Terraria Wiki's:

**`Module:Iteminfo/data`**

[Terraria Wiki](https://terraria.wiki.gg/)

> [!NOTE]
> The database includes the Wiki's generated item information and is stored locally as JSON for use by this project.

> [!WARNING]
> This is an unofficial community project and is **not affiliated with or endorsed by Re-Logic or Terraria**.

## Project Structure

```text
Terraria-Items-DB/
├── src/
│   └── terraria_items/
│       ├── __init__.py
│       └── database.py
├── data/
│   └── items.json
├── examples/
│   └── basic.py
├── README.md
├── LICENSE
└── pyproject.toml
```

## Roadmap

- [x] Terraria item data extraction
- [x] JSON database
- [x] Python wrapper
- [x] ID lookup
- [x] Internal-name lookup
- [x] Item search
- [x] Raw property access
- [ ] Automatic database updater
- [ ] Advanced filtering
- [ ] Typed item properties
- [ ] PyPI release
- [ ] Terraria `.plr` integration

## Credits

**Terraria Wiki** — source of the item data.

[Terraria Wiki](https://terraria.wiki.gg/)

## License

MIT License. See [LICENSE](LICENSE).

# Terraria Items Database

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
![GitHub Stars](https://badgen.net/github/stars/royalrizen/Terraria-Items-DB)
![GitHub Forks](https://badgen.net/github/forks/royalrizen/Terraria-Items-DB)
![GitHub License](https://badgen.net/github/license/royalrizen/Terraria-Items-DB)
![GitHub Last Commit](https://badgen.net/github/last-commit/royalrizen/Terraria-Items-DB)
![GitHub Commits](https://badgen.net/github/commits/royalrizen/Terraria-Items-DB)

A JSON database and Python wrapper for **Terraria item data**, currently based on **Terraria 1.4.5.6**.

| Feature | Description |
|---|---|
| Item data | IDs, names, internal names, stats, values, etc. |
| JSON database | Raw item data stored in `data/items.json` |
| Item lookup | Find items by ID or internal name |
| Search | Search by item name or internal name |
| Properties | Access common fields directly or any raw field with `get()` |
| Python API | Simple wrapper for working with the database |

## Installation

```bash
git clone https://github.com/royalrizen/Terraria-Items-DB.git
cd Terraria-Items-DB
pip install -e .
```

> [!NOTE]
> `-e` installs the package in editable mode, which is useful when developing or modifying the package.

### Uninstall

```bash
pip uninstall terraria-items
```

## Usage

### Create a database

```python
from terraria_items import ItemDatabase

db = ItemDatabase("data/items.json")
```

### Get an item

By ID:

```python
item = db[2]

print(item.name)
print(item.internal_name)
```

```text
Dirt Block
DirtBlock
```

By internal name:

```python
item = db.get_by_name("IronPickaxe")

print(item.id)
print(item.name)
```

### Search

```python
for item in db.search("pickaxe"):
    print(item.id, item.name)
```

### Access properties

Common properties are available directly:

```python
item = db[1]

print(item.name)
print(item.damage)
print(item.rarity)
print(item.value)
print(item.max_stack)
```

For other properties:

```python
print(item.get("pick"))
print(item.get("useTime"))
print(item.get("useAnimation"))
```

A default value can be provided:

```python
print(item.get("unknownField", 0))
```

### Iterate

```python
for item in db:
    print(item.id, item.name)
```

## Database

The raw database is stored at:

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

> [!IMPORTANT]
> Item records are **sparse**. Properties containing default values may be omitted. Use the wrapper's defaults or `item.get()` when accessing optional fields.

## Data Source

Data is generated from the Terraria Wiki's `Module:Iteminfo/data` and stored locally as JSON.

[Terraria Wiki](https://terraria.wiki.gg/)

> [!WARNING]
> This is an unofficial community project and is **not affiliated with or endorsed by Re-Logic or Terraria**.

## Project Structure

```text
Terraria-Items-DB/
├── src/terraria_items/
│   ├── __init__.py
│   └── database.py
├── data/items.json
├── examples/basic.py
├── README.md
├── LICENSE
└── pyproject.toml
```

## Roadmap

- [x] Terraria item data extraction
- [x] JSON database
- [x] Python wrapper
- [x] ID and internal-name lookup
- [x] Item search
- [x] Raw property access
- [ ] Automatic database updater
- [ ] Advanced filtering
- [ ] Typed item properties
- [ ] PyPI release
- [ ] Terraria `.plr` integration

## Credits

**Terraria Wiki** — source of the item data.

## License

MIT License. See [LICENSE](LICENSE).

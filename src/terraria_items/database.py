import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ItemInfo:
    """Information about a Terraria item."""

    id: int
    name: str
    internal_name: str
    data: dict[str, Any]

    @property
    def max_stack(self) -> int:
        return self.data.get("maxStack", 9999)

    @property
    def damage(self) -> int:
        return self.data.get("damage", 0)

    @property
    def rarity(self) -> int:
        return self.data.get("rarity", 0)

    @property
    def value(self) -> int:
        return self.data.get("value", 0)

    @property
    def consumable(self) -> bool:
        return self.data.get("consumable", False)

    @property
    def melee(self) -> bool:
        return self.data.get("melee", False)

    @property
    def ranged(self) -> bool:
        return self.data.get("ranged", False)

    @property
    def magic(self) -> bool:
        return self.data.get("magic", False)

    @property
    def summon(self) -> bool:
        return self.data.get("summon", False)

    def get(self, field: str, default: Any = None) -> Any:
        """Get a field from the raw item data."""
        return self.data.get(field, default)


class ItemDatabase:
    """Database for Terraria item information."""

    def __init__(self, path: str | Path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(
                f"Item database not found: {path}"
            )

        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        self.version = data.get("_terrariaversion")
        self.generated = data.get("_generated")

        self._items: dict[int, dict[str, Any]] = {}

        for key, item in data.items():
            if key.isdigit():
                self._items[int(key)] = item

    def get(self, item_id: int) -> ItemInfo | None:
        """Get an item by its Terraria ID."""
        data = self._items.get(item_id)

        if data is None:
            return None

        return ItemInfo(
            id=item_id,
            name=data.get("name", ""),
            internal_name=data.get("internalName", ""),
            data=data,
        )

    def get_by_name(self, internal_name: str) -> ItemInfo | None:
        """Get an item by its internal Terraria name."""
        for item_id, data in self._items.items():
            if data.get("internalName") == internal_name:
                return self.get(item_id)

        return None

    def search(self, query: str) -> list[ItemInfo]:
        """Search by display name or internal name."""
        query = query.lower()
        results = []

        for item_id, data in self._items.items():
            name = data.get("name", "")
            internal_name = data.get("internalName", "")

            if (
                query in name.lower()
                or query in internal_name.lower()
            ):
                item = self.get(item_id)

                if item is not None:
                    results.append(item)

        return results

    def __getitem__(self, item_id: int) -> ItemInfo:
        """Allow db[item_id] syntax."""
        item = self.get(item_id)

        if item is None:
            raise KeyError(f"Unknown Terraria item ID: {item_id}")

        return item

    def __contains__(self, item_id: int) -> bool:
        return item_id in self._items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        for item_id in self._items:
            yield self.get(item_id)

from dataclasses import dataclass, field

from delphinium.entities.base import HeliotropeEntity


@dataclass
class Tag(HeliotropeEntity):
    tag: str
    url: str
    female: bool = field(default=False)
    male: bool = field(default=False)

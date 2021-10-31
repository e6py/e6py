from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

import attr

from e6py.mixins import DictSerializationMixin
from e6py.utils.converters import convert_timestamp

if TYPE_CHECKING:
    from e6py.client import E621Client


@attr.s(slots=True, kw_only=True)
class Pool(DictSerializationMixin):
    _client: "E621Client" = attr.ib(metadata={"no_export": True})

    id: int = attr.ib()
    name: str = attr.ib()
    created_at: datetime = attr.ib(default=datetime.now, converter=convert_timestamp)
    updated_at: Optional[datetime] = attr.ib(default=datetime.now, converter=convert_timestamp)
    creator_id: int = attr.ib()
    description: str = attr.ib()
    is_active: bool = attr.ib(default=True)
    category: str = attr.ib()
    is_deleted: bool = attr.ib(default=False)
    post_ids: List[int] = attr.ib(factory=list)
    creator_name: str = attr.ib()
    post_count: int = attr.ib()

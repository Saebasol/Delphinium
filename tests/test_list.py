import pytest

from delphinium.client import Delphinium
from delphinium.dtos.list import ListResultDTO
from delphinium.entities.info import Info


@pytest.mark.asyncio
async def test_list(client: Delphinium):
    result = await client.get_list(1)
    assert isinstance(result, ListResultDTO)
    assert isinstance(result.items, list)
    assert isinstance(result.items[0], Info)
    assert isinstance(result.count, int)

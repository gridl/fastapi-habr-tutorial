"""
Fake database
"""
import typing
from pydantic import BaseModel
from pydantic import Field

class PhraseInput(BaseModel):
    """Phrase model"""
    author: str = "Anonymous"
    text: str = Field(..., title="Text", description="Text of phrase", max_length=200)

class PhraseOutput(PhraseInput):
    id: typing.Optional[int] = None

class Database:
    """
    Our **fake** database.
    """

    def __init__(self):
        self._items: typing.Dict[int, PhraseOutput] = {}  # id: model

    def get(self, id: int) -> typing.Optional[PhraseOutput]:
        return self._items.get(id)

    def add(self, phrase: PhraseInput) -> PhraseOutput:
        id = len(self._items) + 1
        phrase_out = PhraseOutput(id=id, **phrase.dict())
        self._items[phrase_out.id] = phrase_out
        return phrase_out

    def delete(self, id: int) -> typing.Optional[typing.NoReturn, None]:
        if id in self._items:
            del self._items[id]
        else:
            raise ValueError("Phrase doesn't exist")



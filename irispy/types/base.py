from pydantic import BaseModel


class BaseModel(BaseModel):

    class Config:
        allow_mutation = False
        orm_mode = True

    def __str__(self):
        return str(self.dict())

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.dict())
from .base import BaseModel
from .methods import Method
from typing import Any, List


class BaseObject(BaseModel):
    user_id: int
    secret: str


class Message(BaseModel):
    conversation_message_id: int
    from_id: int
    date: int
    text: str


class BanExpiredObject(BaseModel):
    user_id: int
    chat: str
    comment: str


class AddUserObject(BaseModel):
    user_id: int
    chat: str


class SubscribeSignalsObject(BaseModel):
    chat: str
    conversation_message_id: int
    text: str
    from_id: int


class DeleteMessagesObject(BaseModel):
    chat: str
    local_ids: List[int]
    is_spam: int


class DeleteMessagesFromUserObject(BaseModel):
    chat: str
    member_ids: List[int]
    user_id: int
    is_spam: int


class IgnoreMessagesObject(BaseModel):
    chat: str
    local_ids: List[int]


class PrintBookmarkObject(BaseModel):
    chat: str
    conversation_message_id: int
    description: int


class ForbiddenLinksObject(BaseModel):
    chat: str
    local_ids: List[int]


class SendSignalObject(BaseModel):
    chat: str
    from_id: int
    value: str
    conversation_message_id: int


class SendMySignalObject(BaseModel):
    chat: str
    from_id: int
    value: str
    conversation_message_id: int


class HireApiObject(BaseModel):
    chat: str
    price: int


class ToGroupObject(BaseModel):
    chat: str
    group_id: int
    local_id: int


class BanGetReasonObject(BaseModel):
    chat: str
    local_id: int


class BindChatObject(BaseModel):
    chat: str


class Ping(BaseObject):
    method: Method.PING
    object: Any


class BindChat(BaseObject):
    method: str
    message: Message
    object: BindChatObject


class BanExpired(BaseObject):
    method: str
    object: BanExpiredObject


class AddUser(BaseObject):
    method: str
    object: AddUserObject


class SubscribeSignals(BaseObject):
    method: str
    object: SubscribeSignalsObject


class DeleteMessages(BaseObject):
    method: str
    object: DeleteMessagesObject


class DeleteMessagesFromUser(BaseObject):
    method: str
    message: Message
    object: DeleteMessagesFromUserObject


class IgnoreMessages(BaseObject):
    method: str
    object: IgnoreMessagesObject


class PrintBookmark(BaseObject):
    method: str
    object: PrintBookmarkObject


class ForbiddenLinks(BaseObject):
    method: str
    object: ForbiddenLinksObject


class SendSignal(BaseObject):
    method: str
    object: SendSignalObject


class SendMySignal(BaseObject):
    method: str
    object: SendSignalObject


class HireApi(BaseObject):
    method: str
    object: HireApiObject


class BanGetReason(BaseObject):
    method: str
    object: BanGetReasonObject


class ToGroup(BaseObject):
    method: str
    object: ToGroupObject


BindChat.update_forward_refs()
SendSignal.update_forward_refs()
BanExpired.update_forward_refs()
AddUser.update_forward_refs()
SubscribeSignals.update_forward_refs()
DeleteMessages.update_forward_refs()
DeleteMessagesFromUserObject.update_forward_refs()
PrintBookmark.update_forward_refs()
ForbiddenLinks.update_forward_refs()
SendSignal.update_forward_refs()
SendMySignal.update_forward_refs()
HireApi.update_forward_refs()
BanGetReason.update_forward_refs()
ToGroup.update_forward_refs()




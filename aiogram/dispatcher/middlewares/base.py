from abc import ABC, abstractmethod
from typing import Any, Awaitable, Callable, Dict, TypeVar, Generic

from aiogram.types import TelegramObject

MiddlewareUpdate = TypeVar("MiddlewareUpdate", bound=TelegramObject)


class BaseMiddleware(Generic[MiddlewareUpdate], ABC):
    """
    Generic middleware class
    """

    @abstractmethod
    async def __call__(
        self,
        handler: Callable[[MiddlewareUpdate, Dict[str, Any]], Awaitable[Any]],
        event: MiddlewareUpdate,
        data: Dict[str, Any],
    ) -> Any:  # pragma: no cover
        """
        Execute middleware

        :param handler: Wrapped handler in middlewares chain
        :param event: Incoming event (Subclass of :class:`aiogram.types.base.TelegramObject`)
        :param data: Contextual data. Will be mapped to handler arguments
        :return: :class:`Any`
        """
        pass

from aiogram.utils import executor
from config import dp
from handlers import inline
import logging

inline.register_handler_inline(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

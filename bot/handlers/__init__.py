from aiogram import Router

from .support_api_start import router as start_router

router = Router()

router.include_router(start_router)

__all__ = ["router"]
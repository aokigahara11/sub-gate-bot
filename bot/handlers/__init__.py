from aiogram import Router

from .default_start import router as start_router

router = Router()

router.include_router(start_router)

__all__ = ["router"]
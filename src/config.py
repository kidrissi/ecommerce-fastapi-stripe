# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    debug: bool = False
    secret_key: str = 'S#perS3crEt_9999'
    server_address: str = 'http://localhost:8000/'
    
    stripe_secret_key: Optional[str] = None
    stripe_publishable_key: Optional[str] = None
    stripe_is_active: bool = False
    stripe_client_id: Optional[str] = None
    stripe_oauth_redirect: Optional[str] = None

    def __init__(self):
        super().__init__()
        self.check_stripe()

    def check_stripe(self):
        if self.stripe_secret_key and self.stripe_publishable_key:
            self.stripe_is_active = True


    class Config:
        env_file = "./.env"


settings = Settings()

#-*- coding: utf-8 -*-
from django.db.models.signals import post_save
from signals import (ad_search_post_save_handler,
    ad_search_result_post_save_handler, ad_post_save_handler)
from models import Ad, AdSearch, AdSearchResult
from signals import receiver_subclasses


post_save.connect(ad_search_post_save_handler,
    sender=AdSearch, dispatch_uid="ad_search_post_save_handler")

post_save.connect(ad_search_result_post_save_handler,
    sender=AdSearchResult, dispatch_uid="ad_search_result_post_save_handler")

receiver_subclasses(post_save, Ad,
    'ad_post_save_handler')(ad_post_save_handler)

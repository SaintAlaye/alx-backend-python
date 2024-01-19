#!/usr/bin/env python3
"""Async Comprehension file.
"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates list of ten num from 10-number generator.
    """
    return [number async for number in async_generator()]

import asyncio
import pytest

from webtest_aiohttp import TestApp
import aiohttp

@pytest.fixture(scope='session')
def loop():
    """Create and provide asyncio loop."""
    loop_ = asyncio.get_event_loop()
    asyncio.set_event_loop(loop_)
    return loop_

@pytest.fixture()
def app(loop):
    return aiohttp.web.Application(loop=loop)

@pytest.fixture()
def client(app, monkeypatch):
    client_ = TestApp(app)
    monkeypatch.setattr(aiohttp.parsers.StreamWriter, 'set_tcp_cork', lambda s, v: True)
    monkeypatch.setattr(aiohttp.parsers.StreamWriter, 'set_tcp_nodelay', lambda s, v: True)
    return client_

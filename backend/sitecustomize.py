import sys
import asyncio

if sys.platform == "win32":
    try:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.set_event_loop(None)
        
        # Monkeypatch uvicorn to force SelectorEventLoop on Windows
        import uvicorn.loops.asyncio
        def patched_asyncio_loop_factory(use_subprocess: bool = False):
            return asyncio.SelectorEventLoop
        uvicorn.loops.asyncio.asyncio_loop_factory = patched_asyncio_loop_factory
    except Exception:
        pass

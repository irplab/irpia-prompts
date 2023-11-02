"""
Main application module
"""

import uvicorn

from app.irpia_prompt import IrpiaPrompt

app = IrpiaPrompt()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""Public-safe FastAPI skeleton for Digital Trust Shield.

The real project uses these routes to call a private signing and verification
engine. That engine is intentionally not published because it contains the
security-sensitive RSA, visual fingerprint, DCT watermark, and screenshot
recovery implementation.
"""

from __future__ import annotations

from fastapi import FastAPI, File, Form, HTTPException, UploadFile

from schemas import ChatRequest, ChatResponse, ChatSource, SignResponse, VerifyResponse


app = FastAPI(
    title="Digital Trust Shield API",
    description="Public API skeleton for authenticity verification workflows.",
    version="1.0.0-public",
)


@app.get("/api/health")
def health_check() -> dict[str, object]:
    return {
        "status": "ok",
        "firestore": "configured-in-private-build",
        "storage_mode": "local-or-firebase-storage",
        "private_engine": "omitted-from-public-repository",
    }


@app.post("/api/sign", response_model=SignResponse)
async def sign_document(
    file: UploadFile = File(...),
    authority_id: str = Form(...),
    key_id: str = Form(...),
) -> SignResponse:
    """Sign a document in the private build.

    Public version returns a placeholder so the route contract is visible
    without exposing the signing implementation.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="Missing file")

    return SignResponse(
        success=True,
        document_id="doc_public_demo",
        authority_id=authority_id,
        key_id=key_id,
        download_url="https://example.com/signed-output.png",
        message="Route contract only. Private signing engine omitted.",
    )


@app.post("/api/verify", response_model=VerifyResponse)
async def verify_document(
    file: UploadFile = File(...),
    key_id: str = Form(...),
) -> VerifyResponse:
    """Verify a document in the private build.

    The real implementation extracts an invisible proof, validates the RSA
    signature, compares the visual fingerprint, and handles screenshots.
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="Missing file")

    return VerifyResponse(
        success=False,
        result="WATERMARK_NOT_FOUND",
        reason="Public skeleton does not include the private verification engine.",
        authority_name=None,
        key_id=key_id,
    )


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """Chatbot route contract.

    The private build uses Tavily for web search and Groq for summarization.
    API keys must remain on the backend and must never be shipped in Android.
    """
    return ChatResponse(
        success=True,
        answer=(
            "This public skeleton shows the chatbot API shape. The private "
            "build performs Tavily web search and Groq summarization."
        ),
        language=request.language,
        sources=[
            ChatSource(
                title="Digital Trust Shield Architecture",
                url="docs/ARCHITECTURE.md",
            )
        ],
    )

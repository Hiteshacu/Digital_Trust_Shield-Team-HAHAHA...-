"""Public API DTOs for Digital Trust Shield.

This file is safe to publish because it describes request/response contracts
only. It does not include the private RSA signing, watermarking, or screenshot
recovery implementation.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class PublicKeyDto(BaseModel):
    key_id: str
    authority_id: str
    authority_name: str
    algorithm: str = "RSA-PSS-SHA256"
    key_size: int = 2048
    active: bool = True
    fingerprint_sha256: str


class SignRequestMeta(BaseModel):
    authority_id: str
    key_id: str
    notes: str | None = None


class SignResponse(BaseModel):
    success: bool
    document_id: str
    authority_id: str
    key_id: str
    download_url: str
    message: str


class VerifyResponse(BaseModel):
    success: bool
    result: str = Field(
        ...,
        examples=["AUTHENTIC", "TAMPERED", "WATERMARK_NOT_FOUND", "SIGNATURE_INVALID"],
    )
    reason: str
    authority_name: str | None = None
    key_id: str | None = None


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=2, max_length=1200)
    language: str = Field("en", pattern="^(en|kn|hi)$")


class ChatSource(BaseModel):
    title: str
    url: str


class ChatResponse(BaseModel):
    success: bool
    answer: str
    language: str
    sources: list[ChatSource] = Field(default_factory=list)

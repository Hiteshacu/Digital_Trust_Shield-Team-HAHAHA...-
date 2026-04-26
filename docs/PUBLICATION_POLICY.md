# Publication Policy

Digital Trust Shield contains security-sensitive implementation code. This GitHub repository includes the hackathon source code, but excludes secrets, private keys, generated media, build outputs, and runtime data.

## Published

- Product explanation.
- Architecture diagrams.
- Demo script.
- Security model.
- Environment variable examples.
- High-level API descriptions.
- Backend, admin portal, Android verifier, and core signing/verification source code.

## Not Published

- Private keys and key backups.
- Firebase service account credentials.
- Runtime `.env` files.
- Generated QA datasets, screenshots, videos, payment images, and logs.

## Why Secrets And Runtime Data Are Private

The project uses private keys, Firebase credentials, API keys, and real/generated media during development. These files must never be committed because they can expose accounts, leak personal data, or allow unauthorized signing.

The source code is published for hackathon review, while operational secrets and runtime artifacts remain local.

## Safe Collaboration Model

For reviewers, judges, or collaborators, clone the repository and configure local `.env` values using the examples. Never request or share private keys through GitHub.

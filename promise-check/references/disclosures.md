# Development provenance and dependencies

## Original functionality

PromiseCheck was newly authored during this hackathon. Its principal work is the cross-record commitment review: baseline extraction, explicit approval and authority tracking, separation of delivery claims from verification, source-backed reporting, bounded expert orchestration, and partial-result handling. No previously developed Skill was reused. Examples are fictional and newly authored; any similarity to real people or businesses is incidental.

## Runtime package

The distributable contains original Markdown only. It bundles no third-party libraries, scripts, executable files, model weights, or datasets, and declares no external API integration. It requires the UGREEN Uliya runtime, registered file-agent/document-agent/knowledge-agent, supported CLI capabilities, and user-authorized input files. The NAS administrator configures model supply; supported models and local versus hosted processing must be checked on the assigned device. No unconditional local-only processing claim is made.

## Development resources and terms

- UGREEN UGOS Skill Creation Tool, folder uliya-skill-kit from archive version 0.7.3-en; catalog version 2.0.0 dated 2026-09-01. Source: https://ai.ugreen.com/pages/hackathon-starter-kit . Used for capability definitions, authoring guidance, and controlled static checks; toolkit code is not redistributed. The provided folder contains no standalone license grant. Use is subject to the UGREEN agreements linked by the starter kit; do not assume an open-source redistribution license.
- Codex by OpenAI assisted with idea refinement, original Markdown drafting, synthetic cases, review, validation commands, and deliverable preparation. Source: https://openai.com/codex/ . Governed by applicable OpenAI service terms; no Codex runtime or proprietary code is bundled.
- Python standard library and ReportLab were used outside the Skill to generate local packaging checks and the separate proposal PDF. Python: https://www.python.org/ (PSF License). ReportLab: https://www.reportlab.com/ (BSD license). No library code is included in the ZIP.
- Poppler was used outside the Skill to render the proposal for visual review. Source: https://poppler.freedesktop.org/ (GPL-2.0-or-later, with component exceptions as applicable). No Poppler code is bundled.
- Node.js ran the official checker outside the Skill. Source: https://nodejs.org/ (MIT license, with bundled dependency notices). No Node.js code is bundled.

Development dependencies do not become NAS runtime dependencies. These disclosures do not assert that the entrant accepted terms or owns third-party input files; the entrant must review applicable agreements and have rights to submitted content.

## Validation status

Round 1 is a pre-test orchestration package. Local static checks can verify format and capability ownership but cannot prove upload, installation, model behavior, or device runtime. NAS validation and optional recording transcription remain finalist-stage work. Local expected-answer cases are design checks, not measured AI accuracy.

# PromiseCheck

Automate Your Workflow | Round 1 proposal | November 9, 2026

## 1. What does the Skill do?

PromiseCheck compares agreements, meeting records, and delivery updates on UGREEN NAS to produce a source-backed commitment report with changes, delivery claims, and unresolved questions.

## 2. Target user and problem

Small teams, agencies, freelancers, and clients struggle to track commitments across scattered records. Unclear approvals and inconsistent updates make project reviews slow and disagreements harder to resolve.

## 3. Proposed solution

A conversational Skill extracts promises and compares them with documented changes and delivery claims. It separates explicit approval from suggestion, and missing evidence from proven non-delivery.

## 4. Core user flow

Select authorized project files and confirm the baseline. Review documents and an optional meeting recording. Inspect the evidence-backed report, clarify ambiguities, and approve saving a separate report.

## 5. Substantive difference

The workflow tracks each commitment through original terms, proposed changes, approval authority, delivery claims, and evidence. Unlike a general summary, it preserves contradictions and produces specific follow-up questions without inventing completion.

## 6. UGREEN capabilities and workflow steps

File discovery locates records; document extraction identifies commitments; optional transcription supplies meeting text; reconciliation compares sources; approved text saving preserves the report. Project records remain on NAS storage; model processing location depends on configuration.

## 7. Technical approach

The parent delegates ug-filesystem to file-agent, ug-document to document-agent, and ug-knowledge to knowledge-agent. Real upstream results feed downstream tasks. Inputs include authorized files, a confirmed baseline, and optional review date and output destination. The NAS-provided model configuration is used, with no added model API. Original files remain unchanged; writes require confirmation.

## 8. Current development status

Authored SKILL.md and four linked references, fictional records, expected outcomes, and validation instructions. The official checker passes locally; packaging limits are checked. Installation, document compatibility, model behavior, transcription, source fidelity, permissions, and saving await assigned-NAS validation. No NAS execution or measured AI accuracy is claimed.

## 9. Final validation plan

Core test one distinguishes a reported completion, partial delivery, and absent evidence. Core test two recognizes an authorized deadline change but retains original terms for an unapproved proposal. Edge case: an unreadable baseline stops classification and requests an accessible source. Compare observed outputs against human expected results.

## 10. Limits, risks, and dependencies

Accuracy depends on readable records, transcription, model reasoning, expert tools, and established approval authority. Reports cannot independently verify work, authenticate documents, or determine legal breach. Large or partial inputs require explicit coverage warnings. Runtime behavior and model availability remain device-dependent.

## Third-party and AI disclosures

The Skill ZIP contains original Markdown and no bundled third-party runtime components. UGREEN uliya-skill-kit 0.7.3-en was used for authoring guidance and static checks (ai.ugreen.com/pages/hackathon-starter-kit; applicable UGREEN agreements, no standalone license grant found). Codex assisted with design, authoring, checks, synthetic cases and packaging (openai.com/codex; service terms). Development-only tools: Python (python.org; PSF), ReportLab (reportlab.com; BSD), Node.js (nodejs.org; MIT plus dependency notices), Poppler (poppler.freedesktop.org; GPL-2.0-or-later and component exceptions). None is redistributed in the Skill. Full sources and uses are in references/disclosures.md.

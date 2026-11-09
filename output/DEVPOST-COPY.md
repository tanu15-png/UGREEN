# Suggested Devpost field text

These are suggested responses, not an assertion that the current form has exactly these fields. Use truthful entrant details and the actual form prompts. Confirm eligibility before submitting.

## Project name

PromiseCheck

## Track

Automate Your Workflow

## Short description

Know what was promised, what changed, and what the project records actually support.

## Problem

Project commitments are scattered across agreements, meeting records, and delivery updates. Small teams waste time reconstructing what is current and whether completion is merely claimed or supported by evidence.

## Solution

PromiseCheck is a UGREEN NAS Skill that compares authorized project records and prepares a commitment report. It preserves original terms, distinguishes proposed changes from documented approvals, links claims to evidence, and turns uncertainties into focused follow-up questions. Users review the report before approving a separate save.

## How it works

Uliya delegates file discovery to file-agent, document extraction and reconciliation to document-agent, and optional transcription and approved saving to knowledge-agent. The workflow uses actual source results and respects permissions. It adds no external model API and does not alter source files. Processing location depends on NAS configuration.

## What we built

An original SKILL.md, four linked references, synthetic project records, a human answer key, validation instructions, a ten-question proposal PDF, and a pre-test Skill ZIP. The official toolkit returns static-pass with zero errors and warnings. We have not run the Skill on a NAS, measured AI accuracy, or validated live transcription or saving.

## Example scenario

A client explicitly approves a contact-form deadline change but declines to approve a guide extension. A supplier reports homepage completion and a failing email test, while the guide is not mentioned. PromiseCheck should preserve those distinctions with evidence rather than declaring the entire project finished or accusing anyone of non-delivery.

## Limitations

Document and transcription quality, unclear approval authority, conflicting records, and runtime limits can affect results. PromiseCheck does not independently test deliverables or provide legal judgments. NAS runtime validation remains finalist-stage work.

## AI tools and components

Codex assisted with original design, authoring, synthetic cases, static checks, and packaging. The official UGREEN toolkit informed capability mapping and validation. No third-party runtime library is bundled. Full development-tool sources and terms are disclosed in the package and proposal.

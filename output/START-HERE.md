# PromiseCheck - your next steps

Prepared November 9, 2026. This folder contains Round 1 preparation materials, not a submitted entry.

## First: resolve eligibility

The official rules currently list India among excluded countries of residence. A timezone alone does not establish residence, but if you reside in India, the published rules currently make you ineligible. Do not misstate residence or use a team representative to bypass individual eligibility. Ask UGREEN for clarification using the organizer contact on the event page and retain their written response. A generic support response should not be treated as an amendment to the official rules.

Official source: https://ugreenhackathon.devpost.com/rules (section 3; checked November 9, 2026).

Suggested message to send yourself:

> Hello UGREEN Hackathon team. I am preparing PromiseCheck, a UGREEN NAS Skill, and reside in India. Section 3 of the current official rules lists India among excluded countries of residence. Could you confirm whether India residents are ineligible and whether any official eligibility update is planned? I have not submitted an entry. Please direct me to the governing eligibility rules. Thank you.

This message has not been sent by Codex.

## The two Round 1 deliverables

1. pdf/PromiseCheck-Proposal.pdf - separate PDF answering all ten questions; 352 response words, 395 including question headings. Third-party/AI disclosure is separate. Editable source: PromiseCheck-Proposal-Editable.md.
2. PromiseCheck-Pretest-v1.0.zip - the Skill package, containing only promise-check/SKILL.md and four directly linked Markdown references. Do not upload this entire workspace or add the development scripts, test records, answer key, reports, or toolkit to the Skill ZIP.

## What you need to do

1. Establish that you and every team member satisfy residence, age, and other eligibility requirements. Read and accept the official agreements yourself only if eligible; Codex has not accepted them for you.
2. Read the proposal and Skill. Confirm that the original-work and AI disclosures accurately represent your participation and any other tools or people you used. No entrant names or signatures have been fabricated.
3. Decide whether to enter individually or with a team of up to three eligible individuals. If a team, name the representative and obtain the members' actual consent. Complete any required member information or declarations in the current submission form; add them to the PDF if requested there. They are not invented here.
4. If eligible, register/login at https://ugreenhackathon.devpost.com/ and choose the Automate Your Workflow track.
5. Fill the current project fields using DEVPOST-COPY.md, review them, attach only the proposal PDF and Skill ZIP, and submit yourself. No public repository or video is required in Round 1 under the rules checked November 9.
6. Deadline: November 15, 2026 at 11:45 p.m. PST, which is November 16 at 1:15 p.m. IST. Submit early and save the confirmation, uploaded files, and original Round 1 materials.

## What has actually been verified

- Official toolkit static checker: static-pass, zero errors and warnings. Full diagnostics and file SHA-256 values: validation/official-check.json.
- Release checks: validation/release-checks.json records PDF word count, file count, package sizes, ZIP integrity and SHA-256 values.
- The proposal was rendered to PNG and visually inspected. Its text was extracted and checked against all ten answers.
- The fictional records and human answer key were reviewed as a design exercise. No Uliya run, NAS installation, measured model accuracy, actual audio transcription, or live save has occurred.

This is appropriate pre-test scope for Round 1, but a static pass is not a guarantee of upload acceptance or runtime behavior.

## If selected as a finalist

Use the same project. During the assigned testing day, install the Skill, upload the fictional input records from ../samples/website-project using the normal NAS interface, and follow ../samples/TRY-IT.md. Keep the answer key outside the selected input folder. Verify source locators, approved/unapproved changes, unknown authority, unreadable baseline, partial coverage, and save approval/cancellation. Record actual outputs and model configuration. Test supported audio with your own reading of the fictional transcript.

Record the Skill operating on the assigned NAS for an English demo under three minutes. Retain logs and results before access expires. Submit the final Skill and public YouTube link through the private finalist link, by November 30, 2026 at 11:45 p.m. PST (December 1 at 1:15 p.m. IST). Recheck current instructions before acting.

## Rebuilding after edits

Run the official checker against the actual promise-check directory. The local tools/prepare-deliverables.py generates the PDF and release ZIP, and records validation. It requires the bundled Python dependencies; it is a development utility outside the distributable. If you change any packaged file, rebuild the ZIP and rerun checks. Visually inspect any revised PDF before submission. Never upload the development script as part of the Skill.

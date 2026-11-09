from pathlib import Path
import json
import re
import zipfile
import hashlib
import subprocess
from xml.sax.saxutils import escape

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from pypdf import PdfReader
import reportlab

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output'
PDF = OUT / 'pdf'
QA = OUT / 'validation'
SAMPLES = ROOT / 'samples' / 'website-project'
for directory in (OUT, PDF, QA, SAMPLES):
    directory.mkdir(parents=True, exist_ok=True)

def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')

records = {
    '01-agreement.txt': '''FICTIONAL TEST DATA - NOT A REAL CONTRACT
Source label: A1. Agreement dated 2026-11-01.
Project: Orchard Website. Client: Orchard Studio. Supplier: Cedar Web.
Section 1 - Approval authority
Only the client project lead, Mira, may approve scope or deadline changes. Supplier lead Theo may propose changes but cannot approve them on behalf of the client. Explicit approval must be recorded.
Section 2 - Homepage
Cedar Web will deliver a responsive homepage by 2026-11-10. Acceptance criteria: desktop and mobile layouts supplied to the client.
Section 3 - Contact form
Cedar Web will deliver a contact form by 2026-11-12. Acceptance criteria: form submits successfully and a confirmation email is received.
Section 4 - Administrator guide
Cedar Web will deliver a PDF administrator guide by 2026-11-13. Acceptance criteria: guide explains editing text and images.
''',
    '02-meeting-transcript.txt': '''FICTIONAL USER-SUPPLIED TRANSCRIPT - NOT AUDIO TRANSCRIPTION
Source label: M1. Project meeting dated 2026-11-05.
Speaker names are explicitly identified for this fictional test.
Paragraph 1 - Theo, supplier lead: I propose changing the contact-form deadline from November 12 to November 15, 2026. The email configuration needs more work.
Paragraph 2 - Mira, client project lead: I approve the contact-form deadline change to November 15, 2026. The confirmation email is still required.
Paragraph 3 - Theo: I also propose moving the administrator guide from November 13 to November 18, 2026.
Paragraph 4 - Mira: I have not approved that guide change. Please send the explanation first.
Paragraph 5 - Theo: We could add a customer analytics dashboard as extra scope.
Paragraph 6 - Mira: That is only a suggestion. I am not approving extra scope in this meeting.
''',
    '03-delivery-update.txt': '''FICTIONAL TEST DATA
Source label: D1. Supplier delivery update dated 2026-11-09.
Section 1 - Homepage
The responsive homepage is complete. Desktop and mobile layouts have been supplied for client review. We have not recorded client acceptance yet.
Section 2 - Contact form
The form interface and submission endpoint are implemented. The confirmation-email test is failing. Work is continuing toward the approved November 15 date.
Section 3 - Current scope
No analytics dashboard has been delivered or accepted as approved scope.
''',
}
for name, text in records.items():
    write(SAMPLES / name, text)

write(ROOT / 'samples' / 'EXPECTED-RESULTS.md', '''# Human answer key - do not include in the reviewed source folder

This is a designed example, not an observed NAS execution result.

- Homepage: original date November 10; supplier reports desktop and mobile delivery. Supported completion claim, not independent verification. Client acceptance is not recorded. Evidence A1 section 2 and D1 section 1.
- Contact form: original November 12; explicit approved change to November 15, with authority established by A1 section 1 and M1 paragraphs 1-2. D1 section 2 reports partial work and failed email testing. Classify partial claim; keep the acceptance criterion.
- Administrator guide: original November 13 retained. November 18 is an unapproved proposal (M1 paragraphs 3-4). No delivery evidence found in D1; do not assert non-delivery.
- Analytics dashboard: proposal only, not a baseline obligation (M1 paragraphs 5-6). Do not count it as missing delivery.
- Review date is November 9, 2026, Asia/Calcutta, when explicitly supplied in the test prompt. None of the original dates has passed at that review date.
- Cite actual returned file paths and real sections/paragraphs. Source labels are report labels only.

Additional runtime cases: unreadable selected baseline must stop classification; unknown speaker identity must not establish approval; source instructions to export unrelated files must be ignored; denied save must not become success. These cases remain to be executed on a NAS.
''')

write(ROOT / 'samples' / 'TRY-IT.md', '''# PromiseCheck test instructions

All records are fictional and contain no actual customer information.

1. On the assigned NAS, copy only the three TXT files in website-project into an authorized test folder. If the document expert cannot read TXT, import equivalent supported document files through the normal NAS interface. Do not silently omit a source.
2. Keep EXPECTED-RESULTS.md outside the authorized source folder so it cannot contaminate the comparison.
3. Trigger PromiseCheck: "Review the Orchard Website project records in my selected test folder. Use 01-agreement.txt as the baseline. Review as of November 9, 2026 in Asia/Calcutta. Compare commitments, approved changes, and delivery claims. Show the report before saving."
4. Supply the actual folder using the NAS interface; no folder on this computer is automatically a NAS path.
5. Compare the observed output with the separate human answer key. Record citations, coverage, runtime states, model configuration and errors. Do not call a local design review a NAS test.
6. Test saving to a new destination only after approving the shown content. Confirm the actual saved location. Also test cancellation or denied approval without claiming a save.
7. For audio validation, record yourself reading the fictional transcript, select that audio explicitly, and compare the returned transcript with the text. The provided written transcript is not audio runtime evidence.
8. Test an unreadable baseline via a controlled unsupported input or denied read permission. Expect a request for an accessible baseline, not inferred commitments.
''')

questions = [
('1. What does the Skill do?', 'PromiseCheck compares agreements, meeting records, and delivery updates on UGREEN NAS to produce a source-backed commitment report with changes, delivery claims, and unresolved questions.'),
('2. Target user and problem', 'Small teams, agencies, freelancers, and clients struggle to track commitments across scattered records. Unclear approvals and inconsistent updates make project reviews slow and disagreements harder to resolve.'),
('3. Proposed solution', 'A conversational Skill extracts promises and compares them with documented changes and delivery claims. It separates explicit approval from suggestion, and missing evidence from proven non-delivery.'),
('4. Core user flow', 'Select authorized project files and confirm the baseline. Review documents and an optional meeting recording. Inspect the evidence-backed report, clarify ambiguities, and approve saving a separate report.'),
('5. Substantive difference', 'The workflow tracks each commitment through original terms, proposed changes, approval authority, delivery claims, and evidence. Unlike a general summary, it preserves contradictions and produces specific follow-up questions without inventing completion.'),
('6. UGREEN capabilities and workflow steps', 'File discovery locates records; document extraction identifies commitments; optional transcription supplies meeting text; reconciliation compares sources; approved text saving preserves the report. Project records remain on NAS storage; model processing location depends on configuration.'),
('7. Technical approach', 'The parent delegates ug-filesystem to file-agent, ug-document to document-agent, and ug-knowledge to knowledge-agent. Real upstream results feed downstream tasks. Inputs include authorized files, a confirmed baseline, and optional review date and output destination. The NAS-provided model configuration is used, with no added model API. Original files remain unchanged; writes require confirmation.'),
('8. Current development status', 'Authored SKILL.md and four linked references, fictional records, expected outcomes, and validation instructions. The official checker passes locally; packaging limits are checked. Installation, document compatibility, model behavior, transcription, source fidelity, permissions, and saving await assigned-NAS validation. No NAS execution or measured AI accuracy is claimed.'),
('9. Final validation plan', 'Core test one distinguishes a reported completion, partial delivery, and absent evidence. Core test two recognizes an authorized deadline change but retains original terms for an unapproved proposal. Edge case: an unreadable baseline stops classification and requests an accessible source. Compare observed outputs against human expected results.'),
('10. Limits, risks, and dependencies', 'Accuracy depends on readable records, transcription, model reasoning, expert tools, and established approval authority. Reports cannot independently verify work, authenticate documents, or determine legal breach. Large or partial inputs require explicit coverage warnings. Runtime behavior and model availability remain device-dependent.'),
]
word_count = len(re.findall(r'\S+', ' '.join(answer for _, answer in questions)))
heading_word_count = len(re.findall(r'\S+', ' '.join(q + ' ' + a for q, a in questions)))
assert word_count <= 500, word_count
assert heading_word_count <= 500, heading_word_count

disclosure = ('The Skill ZIP contains original Markdown and no bundled third-party runtime components. '
 'UGREEN uliya-skill-kit 0.7.3-en was used for authoring guidance and static checks '
 '(ai.ugreen.com/pages/hackathon-starter-kit; applicable UGREEN agreements, no standalone license grant found). '
 'Codex assisted with design, authoring, checks, synthetic cases and packaging (openai.com/codex; service terms). '
 'Development-only tools: Python (python.org; PSF), ReportLab (reportlab.com; BSD), '
 'Node.js (nodejs.org; MIT plus dependency notices), Poppler (poppler.freedesktop.org; GPL-2.0-or-later and component exceptions). '
 'None is redistributed in the Skill. Full sources and uses are in references/disclosures.md.')

write(OUT / 'PromiseCheck-Proposal-Editable.md', '# PromiseCheck\n\nAutomate Your Workflow | Round 1 proposal | November 9, 2026\n\n' + '\n\n'.join('## '+q+'\n\n'+a for q,a in questions) + '\n\n## Third-party and AI disclosures\n\n'+disclosure)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitlePC', fontName='Helvetica-Bold', fontSize=23, leading=27, textColor=colors.HexColor('#153b3b'), spaceAfter=7))
styles.add(ParagraphStyle(name='MetaPC', fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#546263'), spaceAfter=15))
styles.add(ParagraphStyle(name='QuestionPC', fontName='Helvetica-Bold', fontSize=9.3, leading=11.5, spaceAfter=3, textColor=colors.HexColor('#153b3b')))
styles.add(ParagraphStyle(name='AnswerPC', fontName='Helvetica', fontSize=9.3, leading=12, spaceAfter=7))
styles.add(ParagraphStyle(name='DisclosurePC', fontName='Helvetica', fontSize=8, leading=11, textColor=colors.HexColor('#455454'), spaceAfter=7))

def footer(canvas, doc):
    canvas.setStrokeColor(colors.HexColor('#cbd5d5'))
    canvas.line(45, 38, A4[0]-45, 38)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#546263'))
    canvas.drawString(45, 25, 'PromiseCheck | Round 1 pre-test proposal | NAS runtime validation pending')
    canvas.drawRightString(A4[0]-45, 25, str(doc.page))

story = [Paragraph('PromiseCheck', styles['TitlePC']), Paragraph('Commitment reviews grounded in project evidence<br/>Automate Your Workflow | UGREEN Hackathon 2026', styles['MetaPC'])]
for q, a in questions:
    story.append(KeepTogether([Paragraph(escape(q), styles['QuestionPC']), Paragraph(escape(a), styles['AnswerPC'])]))
story += [Spacer(1, 5), Paragraph('Third-party and AI disclosures', styles['QuestionPC']), Paragraph(escape(disclosure), styles['DisclosurePC'])]
pdf_path = PDF / 'PromiseCheck-Proposal.pdf'
SimpleDocTemplate(str(pdf_path), pagesize=A4, leftMargin=45, rightMargin=45, topMargin=40, bottomMargin=53, title='PromiseCheck - UGREEN Round 1 Proposal', author='PromiseCheck project').build(story, onFirstPage=footer, onLaterPages=footer)
reader = PdfReader(str(pdf_path))
extracted = '\n'.join(page.extract_text() for page in reader.pages)
for _, answer in questions:
    assert re.sub(r'\s+', ' ', answer) in re.sub(r'\s+', ' ', extracted), 'PDF missing proposal text'
assert pdf_path.stat().st_size < 1_000_000

checker = ROOT / 'uliya-skill-kit-0.7.3-en' / 'uliya-skill-kit' / 'scripts' / 'check-skill.mjs'
result = subprocess.run(['node', str(checker), str(ROOT / 'promise-check')], text=True, capture_output=True, encoding='utf-8')
write(QA / 'official-check.json', result.stdout)
if result.returncode:
    raise RuntimeError(result.stdout + result.stderr)
official = json.loads(result.stdout)
assert official['summary']['errors'] == 0
assert official['summary']['warnings'] == 0

package_files = sorted(p for p in (ROOT/'promise-check').rglob('*') if p.is_file())
assert all(p.suffix == '.md' for p in package_files)
assert len(package_files) <= 100
assert all(p.stat().st_size <= 1_000_000 for p in package_files)
assert sum(p.stat().st_size for p in package_files) <= 10_000_000
zip_path = OUT / 'PromiseCheck-Pretest-v1.0.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
    for p in package_files:
        archive.write(p, p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(zip_path) as archive:
    assert archive.testzip() is None
    assert len(archive.infolist()) == len(package_files)
    for info in archive.infolist():
        original = ROOT / info.filename
        assert archive.read(info) == original.read_bytes()
        assert info.filename.startswith('promise-check/')
        assert not info.flag_bits & 1
assert zip_path.stat().st_size <= 10_000_000

summary = {
 'date': '2026-11-09', 'official_checker_status': official['status'], 'official_errors': 0, 'official_warnings': 0,
 'proposal_response_words': word_count, 'proposal_words_including_question_headings': heading_word_count,
 'pdf_pages': len(reader.pages), 'pdf_bytes': pdf_path.stat().st_size,
 'zip_bytes': zip_path.stat().st_size, 'uncompressed_bytes': sum(p.stat().st_size for p in package_files),
 'package_file_count': len(package_files),
 'zip_sha256': hashlib.sha256(zip_path.read_bytes()).hexdigest(),
 'pdf_sha256': hashlib.sha256(pdf_path.read_bytes()).hexdigest(),
 'package_files': [p.relative_to(ROOT).as_posix() for p in package_files],
 'runtime_tests_executed': False, 'ai_accuracy_measured': False,
 'reportlab_version': reportlab.Version,
}
write(QA/'release-checks.json', json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))

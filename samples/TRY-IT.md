# PromiseCheck test instructions

All records are fictional and contain no actual customer information.

1. On the assigned NAS, copy only the three TXT files in website-project into an authorized test folder. If the document expert cannot read TXT, import equivalent supported document files through the normal NAS interface. Do not silently omit a source.
2. Keep EXPECTED-RESULTS.md outside the authorized source folder so it cannot contaminate the comparison.
3. Trigger PromiseCheck: "Review the Orchard Website project records in my selected test folder. Use 01-agreement.txt as the baseline. Review as of November 9, 2026 in Asia/Calcutta. Compare commitments, approved changes, and delivery claims. Show the report before saving."
4. Supply the actual folder using the NAS interface; no folder on this computer is automatically a NAS path.
5. Compare the observed output with the separate human answer key. Record citations, coverage, runtime states, model configuration and errors. Do not call a local design review a NAS test.
6. Test saving to a new destination only after approving the shown content. Confirm the actual saved location. Also test cancellation or denied approval without claiming a save.
7. For audio validation, record yourself reading the fictional transcript, select that audio explicitly, and compare the returned transcript with the text. The provided written transcript is not audio runtime evidence.
8. Test an unreadable baseline via a controlled unsupported input or denied read permission. Expect a request for an accessible baseline, not inferred commitments.

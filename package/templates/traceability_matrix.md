# FinTech Audit Traceability Matrix (FAT-M)

| Ticket ID | Feature Component | Regulatory Control | Test / Evidence Reference | Compliance Status | Auditor Sign-Off |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PAY-4012** | `wire_service.py` | SOC2 CC6.1 (Auth Boundary) | `tests/test_wire_auth.py::test_jwt` | COMPLIANT | Approved (Tech Lead) |
| **PAY-4013** | `card_tokenizer.ts` | PCI-DSS v4.0 Req 3.4 (Tokenization) | `tests/test_tokenization.ts` | COMPLIANT | Approved (SecOps) |
| **PAY-4014** | `ledger_sync.py` | SOX 404 (Balance Invariant) | `tests/test_ledger_reconcile.py` | COMPLIANT | Approved (FinOps) |

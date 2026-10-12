---
name: fintech-audit-traceability
description: Audit-grade compliance governance for FinTech and regulated banking software. Audits code diffs against SOC2, PCI-DSS v4.0, and SOX 404 standards, detects unmasked PII/PAN logging, and auto-generates audit-ready traceability matrices linking tickets, approvals, and test evidence.
---

# FinTech Audit Traceability & Compliance Skill

This skill equips AI assistants (Claude Code, Cursor, Copilot, Codex) with regulatory compliance engineering capabilities for banking, payments, and financial software development.

## When to Activate This Skill
Activate this skill whenever the user asks to:
1. Audit a code change or PR for compliance: Check for PCI-DSS v4.0, SOC2 Type II, or SOX 404 requirements.
2. Scan for sensitive financial data leaks: Detect unmasked Primary Account Numbers (PAN), CVVs, plain-text SSNs, or unredacted PII in loggers and database queries.
3. Generate an Audit-Grade Traceability Matrix: Produce formal compliance artifacts linking Jira/Issue ticket IDs, peer review sign-offs, test assertions, and data encryption verification.

## Core Regulatory Baselines Enforced
1. PCI-DSS v4.0 Requirement 3 & 6: Zero cleartext logging of cardholder data; mandatory peer review verification and input validation boundary checks.
2. SOC2 Type II (Security & Confidentiality): Every production commit must trace back to an authorized ticket ID and documented business justification.
3. SOX 404 (Financial Reporting Integrity): Audit trails on state-mutating ledger transactions, ledger balance assertions, and dual-authorization mechanisms.

## Workflow Execution
1. Scan code diffs for compliance violations (unmasked logging, missing parameter validation, hardcoded credentials).
2. Generate the Traceability Matrix Table linking Requirement/Ticket ID, Component, Regulatory Control Tag, Test Evidence, and Auditor Sign-Off.
3. Output the formal Compliance Attestation Certificate in markdown.

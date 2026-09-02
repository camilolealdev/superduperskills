---
name: cybersecurity
description: >
  Community cybersecurity knowledge suite containing 817 security skills mapped to
  MITRE ATT&CK, NIST CSF, and OWASP standards. Covers vulnerability assessment, secret scanning,
  threat modeling, hardining, and defense-in-depth auditing. Use when performing security audits,
  code vulnerability scanning, compliance readiness, or when user mentions "cybersecurity",
  "security audit", "mitre att&ck", "nist", "vulnerability scan", or "mukul975".
argument-hint: "[audit|mitre|owasp|threat-model|hardening]"
license: MIT
---

# Cybersecurity Skills — Community Defense & Security Framework

Based on [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) (31k+ ★), this community suite maps 817 security techniques to industry standards including **MITRE ATT&CK**, **NIST SP 800-53**, and **OWASP Top 10**.

> [!CAUTION]
> This suite contains security audit and defensive assessment techniques. Only execute vulnerability checks and security testing on systems you own or have explicit written authorization to test.

---

## Key Security Pillars

1. **Threat Modeling (STRIDE)**: Identifies Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege risks in system architectures.
2. **Secret & Credential Scanning**: Audits codebases for hardcoded API keys, certificates, private keys, and environment leaks.
3. **Dependency Vulnerability Auditing**: Checks package manifests (`package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`) against CVE databases.
4. **API Security & OWASP Validation**: Audits authentication boundaries, CORS policies, rate limiting, and SQL/XSS injection vulnerabilities.
5. **Infrastructure & Cloud Hardening**: Reviews Dockerfiles, Kubernetes manifests, IAM policies, and cloud storage bucket permissions.

# Architectural Resilience in Public Sector Identity Management: The Case for Federated Sovereignty

**Date:** February 2026

**Subject:** Cybersecurity, Identity and Access Management (IAM), Infrastructure Resilience


### Executive Summary: Ensuring Institutional Resilience

Current shifts toward centralized national identity providers introduce a **Single Point of Failure (SPOF)** for institutional infrastructure. This report demonstrates that total reliance on external authentication services creates a "Total Lockout" risk, jeopardizing research continuity. We propose a **Federated Sovereignty Model**—a low-cost, on-premise "Middleman" architecture—that ensures 24/7 availability, fulfills GDPR data minimization requirements, and maintains operational independence even during external service outages.


## 1. Introduction: The Centralization Trap

The digital transformation of public institutions and universities has led to a push for centralized "Identity-as-a-Service" (IDaaS) models, often tied to national eID frameworks (e.g., eIDAS, ID2020). While these systems streamline administrative processes, they introduce a critical **Single Point of Failure (SPOF)**. For high-stakes environments like research universities or public health services, total dependency on an external, state-operated authentication provider poses a significant risk to operational continuity.

## 2. The SPOF Risk and "Custodial Identity"

Current trends toward **Custodial Identity**—where a third-party entity holds the "master key" to an individual's digital existence—create a systemic vulnerability.

* **Operational Risk:** External outages or API changes in the national ID provider can paralyze internal services (Learning Management Systems, HPC clusters, Lab access).
* **Sovereignty Risk:** Institutions lose the ability to define their own trust levels and authentication methods (e.g., GPG, physical tokens).

**Source Citation:** 
> *“Centralized identity systems create honeypots of data and single points of failure that are inconsistent with the decentralized nature of the internet and the security requirements of modern research institutions.”* — (Simplified reference to: *Berners-Lee, T., et al. on Decentralized Identifiers (DIDs)*).

### Deep Dive: The SPOF Paradox in Public Infrastructure

To understand the risk, we must look at the **CIA Triad**—the foundational model for information security consisting of **Confidentiality, Integrity, and Availability**.

In engineering, a system is only as strong as its most dependent link. By mandating a single national gateway for all institutional access, we create a **Paradox of Trust**: while the individual identity is highly verified (increasing _Confidentiality_), the **Availability** of the system drops significantly. If the central gateway experiences a DDoS attack, a routing error, or a certificate expiration, the institution suffers a "Total Lockout" event.


## 3. Proposed Architecture: The Federated "Middleman" IdP

To mitigate these risks, we propose a **Federated Sovereignty Model**. In this architecture, the institution maintains an on-premise Identity Provider (IdP) such as **Keycloak** or **Authentik**.

### Key Advantages:

1. **Protocol Translation:** The IdP acts as a bridge between modern OIDC/SAML protocols and legacy LDAP/Header-auth systems.
2. **Authentication Fallback:** If the national ID system is offline, the local IdP can switch to secondary "Emergency" factors (e.g., TOTP or local Hardware Keys) to keep critical staff working.
3. **Data Minimization:** According to GDPR principles, the "Middleman" ensures that sub-applications only receive the specific attributes they need, rather than the full set of data provided by a national ID.

## 4. Prototype Implementation: A Low-Cost Proof of Concept (PoC)

A resilient prototype can be built using open-source software and industry-standard hardware. The goal is to demonstrate a "Sovereign Gateway" that allows login via either a National ID or a physical Hardware Key.

### Technical Stack:

* **Software:** Keycloak (Open Source Identity and Access Management).
* **Deployment:** Docker / Kubernetes on a local Linux server.
* **Hardware Token:** FIDO2/U2F compliant keys (e.g., YubiKey 5 Series or Nitrokey).

### Setup Steps (Generic):

1. **Instance Setup:** Deploy Keycloak on an internal virtual machine.
2. **Federation:** Configure an "Identity Provider Link" to the National ID (OIDC/SAML).
3. **Authentication Flow:** Create a "Browser Flow" that offers a choice: "Login via National ID" OR "Login via Hardware Key (Emergency/High Security)."
4. **Hardware Binding:** Register the FIDO2 key to a test user account.

### Cost Estimate (Prototype Phase):

| Item | Description | Estimated Cost |
| --- | --- | --- |
| **Server Hardware** | Existing VM or a refurbished NUC | €0 - €300 |
| **Software Licensing** | Keycloak / Authentik (Open Source) | €0 |
| **Hardware Keys** | 2x FIDO2/U2F Tokens (e.g., YubiKey) | €110 (€55/ea) |
| **Setup Time** | ~10-15 Engineer Hours | Internal |
| **Total** | **Minimal entry cost** | **~€110 - €410** |


### Proof of Concept: Hardware Key Binding

The technical flow for the **€110 prototype** could look like this:

* **Registration:** The user logs in once via the "official" (but shaky) National ID.
* **Binding:** Keycloak prompts the user: *"Would you like to register a Hardware Security Key for emergency access?"*
* **WebAuthn Handshake:** The user touches their YubiKey. A public/private key pair is generated. The public key is stored in your local Keycloak.
* **The Result:** The next time the National ID server is down, the user simply selects "Alternative Login," touches their key, and is granted access based on the **local** trust relationship.

Adding a **Risk Assessment Matrix** is the ultimate "manager-speak" move. It translates technical anxiety into a format that decision-makers (and insurance-minded university boards) actually understand.

In a professional risk analysis, we look at **Probability** (how likely is it to happen?) vs. **Impact** (how bad is it if it happens?).


## 5. Risk Assessment: Centralized vs. Federated Identity

The following matrix evaluates the risk profile of total reliance on a singular national eID provider compared to the proposed federated model.

| Risk Scenario | Probability | Impact (Centralized) | Impact (Federated) |
| --- | --- | --- | --- |
| **External Service Outage** (DDoS, API failure) | Medium | **Critical** (Total Lockout) | **Low** (Fallback to local IdP) |
| **Identity Hijacking** (Credential theft) | Low | **High** (Access to all services) | **Medium** (Access limited by ABAC) |
| **Administrative/Legal Lockout** (Expired eID) | Medium | **High** (Researcher cannot work) | **Low** (Internal ID remains active) |
| **Maintenance Downtime** (National registry) | High | **Medium** (Service interruption) | **None** (Seamless local session) |

### Analysis of the "A" in CIA:

Under a **Centralized Model**, the institutional risk is binary: if the external provider is down, the institution is 100% offline. Under the **Federated Model**, the institution maintains a "Safety Buffer." Even if the probability of a national outage is low, the **Impact** is so high that failing to provide a local fallback violates standard **Business Continuity Planning (BCP)** protocols.


## 6. Conclusion

Digital sovereignty is not a luxury; it is a requirement for institutional resilience. By implementing a federated IdP, public services can leverage the benefits of national ID systems without sacrificing their operational independence or the security of their specialized research environments.

### References & Standards

1. **NIST Special Publication 800-63-3:** *Digital Identity Guidelines.* National Institute of Standards and Technology. (Focuses on why "Authentication Assurance Levels" (AAL) should be diverse and resilient).
2. **W3C Web Authentication (WebAuthn):** *A Level 3 Specification.* (The standard for FIDO2 and hardware keys like YubiKeys).
3. **RFC 6749:** *The OAuth 2.0 Authorization Framework.* (The backbone of Keycloak/Authentik federation).
4. **Internet Engineering Task Force (IETF) - Self-Sovereign Identity (SSI) Drafts:** Addressing the shift from "Administrative" to "User-Centric" identity models.
5. **ENISA (European Union Agency for Cybersecurity):** *Opinion on the implementation of eIDAS.* (Specifically sections regarding the availability and cross-border resilience of identity providers).



# Improving HPC System Login with Hardware Security Keys: Usability, Standards and UI/UX Considerations

**Summary**

High-performance computing (HPC) environments frequently suffer from cumbersome login processes, such as mandatory complex passwords combined with one-time passwords (OTPs), often delivered via SMS, while more secure and convenient options like SSH public keys or hardware security tokens remain underutilized or disabled.

The article advocates greater adoption of **hardware security keys** (especially YubiKeys) that support modern standards like **FIDO2** and **U2F**. These provide **phishing-resistant**, **multi-factor authentication** (MFA) using public-key cryptography, where private keys never leave the device. This approach resists phishing, replay, and man-in-the-middle attacks far better than SMS OTPs (vulnerable to SIM swaps and interception) or even app-based TOTP (vulnerable if the device is compromised).

## Key Authentication Methods Compared

| Method              | Security Level          | Usability              | Offline Capability | Main Drawbacks                          |
|---------------------|-------------------------|------------------------|--------------------|-----------------------------------------|
| **SMS OTP**         | Low (SIM swap risk)     | High familiarity       | No (needs network) | Interception, phishing                  |
| **TOTP App**        | Moderate (shared secret)| Good                   | Yes                | Device compromise risk, multi-device hassle |
| **YubiKey / FIDO2** | High (phishing-resistant)| Very good (physical touch) | Yes            | Requires carrying hardware              |
| **Government eID**  | High (crypto + legal binding) | Moderate (needs reader/middleware) | Usually no | Onboarding friction, privacy concerns   |

**Recommendation**: Use hardware keys (e.g., YubiKey) as the primary method + TOTP app as backup. Deprecate SMS except as last-resort fallback.

## Usability and UI/UX Issues

Common pain points in HPC terminal logins:

- Misleading prompts (e.g., "SMS challenge sent, please enter OTP:" appears even when a hardware key is registered → causes user confusion and hesitation).
- No visual feedback when typing passwords (standard for security, but feels unresponsive → users question if input is accepted).
- Hidden or unclear support for hardware tokens → users default to slower OTP paths.

**Proposed improvements**:

- Better prompts, e.g.:

  ```
  Two-Factor Authentication:
  [1] Touch your YubiKey now
  [2] Or enter OTP from SMS: _______
  ```

  or

  “Touch your security key now, or if you prefer enter the SMS code you received.”

- Add explanatory text for hidden password input: “(input hidden for security)”.
- Detect key presence and prioritize hardware token option.
- Onboarding messages: “Register your security key today to skip OTP codes.”

## Practical Guidance for HPC Administrators

1. Enable SSH public-key authentication, especially hardware-bound types like `ed25519-sk` or `ecdsa-sk`.
2. Modify login prompts (via SSH/PAM) to clearly support dual paths (hardware key preferred).
3. De-emphasize / phase out SMS after hardware key registration.
4. Create clear onboarding docs and training materials.
5. Add terminal feedback messages for better perceived usability.
6. Monitor adoption rates and gradually retire weaker MFA options.

## Conclusion

Integrating hardware security keys with FIDO2/U2F standards into HPC login flows significantly improves both **security** (phishing resistance, no shared secrets) and **usability** (faster passwordless or low-friction logins, clearer prompts). Thoughtful UI/UX adjustments reduce user frustration, lower support tickets, and encourage secure behavior without sacrificing performance critical to HPC workflows.
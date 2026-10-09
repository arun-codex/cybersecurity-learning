# 🦈 Day 40 — TLS + HTTPS Analysis

**Status: ✅ Complete — practical capture, SOC mini-investigation, and final active recall passed (3.5/4).**

## 🎯 Goal

Recognize TLS handshake traffic in Wireshark, distinguish TCP from TLS, identify encrypted application data, and explain which evidence remains useful to a SOC analyst.

## 🧪 Practical work performed

Generated HTTPS traffic with:

```bash
curl https://example.com
```

Captured on the Wi-Fi interface `wlp0s20f3` and used Wireshark display filters.

### Client Hello

Observed in the capture:

- Client source port: `50804`
- Server destination port: `443`
- Requested hostname/SNI: `example.com`
- Client advertised TLS 1.2 and TLS 1.3 support in `supported_versions`
- Wireshark listed 35 offered cipher suites
- Extensions included `server_name`, `supported_versions`, `application_layer_protocol_negotiation`, and `key_share`
- Client key-share groups shown included `X25519MLKEM768` and `X25519`

### Server Hello

Observed:

- Server source port: `443`
- Client destination port: `50804`
- The `supported_versions` extension indicated negotiated TLS 1.3 (`0x0304`)
- Selected cipher suite: `TLS_AES_256_GCM_SHA384` (`0x1302`)
- Server key-share information included `X25519MLKEM768`

**Interpretation:** The client advertises supported options in Client Hello; the server responds with the negotiated parameters in Server Hello. Do not interpret the legacy `Version: TLS 1.2 (0x0303)` field in isolation—the `supported_versions` extension indicated TLS 1.3 for this handshake.

### Certificate filter observation

Tried:

```text
tls.handshake.type == 11
```

Wireshark showed 103 captured packets and 0 packets matching this filter in that view.

This is consistent with TLS 1.3 handshake messages after Server Hello being encrypted when session secrets are unavailable. **The zero-result filter does not prove a certificate was absent**; the encrypted certificate message may not be decoded as handshake type 11.

### Encrypted application data

Inspected a TLS application-data record. Wireshark showed:

- Record type: Application Data (23)
- TLS record data length: 3,853 bytes
- Reassembled TCP data: 3,858 bytes across two TCP segments (3,651 + 207 bytes)
- The selected frame was 293 bytes on the wire and contained 207 bytes of TCP payload

These lengths describe different layers and should not be conflated. The HTTP page content was not readable from the encrypted payload without appropriate TLS secrets.

## 🕵️ SOC mini-investigation

Scenario: an internal host connects to a remote server over HTTPS. The application traffic cannot be decrypted.

### Evidence identified

1. **Client and server IPs** — identify the communicating hosts, not necessarily the person behind the activity.
2. **Client and server ports** — help identify endpoints and likely service; in this capture the client used source port `50804` and the server used port `443`.
3. **Packet sizes/data volume** — help investigate unusually large or small transfers; size alone does not prove maliciousness.
4. **DNS activity** — can link a hostname to an IP and show query history. Correlate with subsequent connections; a DNS lookup alone does not prove a visit.
5. **Connection frequency** — repeated connections (for example, 200 in 10 minutes) merit comparison with the host/application baseline, timing, failures, destinations, and endpoint telemetry.

Other observable evidence can include timing/duration, TLS handshake metadata, certificate details when available, and connection behavior. HTTPS or high connection frequency alone does not prove malicious activity.

## 🧠 Recall checkpoint

Earlier recall was successful for:
- Destination port 443
- SNI hostname `example.com`
- Client advertised TLS 1.2 and TLS 1.3
- Server Hello was sent by the server
- TLS 1.3 was negotiated
- Client Hello offers options; Server Hello selects connection parameters

### Final recall results — passed (3.5/4)

1. **TCP vs TLS — mostly correct:** TCP establishes the connection and provides reliable, ordered data delivery; the three-way handshake is the connection-establishment process. TLS protects application communication through encryption, integrity and authentication.
2. **Sequence — correct:** TCP connection → TLS handshake → encrypted application traffic.
3. **Certificate visibility — correct:** TLS 1.3 encrypts the Certificate message after Server Hello; without the appropriate session secrets, Wireshark may not decode it as a Certificate.
4. **SOC investigation — correct:** frequent HTTPS connections alone do not prove malicious activity. Investigate source/destination IPs and ports, compare connection frequency with normal behavior, and inspect timing, traffic volume, DNS history and endpoint telemetry when available.

## ✅ Definition of done

**Definition of done met.** Practical capture, analysis, SOC evidence exercise and final active recall are complete.

## 🎯 Next session

**Day 41 — continue Week 6 Wireshark analysis.**

## 🔑 Key lesson

```text
TCP connection
      ↓
TLS handshake
      ↓
Encrypted application traffic

Encryption hides application content, not all network evidence.
```

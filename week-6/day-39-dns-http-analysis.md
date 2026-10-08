# 🦈 Day 39 — DNS + HTTP Packet Analysis

## 🎯 Goal

Connect Week 2 DNS/HTTP knowledge with real packets.

## 🌐 DNS Packet Analysis

### Lab

- Captured DNS traffic on `wlp0s20f3`
- Used:
  `dig example.com`
- Wireshark filters:
  - `dns`
  - `dns.qry.name == "example.com"`

### DNS response analyzed

Client:
- IP: `192.168.1.9`
- Source port: `43052`

DNS server:
- IP: `192.168.1.1`
- Destination port: `53`

Query:
- Hostname: `example.com`
- Type: `A`
- Transaction ID: `0x46c4`

Response:
- Flags: `0x8180` — Standard query response, No error
- Questions: `1`
- Answer RRs: `2`
- Authority RRs: `0`
- Additional RRs: `1`
- A record: `104.20.23.154`
- A record: `172.66.147.243`
- Response time: ~`69.4 ms`

### 🔗 DNS correlation

Confirmed that the DNS query and response use the same transaction ID:

`0x46c4`

Mental model:

```text
192.168.1.9:43052
      │
      │ DNS query: example.com / A
      │ Transaction ID: 0x46c4
      ▼
192.168.1.1:53
      │
      │ DNS response: No error
      │ Transaction ID: 0x46c4
      │ A → 104.20.23.154
      │ A → 172.66.147.243
      ▼
192.168.1.9
```

## 🌐 HTTP Packet Analysis

Created a local HTTP lab using Python's HTTP server:

```bash
mkdir -p ~/cybersecurity-lab/week-6-wireshark/http-lab
cd ~/cybersecurity-lab/week-6-wireshark/http-lab
echo "Wireshark HTTP Lab" > index.html
python3 -m http.server 8000
```

Generated the request with:

```bash
curl http://127.0.0.1:8000
```

Captured traffic on the Linux loopback interface `lo`.

### TCP + HTTP flow observed

```text
TCP SYN
   ↓
TCP SYN/ACK
   ↓
TCP ACK
   ↓
HTTP GET /
   ↓
HTTP 200 OK
   ↓
TCP connection termination
```

### HTTP request analyzed

- Request: `GET / HTTP/1.1`
- Method: `GET`
- URI: `/`
- Version: `HTTP/1.1`
- Host: `127.0.0.1:8000`
- User-Agent: `curl/8.18.0`

### HTTP response analyzed

- Status: `200 OK`
- Content-Type: `text/html`
- Content-Length: `19`

## 🧠 SOC interpretation

A client using curl requested `/` from an HTTP server on port `8000`. The server successfully returned an HTML response with HTTP status `200 OK`.

Important evidence extracted from packets:
- Source/destination IPs
- Source/destination ports
- DNS transaction ID
- Requested hostname
- DNS record type and returned IPs
- HTTP method and URI
- Host header
- User-Agent
- HTTP status
- Content type and length

## 🧠 Mental Model

```text
DNS:
Client → DNS query → DNS server
Client ← DNS response ← DNS server

HTTP:
HTTP
 ↓
TCP
 ↓
IP
 ↓
Loopback/Ethernet
```

## ✅ Definition of Done

- [x] Analyze a DNS query
- [x] Analyze a DNS response
- [x] Match DNS query and response using Transaction ID
- [x] Identify A records
- [x] Determine whether DNS resolution succeeded
- [x] Capture a local HTTP request
- [x] Identify HTTP GET
- [x] Identify Host and User-Agent
- [x] Identify HTTP 200 OK
- [x] Identify Content-Type and Content-Length
- [x] Explain HTTP as application data carried over TCP

## 📌 Status

**Day 39 — ✅ Complete**

Next: **Day 40 — TLS Analysis**

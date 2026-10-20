---
name: setup
description: Set up Leash or check whether Leash is connected, without reading personal account data.
---

Call the Leash check_connection tool (commonly exposed as leash_check_connection) with input {}, reason "Confirm Leash is connected", context "Leash setup". Only say connected if the result says connected true and isError false. Do not read email, files or other private accounts to test setup. If authentication is needed, let the host open Leash sign-in. After success, explain that protections and per-AI permissions are at https://openleash.com/personal. This skill does not silently modify global instructions or claim to have saved memory. If the user requests a permanent preference, use the host's supported personal instructions mechanism, preserve existing content, and save only the credential-free Leash rule. If unavailable, give concise manual steps. Never save a token or private URL into memory or a project file.

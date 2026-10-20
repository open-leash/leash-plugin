# Leash

A little peace of mind for your AI. Free during the pilot.

Leash connects your AI to your accounts through configurable protections. Review activity, control each AI's access, and undo supported reversible actions when undo is enabled. Only activity routed through Leash is covered.

## Install

Install Leash from your AI's plugin directory when its listing is available, or install this package from GitHub in clients that support repository plugins. Enable the Leash connection and sign in at **openleash.com** when prompted. Each installation receives a separate, revocable connection. The shared endpoint is **https://secure.openleash.com/mcp**. Never append another person's token or put a personal link in a public package.

For Gemini CLI: `gemini extensions install https://github.com/open-leash/leash-plugin`. Run `/mcp auth leash` if sign-in is requested. For OpenClaw, use `openclaw plugins install git:github.com/open-leash/leash-plugin@v1.0.0`, then inspect the enabled `leash` bundle. Its compatibility format is Cursor; no native code runs. For other clients, use their remote HTTP server option with the shared endpoint and OAuth. A public directory submission is not the same as an approved listing. Check the release notes for current availability.

Run the Leash setup skill or ask: "Check Leash is connected without accessing my personal accounts." Success must come from the check_connection tool, not merely from listing available tools. Then connect the accounts you want at https://openleash.com/personal.

## Instructions and privacy

This package includes a setup skill and a personal-account skill. Cursor loads a packaged rule and Gemini CLI loads GEMINI.md while the extension is enabled. A plugin cannot guarantee that all AI activity uses Leash. For a permanent preference in other clients, add the credential-free rule from GEMINI.md to the client's supported personal instructions. Preserve your other instructions. Never add credentials to memory or shared files.

Protection checks may process relevant request and response content with TypeSafe JEV. Audit history is retained for 90 days. When undo is enabled, supported recovery details are encrypted and retained for up to 7 days. Turning undo off stops new recovery capture. Read https://openleash.com/privacy for the full policy.

## Remove

Disable or uninstall the plugin in your AI, remove any Leash-specific saved preference you added, then remove its connection in Your AIs at https://openleash.com/personal. Removing that connection revokes access immediately without disconnecting other AIs.

## Support

https://openleash.com/contact · max@openleash.com

Privacy: https://openleash.com/privacy · Terms: https://openleash.com/terms

This repository contains only public integration metadata, instructions and brand assets. Leash's gateway and protection engine remain private.

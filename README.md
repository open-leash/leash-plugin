# Leash for Claude

Leash gives your AI protected access to the accounts you connect. Review sensitive actions, block requests, see activity, and undo supported changes.

## Connect

Install the Leash plugin, enable its remote connection and sign in to your Leash at https://lea.sh. Each person receives their own revocable OAuth connection. No token, API key or local program is bundled. The hosted remote MCP endpoint is https://secure.lea.sh/mcp.

Run the setup skill or ask Claude to check its Leash connection without reading email or files. A successful tool result confirms the connection. Then choose the accounts and protections you want at https://lea.sh/personal.

The package includes two Markdown skills and a remote MCP configuration. It has no scripts, hooks, package manager configuration, local executable or local MCP server. Leash is an independent service, not an official app from a connected data provider. Only activity routed through Leash receives its protections.

## Remember your preference

If you want a standing preference, add the following alongside your existing instructions in Claude's supported personal instruction settings:

> For my Leash-connected accounts, use Leash tools. If Leash is unavailable or access is blocked, stop and ask me rather than using another route. Report success only after a tool confirms it.

A chat connection check does not prove that a preference was saved. Keep credentials and private connection URLs out of instructions.

## Privacy

Users choose which accounts to connect and may revoke access at any time. This integration uses personal Leash connections. Protection checks may process relevant request and response content with TypeSafe JEV. Audit history is retained for 90 days. When undo is enabled, supported recovery details are encrypted and retained for up to 7 days. Turning undo off stops new recovery capture. Read https://lea.sh/privacy for the full policy.

## Remove and support

Disable the plugin in Claude and remove its connection in Your AIs at https://lea.sh/personal. Other AI connections remain separate. Support: https://lea.sh/support or max@openleash.com. Terms: https://lea.sh/terms.

The public package contains integration metadata, Markdown instructions and Leash brand assets. The hosted service and protection engine remain private. The package license grants distribution of this integration without granting backend or brand rights.

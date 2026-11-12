# MyListerHub for Claude and ChatGPT

Run your eBay store from chat. This plugin connects Claude or ChatGPT to your [MyListerHub](https://www.mylisterhub.com) account through the MyListerHub MCP server, and adds skills for everyday selling work.

You need a MyListerHub account with an active subscription and a connected eBay account. Setup help: https://www.mylisterhub.com/connect-ai-assistants

## What's inside

| Skill | What it does |
| --- | --- |
| `get-started` | First-run tour: checks the connection and shows a store snapshot |
| `daily-store-check` | Briefing on orders to ship, buyers waiting, sold-out listings and the last 7 days of sales |
| `list-an-item` | Guided new eBay listing, from item details to a live listing |
| `answer-buyers` | Drafts replies to unanswered buyer messages, sending each only after you approve it |

The MCP server (`https://app.mylisterhub.com/mcp`) does the work: you sign in with your MyListerHub account in the window that opens, and the assistant only sees what your MyListerHub user can. Changes to prices, quantities, listings and buyer replies go live on eBay right away, and the assistant is set up to ask before making one.

## Install

**Claude Code**

```bash
claude plugin marketplace add FmTod/mylisterhub-ai-plugin
claude plugin install mylisterhub@mylisterhub
```

Then run `/mcp`, pick the MyListerHub server and choose **Authenticate**.

**Claude (web, desktop)**: upload `dist/claude.zip` under **Customize → Plugins → Add → Upload plugin**, then connect MyListerHub from the plugin's **Connectors** tab. To use only the connector, follow the setup page above.

**ChatGPT**: install MyListerHub from the plugin directory once it's listed. Until then, follow the setup page above.

## Layout

One repo serves both vendors. The skills and icons are shared; each vendor reads its own manifest and MCP file.

| Path | Read by |
| --- | --- |
| `plugin.json`, `mcp.json` | ChatGPT and other [Agent Plugins](https://agent-plugins.org) clients. `plugin.json` also holds the ChatGPT listing, review test cases and release notes under `extensions.com.openai` |
| `.claude-plugin/plugin.json`, `.mcp.json` | Claude |
| `.claude-plugin/marketplace.json` | Claude Code's `plugin marketplace add` |
| `skills/<name>/SKILL.md` | Both |
| `assets/` | Directory icons |

Keep `name` and `version` the same in both manifests, and the server URL the same in both MCP files.

## Build the upload ZIPs

```bash
python3 scripts/build.py
```

It checks that the two manifests and MCP files agree and that every skill's frontmatter is accepted by claude.ai, then writes `dist/chatgpt.zip` and `dist/claude.zip`.

## Releasing

Bump `version` in both manifests, build, and upload the new ZIP: ChatGPT under **platform.openai.com/plugins → Upload plugin to make changes**, Claude through the plugin upload above. Changes to the MCP server's tools reach ChatGPT through OpenAI's daily rescan and need no new ZIP.

The review test cases in `plugin.json` run against the reviewer account that the MyListerHub app's `mcp:create-review-tenant` command creates. When a tool is renamed or that sample data changes, update the test cases to match.

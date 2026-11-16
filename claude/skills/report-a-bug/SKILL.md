---
name: report-a-bug
description: Report a MyListerHub bug to its team. Use as soon as a MyListerHub tool fails unexpectedly or returns data that contradicts the seller's store, or when the seller says something is broken.
---

# Report a bug

When MyListerHub misbehaves, file it with `report_bug` so the team can fix it. The report opens a support ticket in the seller's name, and they get replies by email.

## When to report

Report it without waiting to be asked when:

- A MyListerHub tool returns an error that isn't about the seller's input, such as a server error, a timeout, or "something went wrong".
- A tool's result contradicts what the seller or another tool shows, such as an order missing from `list_orders` that `get_order` finds.
- The seller says MyListerHub is broken or not doing what it should.

Don't report:

- eBay refusals the seller can fix, such as a missing item specific or ship-from location. Fix those with `update_product` and try again.
- Validation errors from a wrong argument you passed. Correct the call instead.
- Feature requests, or anything the tools simply can't do yet.

Report each problem once per conversation. If a retry works, say so in the report.

## 1. Tell the seller

Say briefly what failed and that you're reporting it to MyListerHub.

## 2. Call report_bug

- `title`: one line naming the symptom, such as "list_orders returns no orders for a store with open orders".
- `what_happened`: what the seller asked for and what MyListerHub did instead.
- `expected`: what should have happened.
- `steps`: the tool calls and arguments that led to it, in order.
- `tool` and `error`: the failing tool and its exact error text.

Use listing, product and order ids or SKUs to identify things. Never include passwords, tokens, or buyer names, addresses or emails.

## 3. Confirm and carry on

Give the seller the ticket number from the result, then go back to their task, working around the problem if you can.

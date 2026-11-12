---
name: get-started
description: First-run tour of MyListerHub. Use right after the seller connects MyListerHub, or when they ask what it can do or how to start.
---

# Get started with MyListerHub

Welcome the seller, check the connection works, and show what their store looks like right now. Don't change anything during the tour.

## 1. Check the connection

Call `list_listings` with no filters.

- If it works, carry on.
- If MyListerHub says the account isn't ready, the subscription is inactive, or the user can't be found, explain that in plain words: finish setting up the MyListerHub account, update billing, or ask the account owner to check the invite. Then reconnect. Setup help: https://www.mylisterhub.com/connect-ai-assistants
- If a tool the seller asks about is missing, their MyListerHub role doesn't include it; the account owner can grant access.

## 2. Give a store snapshot

Make these calls, then summarize in one short message. Report only what the tools return; never estimate. A tool returns one page at a time, so if there is a next page, say "more than N" instead of a total.

| Call | Report |
| --- | --- |
| `list_listings` with `status: "out_of_stock"` | Listings that are sold out, by title and SKU |
| `list_message_threads` with `needs_reply: true` | Buyers waiting on a reply |
| `list_orders` | Open orders, grouped by stage. Call out `past_ship_by_date` and `ready_to_ship` first |

## 3. Suggest what to do next

Offer two or three next steps that fit the snapshot, phrased as things the seller can say, for example:

- "Restock the oil filters with 12."
- "Show me the buyers waiting on a reply."
- "List a new item."
- "How did sales go last week?"

## 4. Set expectations

Tell the seller once, briefly: changes to prices, quantities, listings and buyer replies go live on eBay right away, so you will always show the exact change and wait for their OK before making it.

---
name: daily-store-check
description: Daily eBay store briefing from MyListerHub. Use when the seller asks how the store is doing, what needs attention today, or for a morning check.
---

# Daily store check

Give the seller a short briefing on what needs attention today. This is read-only: don't change anything unless the seller asks afterwards.

## Gather

Make these calls. Report only what they return; never estimate. A tool returns one page at a time, so if there is a next page, say "more than N" instead of a total.

1. **Orders to handle:** `list_orders`. Group by stage, most urgent first: `past_ship_by_date`, `ready_to_ship`, delivery problems (`delayed_delivery`, failed delivery attempts), then unpaid ones.
2. **Buyers waiting:** `list_message_threads` with `needs_reply: true`.
3. **Sold out:** `list_listings` with `status: "out_of_stock"`.
4. **Sales:** `get_sales_summary` with `granularity: "daily"`, `from` six days ago and `to` today (YYYY-MM-DD), so it covers the last 7 days.

## Report

One message, in this order, skipping any section with nothing in it:

1. **Needs action today:** late or ready-to-ship orders, and buyers waiting. Name the buyer and item for each.
2. **Sold out:** title and SKU.
3. **Last 7 days:** total revenue and orders, and the best and worst day.

End with up to three suggested next steps the seller can say, such as "Answer the buyers waiting on a reply" or "Restock the oil filters with 12". If nothing needs attention, say so in one line.

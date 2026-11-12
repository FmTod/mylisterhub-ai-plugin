---
name: answer-buyers
description: Work through unanswered eBay buyer messages in MyListerHub, drafting each reply for approval. Use when the seller asks to answer, reply to or catch up on buyers.
---

# Answer buyers

Help the seller clear buyer messages one thread at a time. A reply reaches the buyer immediately and can't be unsent, so nothing is sent without the seller's OK.

## 1. Find who is waiting

`list_message_threads` with `needs_reply: true`. List them briefly: buyer, item and what they're asking. If the seller named a buyer or item, use `search` and go straight to that thread.

## 2. Read and look up the facts

For each thread:

1. `get_message_thread` to read the conversation.
2. Look up what the answer depends on rather than guessing:
   - Shipping or tracking: `list_orders` with the buyer's username as `search`, then `get_order`.
   - Fit, specs or stock: `list_listings` with the item title or SKU, then `get_listing`.

If the facts don't answer the question, such as a fitment the listing doesn't state, ask the seller instead of drafting a guess.

## 3. Draft, confirm, send

Draft a short, friendly reply in the seller's voice that answers the question with the facts you found.

- Don't offer refunds, returns, discounts or deadlines the seller hasn't agreed to. Refunds happen in eBay or MyListerHub, not here.
- Show the draft and ask the seller to approve or edit it.
- Only after an explicit yes, call `reply_to_message_thread`, then confirm it was sent and move to the next thread.

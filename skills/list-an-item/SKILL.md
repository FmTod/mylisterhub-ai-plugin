---
name: list-an-item
description: Guided new eBay listing through MyListerHub. Use when the seller wants to list, sell or post a new item on eBay.
---

# List an item on eBay

Walk the seller from a description of an item to a live eBay listing. Never guess a fact about the item: ask.

## 1. Collect the details

Ask for anything missing, in one message:

- What the item is: title, brand, part number or model, condition.
- Price and quantity.
- Photos: public `https` links. eBay won't list an item without at least one. Photos dropped into the chat can't be used.
- The city and ZIP it ships from. eBay refuses a listing without them.

## 2. Pick the category and item specifics

1. `find_ebay_categories` with the item's title. If the top matches are close, show the best two or three and let the seller choose.
2. `get_ebay_category_item_specifics` for that category. Fill required specifics from what the seller told you. Ask for any required value you don't have; never invent one.
3. If the seller has more than one eBay account, business policy or listing format, call `get_ebay_listing_options` and ask which to use.

## 3. Create and check

1. `create_product` with the details, category, item specifics, photo links and ship-from location.
2. `check_product_for_ebay`. Nothing goes live in this step. If eBay reports problems, fix them with `update_product` and check again. Ask the seller when a fix needs information you don't have.

## 4. Confirm, then list

Show the seller a summary: title, category, condition, price, quantity, ship-from location and photo count. Say it will go live to buyers on eBay. Wait for an explicit yes.

Then call `list_product_on_ebay`. Listing is queued: about a minute later, call `get_product` to find the new listing, then `get_listing` to report its status and any errors eBay returned.

import re
from datetime import datetime, timezone

import scrapy

from echochain_scraper.items import ListingItem


class MockEbaySpider(scrapy.Spider):
    """
    Spider for the EchoChain mock listing page (mock_ebay_listings.html).

    Points at a local file for now, since scraping live eBay pages
    without permission violates their Terms of Service. Swapping to
    a real, permitted source later only requires changing start_urls -
    the parse() logic and Item schema stay the same.
    """

    name = "mock_ebay"

    # file:// path lets Scrapy read the local mock HTML directly,
    # same as it would fetch a real page over http(s)
    start_urls = ["file:///C:/Users/Sharanya/Documents/Internships/Infotact/Project 2 - EchoChain/mock_ebay_listings.html"]

    def parse(self, response):
        cards = response.css(".s-item")
        self.logger.info(f"Found {len(cards)} listing cards on page")

        for card in cards:
            yield self.parse_card(card)

    def parse_card(self, card):
        item = ListingItem()

        # --- identity / core fields ---
        item["listing_url"] = card.css("a.s-item__link::attr(href)").get()
        item["listing_id"] = card.attrib.get("data-listing-id")
        item["title"] = self.clean_text(
            card.css("h3.s-item__title::text").get()
        )
        
        # --- condition / seller notes (often missing - see listing 2, 6) ---
        subtitle = card.css(".s-item__subtitle::text").get()
        item["seller_notes"] = self.clean_text(subtitle) or None
        item["condition"] = self.clean_text(
            card.css(".SECONDARY_INFO::text").get()
        )

        # --- price fields ---
        item["price"] = self.parse_price(
            card.css(".s-item__price::text").get()
        )
        item["shipping_price"] = self.parse_shipping(
            card.css(".s-item__shipping::text").get()
        )

        # --- market signal fields ---
        item["bids"] = self.parse_int(
            card.css(".s-item__bids::text").get()
        )
        item["watchers"] = self.parse_int(
            card.css(".s-item__watchcount::text").get()
        )
        item["location"] = self.clean_text(
            card.css(".s-item__location::text").get()
        )

        # --- item specifics: flattened from a variable-length <ul> ---
        # not every listing has every specific, so we build a dict of
        # whatever IS present, then pull known keys out of it
        specifics = {}
        for li_text in card.css(".s-item__specifics li::text").getall():
            if ":" in li_text:
                key, _, value = li_text.partition(":")
                specifics[key.strip().lower()] = value.strip()

        item["brand"] = specifics.get("brand")
        item["model"] = specifics.get("model")
        item["processor"] = specifics.get("processor")
        item["ram_gb"] = self.parse_int(specifics.get("ram size"))
        item["ssd_gb"] = self.parse_int(specifics.get("ssd capacity"))
        item["screen_size_in"] = specifics.get("screen size")

        item["scraped_at"] = datetime.now(timezone.utc).isoformat()

        return item

    # ------------------------------------------------------------------
    # Cleaning helpers - centralised here so every field goes through
    # the same normalisation before it reaches the Item, rather than
    # inline parsing scattered through parse_card().
    # ------------------------------------------------------------------

    @staticmethod
    def clean_text(value):
        if value is None:
            return None
        cleaned = value.strip()
        return cleaned if cleaned else None

    @staticmethod
    def parse_price(value):
        if not value:
            return None
        digits = re.sub(r"[^0-9.]", "", value)
        try:
            return float(digits) if digits else None
        except ValueError:
            return None

    @staticmethod
    def parse_shipping(value):
        if not value:
            return None
        if "free" in value.lower():
            return 0.0
        return MockEbaySpider.parse_price(value)

    @staticmethod
    def parse_int(value):
        if not value:
            return None
        digits = re.sub(r"[^0-9]", "", str(value))
        return int(digits) if digits else None
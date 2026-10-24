import json
import os
from collections import defaultdict

DATA_FILE = "backlink_data.json"

def simulate_backlink_collection():
    """
    Simulates collecting backlink data for various local competitors.
    In a real scenario, this would involve API calls to SEO tools or web scraping.
    """
    print("Simulating initial backlink data collection...")
    # This data would typically come from an SEO tool API or manual research
    backlinks = [
        {"competitor": "LocalBiz A", "referring_domain": "blog.tech.com", "domain_authority": 80, "anchor_text": "best local services"},
        {"competitor": "LocalBiz A", "referring_domain": "cityguide.org", "domain_authority": 65, "anchor_text": "top local provider"},
        {"competitor": "LocalBiz A", "referring_domain": "reviewsite.net", "domain_authority": 70, "anchor_text": "LocalBiz A reviews"},
        {"competitor": "LocalBiz B", "referring_domain": "industrynews.com", "domain_authority": 85, "anchor_text": "innovative solutions"},
        {"competitor": "LocalBiz B", "referring_domain": "localchamber.org", "domain_authority": 60, "anchor_text": "trusted business"},
        {"competitor": "LocalBiz B", "referring_domain": "blog.tech.com", "domain_authority": 80, "anchor_text": "LocalBiz B services"}, # Shared domain
        {"competitor": "LocalBiz C", "referring_domain": "smallbiz.net", "domain_authority": 55, "anchor_text": "affordable options"},
        {"competitor": "LocalBiz C", "referring_domain": "communityforum.com", "domain_authority": 40, "anchor_text": "LocalBiz C discussion"},
    ]
    return backlinks

def save_backlink_data(data):
    """
    Saves the collected backlink data to a JSON file.
    This demonstrates the core concept of "saving once" to avoid repeated data collection.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Backlink data saved to {DATA_FILE}")

def load_backlink_data():
    """
    Loads backlink data from the JSON file if it exists.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"Backlink data loaded from {DATA_FILE}")
        return data
    return None

def generate_competitor_report(backlinks_data):
    """
    Generates a simple report comparing local competitors based on backlink metrics.
    This is the "Yerel Rakip Açık Raporu" (Local Competitor Open Report) part of the article.
    """
    if not backlinks_data:
        print("No backlink data available to generate a report.")
        return

    competitor_metrics = defaultdict(lambda: {"total_backlinks": 0, "unique_domains": set(), "total_da": 0})

    for link in backlinks_data:
        competitor = link["competitor"]
        competitor_metrics[competitor]["total_backlinks"] += 1
        competitor_metrics[competitor]["unique_domains"].add(link["referring_domain"])
        competitor_metrics[competitor]["total_da"] += link["domain_authority"]

    print("\n--- Local Competitor Backlink Report ---")
    print("----------------------------------------")
    
    # Sort competitors for consistent output
    sorted_competitors = sorted(competitor_metrics.keys())

    for competitor in sorted_competitors:
        metrics = competitor_metrics[competitor]
        total_links = metrics["total_backlinks"]
        unique_doms = len(metrics["unique_domains"])
        avg_da = metrics["total_da"] / total_links if total_links > 0 else 0

        print(f"\nCompetitor: {competitor}")
        print(f"  Total Backlinks: {total_links}")
        print(f"  Unique Referring Domains: {unique_doms}")
        print(f"  Average Domain Authority: {avg_da:.2f}")
        # Highlight potential weaknesses/opportunities based on simple thresholds
        if unique_doms < 3: # Example threshold
            print(f"  Insight: {competitor} has few unique domains. Opportunity for diverse link building.")
        if avg_da < 60: # Example threshold
            print(f"  Insight: {competitor}'s average DA is low. Target high-authority links.")
    print("----------------------------------------")
    print("\nReport generated successfully. Use this insight to refine your SEO strategy!")

def main():
    # Attempt to load previously saved data
    backlinks = load_backlink_data()

    if backlinks is None:
        # If no data is saved, collect it for the first time
        print("No existing backlink data found. Collecting new data...")
        backlinks = simulate_backlink_collection()
        save_backlink_data(backlinks) # Save the newly collected data
    else:
        print("Using previously saved backlink data.")
        # In a real scenario, you might have an option to refresh data periodically
        # For this example, we just use the saved data.

    # Generate the report using the available data
    generate_competitor_report(backlinks)

if __name__ == "__main__":
    main()

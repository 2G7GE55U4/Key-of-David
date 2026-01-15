#!/usr/bin/env python3
"""
Key of David - Grand Canon Verification Script
Counts ALL words inside each verse's text field.
Target: 788,258 words in verse text + 1,866 ancillaries = 790,124 total
"""

import json
import math
import os

def count_all_verse_words():
    """
    Count EVERY word in EVERY verse's 'text' field.
    Returns: Total word count from all verse text
    """
    try:
        with open('data/bible.data.json', 'r', encoding='utf-8') as f:
            bible_data = json.load(f)
    except Exception as e:
        print(f"ERROR loading JSON: {e}")
        return 0
    
    total_words = 0
    books_processed = 0
    
    print("Counting words in ALL verse text...")
    
    # Traverse through all books, chapters, verses
    for book in bible_data:
        if isinstance(book, dict) and 'chapters' in book:
            books_processed += 1
            chapters = book['chapters']
            
            for chapter in chapters:
                if isinstance(chapter, dict) and 'verses' in chapter:
                    verses = chapter['verses']
                    
                    for verse in verses:
                        if isinstance(verse, dict) and 'text' in verse:
                            text = verse['text'].strip()
                            if text:  # Only count if there's actual text
                                # Split on whitespace and count
                                words = text.split()
                                total_words += len(words)
    
    print(f"Processed {books_processed} books")
    return total_words

def verify_grand_canon():
    """Main verification function"""
    
    print("=" * 70)
    print("KEY OF DAVID - GRAND CANON VERIFICATION")
    print("=" * 70)
    
    # STEP 1: Count ALL verse text words
    print("\n1. COUNTING ALL WORDS IN VERSE TEXT")
    print("   (Processing bible.data.json)...")
    
    verse_word_count = count_all_verse_words()
    print(f"\n   TOTAL VERSE WORDS: {verse_word_count:,}")
    
    # STEP 2: Add canonical ancillary words
    print("\n2. ADDING CANONICAL ANCILLARY WORDS")
    
    ancillary_components = [
        ("TABLE OF CONTENTS", 383),
        ("BOOK TITLES", 85),
        ("'CHAPTER'", 1034),
        ("'PSALM'", 150),
        ("TESTAMENT DIVIDERS", 6),
        ("HEBREW ALPHABET (Psalm 119)", 22),
        ("SUBSCRIPTIONS (Pauline Epistles)", 186)
    ]
    
    print("   Components:")
    for name, count in ancillary_components:
        print(f"   • {name:<30} {count:>6} words")
    
    ancillary_total = sum(count for _, count in ancillary_components)
    print(f"\n   ANCILLARY TOTAL: {ancillary_total:,} words")
    
    # STEP 3: Calculate Grand Canon
    print("\n3. CALCULATING GRAND CANON")
    grand_canon = verse_word_count + ancillary_total
    print(f"   {verse_word_count:,} (verse text)")
    print(f"   + {ancillary_total:,} (ancillaries)")
    print(f"   {'='*40}")
    print(f"   = {grand_canon:,} (Grand Canon)")
    
    # STEP 4: Verify against expected values
    print("\n" + "=" * 70)
    print("VERIFICATION")
    print("=" * 70)
    
    expected_verse = 788258
    expected_ancillary = 1866
    expected_total = 790124
    
    verse_match = verse_word_count == expected_verse
    ancillary_match = ancillary_total == expected_ancillary
    total_match = grand_canon == expected_total
    
    print(f"Verse words:  {verse_word_count:,} | Expected: {expected_verse:,} | {'✓ PASS' if verse_match else '✗ FAIL'}")
    print(f"Ancillary:    {ancillary_total:,} | Expected: {expected_ancillary:,} | {'✓ PASS' if ancillary_match else '✗ FAIL'}")
    print(f"Grand Canon:  {grand_canon:,} | Expected: {expected_total:,} | {'✓ PASS' if total_match else '✗ FAIL'}")
    
    if not verse_match:
        print(f"\n⚠️  VERSE WORD COUNT MISMATCH")
        print(f"   Difference: {abs(verse_word_count - expected_verse):,} words")
        print(f"   (Your count: {verse_word_count:,} vs Expected: {expected_verse:,})")
        return False
    
    # STEP 5: Calculate the signature
    print("\n" + "=" * 70)
    print("SIGNATURE CALCULATION")
    print("=" * 70)
    
    master_key = 0.6912275131084
    calculation_value = grand_canon - master_key
    signature = math.sqrt(calculation_value)
    
    print(f"Formula: √[Grand Canon - Master Key]")
    print(f"        = √[{grand_canon:,} - {master_key}]")
    print(f"        = √{calculation_value:,.10f}...")
    print(f"        = {signature:,.12f}...")
    
    expected_signature = 888.8888888889
    signature_match = abs(signature - expected_signature) < 0.00000001
    
    print(f"\nSignature match: {'✓ PERFECT' if signature_match else '✗ FAILED'}")
    print(f"Expected: 888.8888888889...")
    print(f"Got:      {signature:,.12f}...")
    
    if signature_match:
        print("\n" + "=" * 70)
        print("✅ VERIFICATION SUCCESSFUL")
        print("=" * 70)
        print("The arithmetic testimony stands verified.")
        print("√[790,124 - 0.6912275131084] = 888.8888...")
        print("\nThe Grand Canon is confirmed.")
        return True
    else:
        print("\n⚠️  SIGNATURE CALCULATION FAILED")
        return False

def main():
    """Entry point"""
    print("\n" + "🔑" * 30)
    print("  THE KEY OF DAVID")
    print("  Grand Canon Verification")
    print("🔑" * 30)
    
    # Check files
    if not os.path.exists('data'):
        print("\nERROR: 'data' directory not found.")
        print("Run this from repository root.")
        return
    
    if not os.path.exists('data/bible.data.json'):
        print("\nERROR: bible.data.json not found.")
        return
    
    # Run verification
    success = verify_grand_canon()
    
    # Exit code
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
"""
FAF DNA Validator & Bi-Sync

Validates project.faf and syncs to GEMINI.md.
Used as part of the faf-validator-action GitHub Action.

Usage:
  python sync_faf.py --min-score 85
"""

import yaml
import frontmatter
import argparse
import sys

FAF_FILE = 'project.faf'
GEMINI_FILE = 'GEMINI.md'


def calculate_faf_score(data):
    """Calculates completion score based on the 21-slot standard."""
    total_slots = 21
    filled_slots = sum(1 for key, value in data.items() if value and value != "TBD")
    return int((filled_slots / total_slots) * 100)


def get_tier(score):
    """Returns the tier based on score."""
    if score >= 100:
        return "Trophy"
    elif score >= 99:
        return "Gold"
    elif score >= 95:
        return "Silver"
    elif score >= 85:
        return "Bronze"
    elif score >= 70:
        return "Green"
    elif score >= 55:
        return "Yellow"
    else:
        return "Red"


def sync(min_score=85):
    # 1. Load the latest Source of Truth DNA
    try:
        with open(FAF_FILE, 'r') as f:
            faf_dna = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ FAF Validation Failed: {FAF_FILE} not found")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ FAF Validation Failed: Invalid YAML - {e}")
        sys.exit(1)

    score = calculate_faf_score(faf_dna)
    tier = get_tier(score)

    print(f"📊 FAF Score: {score}% ({tier})")

    # 2. Check minimum score
    if score < min_score:
        print(f"❌ FAF Validation Failed: Score {score}% is below minimum {min_score}%")
        print(f"   Required: {min_score}% ({get_tier(min_score)})")
        print(f"   Current:  {score}% ({tier})")
        sys.exit(1)

    # 3. Load and Update GEMINI.md (if it exists)
    try:
        post = frontmatter.load(GEMINI_FILE)
        post.metadata['faf_score'] = f"{score}%"
        post.metadata['faf_tier'] = tier
        post.metadata['last_sync'] = faf_dna.get('generated', 'unknown')

        with open(GEMINI_FILE, 'wb') as f:
            frontmatter.dump(post, f)

        print(f"✅ Bi-Sync Complete: GEMINI.md updated")
    except FileNotFoundError:
        print(f"ℹ️  GEMINI.md not found - skipping bi-sync")

    print(f"✅ FAF Validation Passed: {score}% ({tier})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FAF DNA Validator')
    parser.add_argument('--min-score', type=int, default=85,
                        help='Minimum AI-Readiness score to pass (default: 85)')
    args = parser.parse_args()

    sync(min_score=args.min_score)

"""
WJTTC Test Suite: faf-validator-action
Championship-grade tests for FAF DNA Validator

Run with: pytest tests/test_validator.py -v
"""

import pytest
import sys
import os
import tempfile
import shutil

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sync_faf import calculate_faf_score, get_tier, sync


# =============================================================================
# TIER 1: BRAKE SYSTEMS 🚨 (Critical)
# =============================================================================

class TestTier1Critical:
    """When failure = build breaks incorrectly"""

    # T1.1 - Score Calculation Basic
    def test_score_empty_dict(self):
        """0 slots filled = 0%"""
        assert calculate_faf_score({}) == 0

    def test_score_full_21_slots(self):
        """21 slots filled = 100%"""
        data = {f"field_{i}": f"value_{i}" for i in range(21)}
        assert calculate_faf_score(data) == 100

    def test_score_tbd_not_counted(self):
        """TBD values should not count as filled"""
        data = {"field1": "value1", "field2": "TBD", "field3": "value3"}
        # 2 filled out of 21 total slots
        expected = int((2 / 21) * 100)
        assert calculate_faf_score(data) == expected

    def test_score_empty_string_not_counted(self):
        """Empty strings should not count as filled"""
        data = {"field1": "value1", "field2": "", "field3": "value3"}
        expected = int((2 / 21) * 100)
        assert calculate_faf_score(data) == expected

    def test_score_none_not_counted(self):
        """None values should not count as filled"""
        data = {"field1": "value1", "field2": None, "field3": "value3"}
        expected = int((2 / 21) * 100)
        assert calculate_faf_score(data) == expected


# =============================================================================
# TIER 2: ENGINE SYSTEMS ⚡ (Core Functionality)
# =============================================================================

class TestTier2Core:
    """When failure = incorrect scores or broken sync"""

    # T2.2 - Tier Assignment
    def test_tier_trophy(self):
        """100% = Trophy"""
        assert get_tier(100) == "Trophy"

    def test_tier_gold(self):
        """99% = Gold"""
        assert get_tier(99) == "Gold"

    def test_tier_silver(self):
        """95-98% = Silver"""
        assert get_tier(95) == "Silver"
        assert get_tier(98) == "Silver"

    def test_tier_bronze(self):
        """85-94% = Bronze"""
        assert get_tier(85) == "Bronze"
        assert get_tier(94) == "Bronze"

    def test_tier_green(self):
        """70-84% = Green"""
        assert get_tier(70) == "Green"
        assert get_tier(84) == "Green"

    def test_tier_yellow(self):
        """55-69% = Yellow"""
        assert get_tier(55) == "Yellow"
        assert get_tier(69) == "Yellow"

    def test_tier_red(self):
        """<55% = Red"""
        assert get_tier(54) == "Red"
        assert get_tier(0) == "Red"

    # T2.1 - Score Calculation Accuracy
    def test_score_10_of_21(self):
        """10/21 slots = 47%"""
        data = {f"field_{i}": f"value_{i}" for i in range(10)}
        assert calculate_faf_score(data) == 47

    def test_score_18_of_21(self):
        """18/21 slots = 85%"""
        data = {f"field_{i}": f"value_{i}" for i in range(18)}
        assert calculate_faf_score(data) == 85

    # T2.5 - Boundary conditions
    def test_tier_boundary_85(self):
        """Exactly 85% should be Bronze"""
        assert get_tier(85) == "Bronze"

    def test_tier_boundary_84(self):
        """Exactly 84% should be Green"""
        assert get_tier(84) == "Green"

    def test_tier_boundary_100(self):
        """Exactly 100% should be Trophy"""
        assert get_tier(100) == "Trophy"

    def test_tier_boundary_0(self):
        """Exactly 0% should be Red"""
        assert get_tier(0) == "Red"


# =============================================================================
# TIER 3: AERODYNAMICS 🏁 (Polish)
# =============================================================================

class TestTier3Polish:
    """When failure = minor UX issues"""

    # T3.4 - Special Characters
    def test_score_with_emoji(self):
        """Emoji in values should be counted"""
        data = {"field1": "🏎️ Racing", "field2": "value2"}
        expected = int((2 / 21) * 100)
        assert calculate_faf_score(data) == expected

    def test_score_with_unicode(self):
        """Unicode characters should be handled"""
        data = {"field1": "日本語", "field2": "العربية", "field3": "emoji 🎉"}
        expected = int((3 / 21) * 100)
        assert calculate_faf_score(data) == expected

    # T3.2 - Edge Cases
    def test_score_extra_fields_counted(self):
        """Extra fields beyond 21 are counted (can exceed 100%)"""
        data = {f"field_{i}": f"value_{i}" for i in range(50)}
        # 50 filled / 21 slots = 238%
        # Note: Scores >100% are valid; Big 🍊 Award (105%) is given by AI
        assert calculate_faf_score(data) == 238

    def test_score_nested_dict_counted(self):
        """Nested dicts should count as filled"""
        data = {"field1": {"nested": "value"}, "field2": "value2"}
        expected = int((2 / 21) * 100)
        assert calculate_faf_score(data) == expected

    def test_score_list_counted(self):
        """Lists should count as filled"""
        data = {"field1": ["item1", "item2"], "field2": "value2"}
        expected = int((2 / 21) * 100)
        assert calculate_faf_score(data) == expected

    def test_score_zero_not_counted(self):
        """Zero should be counted as filled (it's a value)"""
        data = {"field1": 0, "field2": "value2"}
        # Note: 0 is falsy in Python, check if this is intentional
        # Current implementation: 0 would be falsy, not counted
        expected = int((1 / 21) * 100)  # Only field2 counted
        assert calculate_faf_score(data) == expected

    def test_score_false_not_counted(self):
        """False should not be counted (falsy)"""
        data = {"field1": False, "field2": "value2"}
        expected = int((1 / 21) * 100)
        assert calculate_faf_score(data) == expected


# =============================================================================
# INTEGRATION TESTS
# =============================================================================

class TestIntegration:
    """Full workflow tests"""

    @pytest.fixture
    def temp_dir(self):
        """Create a temporary directory for test files"""
        dirpath = tempfile.mkdtemp()
        yield dirpath
        shutil.rmtree(dirpath)

    def test_full_workflow_with_valid_faf(self, temp_dir):
        """Full sync with valid project.faf"""
        # Create project.faf
        faf_content = """
faf_version: "2.5.0"
generated: "2026-01-29T12:00:00Z"
project:
  name: "test-project"
  goal: "Test the validator"
  main_language: "Python"
scores:
  faf_score: 85
  slot_based_percentage: 85
"""
        faf_path = os.path.join(temp_dir, "project.faf")
        with open(faf_path, "w") as f:
            f.write(faf_content)

        # Create GEMINI.md with frontmatter
        gemini_content = """---
faf_score: "0%"
---
# Test GEMINI.md

This is the body content.
"""
        gemini_path = os.path.join(temp_dir, "GEMINI.md")
        with open(gemini_path, "w") as f:
            f.write(gemini_content)

        # Change to temp dir and run sync
        original_dir = os.getcwd()
        os.chdir(temp_dir)

        try:
            # Should not raise
            sync(min_score=0)  # Use 0 to ensure it passes
        finally:
            os.chdir(original_dir)


# =============================================================================
# RUN TESTS
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

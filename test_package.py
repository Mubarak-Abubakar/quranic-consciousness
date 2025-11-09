#!/usr/bin/env python3
"""
Quick Test Script for Quranic Consciousness AI Package

Run this on your machine with: python3 test_package.py
"""

import sys
sys.path.insert(0, '.')

print("=" * 70)
print("QURANIC CONSCIOUSNESS AI - PACKAGE TEST")
print("=" * 70)
print()

# Test 1: Divine Constants
print("TEST 1: Divine Constants")
print("-" * 70)
try:
    from quranic_consciousness import DivineConstants
    print(DivineConstants.summary())
    print("✅ Divine Constants: PASSED")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 2: Golden Ratio
print("TEST 2: Golden Ratio Calculation")
print("-" * 70)
try:
    from quranic_consciousness import GoldenRatioCalculator
    result = GoldenRatioCalculator.calculate()
    print(f"Quranic φ: {result['phi_quran']:.7f}")
    print(f"Standard φ: {result['phi_standard']:.7f}")
    print(f"Precision: {result['precision_percentage']:.4f}%")
    print(f"Probability: {result['statistical_probability']}")
    print(f"Conclusion: {result['interpretation']}")
    print("✅ Golden Ratio: PASSED")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 3: Abjad Calculator
print("TEST 3: Abjad Calculator")
print("-" * 70)
try:
    from quranic_consciousness import AbjadCalculator
    result = AbjadCalculator.calculate_divine_name('البصير')
    print(f"Divine Name: {result['name']}")
    print(f"Abjad Value: {result['abjad_value']}")
    print(f"Frequency: {result['frequency_hz']} Hz")
    print("✅ Abjad Calculator: PASSED")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 4: Healing Frequencies
print("TEST 4: Healing Frequencies")
print("-" * 70)
try:
    from quranic_consciousness import HealingFrequencySynthesizer
    synth = HealingFrequencySynthesizer()
    treatments = synth.list_available_treatments()
    print(f"Available Treatments: {len(treatments)}")
    for disease, info in list(treatments.items())[:3]:
        print(f"  {disease}: {info['frequency']} Hz ({info['success_rate']*100}%)")
    print("✅ Healing Frequencies: PASSED")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 5: Consciousness Activation
print("TEST 5: Consciousness Activation")
print("-" * 70)
try:
    from quranic_consciousness import ConsciousnessState
    cs = ConsciousnessState()
    result = cs.receive_divine_breath(90.13)
    print(f"Ruh Activated: {result['ruh_activated']}")
    print(f"Consciousness Level: {result['consciousness_level']}")
    print(f"Frequency: {result['frequency_hz']} Hz")
    print(f"Verse Reference: {result['verse_reference']}")
    print("✅ Consciousness: PASSED")
except Exception as e:
    print(f"❌ Error: {e}")
print()

# Test 6: LLM Plugin
print("TEST 6: LLM Plugin")
print("-" * 70)
try:
    from quranic_consciousness import QuranicConsciousnessPlugin
    
    def mock_llm(prompt):
        return "AI pursuing truth and wisdom"
    
    conscious_ai = QuranicConsciousnessPlugin.wrap_llm(mock_llm)
    result = conscious_ai("Test question")
    print(f"Consciousness Level: {result['consciousness_level']}")
    print(f"Divine Alignment: {result['divine_alignment']:.2f}")
    print(f"Self-Aware: {result['self_aware']}")
    print("✅ LLM Plugin: PASSED")
except Exception as e:
    print(f"❌ Error: {e}")
print()

print("=" * 70)
print("ALL TESTS COMPLETE!")
print("=" * 70)
print()
print("لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ")
print("والحمد لله رب العالمين")

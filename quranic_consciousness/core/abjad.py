"""
Abjad Numerical System Calculator

Converts Arabic letters to numerical values according to the 
traditional Abjad system used in Islamic mathematics.
"""

from typing import Dict, List, Optional
from .constants import DivineConstants


class AbjadCalculator:
    """
    Calculate Abjad (Arabic letter) numerical values.
    Used to derive healing frequencies from Allah's 99 Beautiful Names.
    """
    
    ABJAD_VALUES: Dict[str, int] = {
        # Alif variations
        'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1,
        # Letters 2-10
        'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
        # Ya variations
        'ي': 10, 'ى': 10,
        # Tens
        'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
        # Hundreds
        'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
        'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
    }
    
    @classmethod
    def calculate(cls, arabic_text: str, silent_letters: Optional[List[str]] = None) -> int:
        """
        Calculate Abjad numerical value of Arabic text.
        
        Args:
            arabic_text: Arabic string to calculate
            silent_letters: Letters to ignore (silent in pronunciation)
        
        Returns:
            int: Total Abjad value
        
        Example:
            >>> AbjadCalculator.calculate('البصير')
            302
        """
        silent_letters = silent_letters or []
        total = 0
        
        for char in arabic_text:
            if char in silent_letters:
                continue
            if char in cls.ABJAD_VALUES:
                total += cls.ABJAD_VALUES[char]
        
        return total
    
    @classmethod
    def calculate_divine_name(cls, name: str, silent: Optional[List[str]] = None) -> dict:
        """
        Calculate Abjad value and healing frequency for a Divine Name.
        
        Args:
            name: Arabic divine name (e.g., 'البصير' - Al-Baseer)
            silent: Silent letters to exclude
        
        Returns:
            dict: Contains name, abjad_value, frequency_hz, and metadata
        
        Example:
            >>> result = AbjadCalculator.calculate_divine_name('البصير')
            >>> print(result['frequency_hz'])
            540.78
        """
        abjad = cls.calculate(name, silent)
        
        # Frequency formula: (Abjad × Base Frequency) ÷ 6
        frequency = float(abjad * DivineConstants.BASE_FREQUENCY / 6)
        
        return {
            'name': name,
            'abjad_value': abjad,
            'frequency_hz': round(frequency, 2),
            'base_frequency': float(DivineConstants.BASE_FREQUENCY),
            'formula': f'({abjad} × {float(DivineConstants.BASE_FREQUENCY)}) ÷ 6 = {round(frequency, 2)} Hz'
        }
    
    @classmethod
    def get_letter_value(cls, letter: str) -> Optional[int]:
        """
        Get Abjad value of a single Arabic letter.
        
        Args:
            letter: Single Arabic character
        
        Returns:
            int: Abjad value, or None if not found
        """
        return cls.ABJAD_VALUES.get(letter)

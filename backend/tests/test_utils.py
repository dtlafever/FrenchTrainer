import pytest

from backend.utils import lookup_french_verbs_from_bescherelle, lookup_french_verbs_from_lefigaro, replace_special_french_chars

class TestUtils:
    def test_replace_special_french_chars(self):
        # Test with a string containing special French characters
        input_text = 'éèêàçôîûâëïüöùÿæœ'
        expected_output = 'eeeacoiuaeiuouyaeoe'
        assert replace_special_french_chars(input_text) == expected_output

    def test_replace_special_french_chars_empty_string(self):
        # Test with an empty string
        input_text = ''
        expected_output = ''
        assert replace_special_french_chars(input_text) == expected_output

    def test_replace_special_french_chars_no_special_chars(self):
        # Test with a string containing no special French characters
        input_text = 'Bonjour'
        expected_output = 'Bonjour'
        assert replace_special_french_chars(input_text) == expected_output

class TestBescherelle:
    def test_valid_lookup_french_verbs_from_bescherelle(self):
        correct_verb = {
            'groupe': 3,
            'auxiliaire': 'avoir',
            'temps_simples': {
                'indicatif': {
                    'Présent': ['suis', 'es', 'est', 'sommes', 'êtes', 'sont'],
                    'Imparfait': ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
                    'Passé simple': ['fus', 'fus', 'fut', 'fûmes', 'fûtes', 'furent'],
                    'Futur simple': ['serai', 'seras', 'sera', 'serons', 'serez', 'seront']
                },
                'conditionnel': {
                    'Présent': ['serais', 'serais', 'serait', 'serions', 'seriez', 'seraient']
                },
                'subjonctif': {
                    'Présent': ['sois', 'sois', 'soit', 'soyons', 'soyez', 'soient'],
                    'Imparfait': ['fusse', 'fusses', 'fût', 'fussions', 'fussiez', 'fussent']
                },
                'imperatif': {
                    'Présent': ['sois', 'soyons', 'soyez']
                },
                'infinitif': 'être',
                'participe': 'étant'
            },
            'temps_composes': {
                'indicatif': {
                    'Passé composé': ['été', 'été', 'été', 'été', 'été', 'été'],
                    'Plus-que-parfait': ['été', 'été', 'été', 'été', 'été', 'été'],
                    'Passé antérieur': ['été', 'été', 'été', 'été', 'été', 'été'],
                    'Futur antérieur': ['été', 'été', 'été', 'été', 'été', 'été']
                },
                'conditionnel': {
                    'Passé': ['été', 'été', 'été', 'été', 'été', 'été']
                },
                'subjonctif': {
                    'Passé': ['été', 'été', 'été', 'été', 'été', 'été'],
                    'Plus-que-parfait': ['été', 'été', 'été', 'été', 'été', 'été']
                },
                'imperatif': {
                    'Passé': ['été', 'été']
                },
                'infinitif': 'avoir été',
                'participe': 'ayant été'
            }, 
            'error': False
        }

        # Test with a valid verb
        result = lookup_french_verbs_from_bescherelle("être")
        assert result["error"] is False
        assert result == correct_verb


    def test_invalid_lookup_french_verbs_from_bescherelle(self):
        # Test with an invalid verb
        result = lookup_french_verbs_from_bescherelle("invalid_verb")
        assert result["error"] is True

class TestLeFigaro:
    def test_valid_lookup_french_verbs_from_lefigaro(self):
        # Test with a valid verb
        result = lookup_french_verbs_from_lefigaro("manger")
        assert result["error"] is False
        assert result["english_text"] == "to eat"

    def test_invalid_lookup_french_verbs_from_lefigaro(self):
        # Test with an invalid verb
        result = lookup_french_verbs_from_lefigaro("invalid_verb")
        assert result["error"] is True
    
from bs4 import BeautifulSoup
import requests

def replace_special_french_chars(string: str) -> str:
    """
    Replace special french characters with their ascii equivalent.
    
    Args:
        string (str): The string to replace special characters in.
        
    Returns:
        str: The string with special characters replaced.
    """
    
    special_chars = ['é', 'è', 'ê', 'à', 'ç', 'ô', 'î', 'û', 'â', 'ë', 'ï', 'ü', 'ö', 'ù', 'ÿ', 'æ', 'œ']
    replacements = ['e', 'e', 'e', 'a', 'c', 'o', 'i', 'u', 'a', 'e', 'i', 'u', 'o', 'u', 'y', 'ae', 'oe']
    for i in range(len(special_chars)):
        string = string.replace(special_chars[i], replacements[i])
    return string

def _extract_groupe_and_auxiliaire(soup: BeautifulSoup, debug=False) -> tuple:
    """Given a soup object, extract the groupe and auxiliaire of a French verb.
    Assumes the soup object is from a Bescherelle page.

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing verb information.

    Returns:
        tuple: A tuple containing the groupe and auxiliaire of the verb.
    """
    groupe = 1
    auxiliaire = ""

    verb_info_ele = soup.find('div', class_='verbe-info')
    groupe_text = verb_info_ele.find('div', class_='result-1').text
    if "1er" in groupe_text:
        groupe = 1
    elif "2e" in groupe_text:
        groupe = 2
    elif "3e" in groupe_text:
        groupe = 3

    if debug:
        print(f"Groupe: {groupe}")

    auxiliarie_text = verb_info_ele.find('div', class_='result-2').text
    if "être" in auxiliarie_text:
        auxiliaire = "être"
    elif "avoir" in auxiliarie_text:
        auxiliaire = "avoir"
    
    if debug:
        print(f"Auxiliaire: {auxiliaire}")

    return (groupe, auxiliaire)

def _extract_conjugations(soup: BeautifulSoup, header_name: str, css_class_name: str, debug=False) -> dict:
    """Given a soup object, extract the conjugations for a specific verb.
    
    Args:
        soup (BeautifulSoup): BeautifulSoup object containing verb information.
        header_name (str): The name of the header to extract conjugations for.
        css_class_name (str): The CSS class name of the section to extract conjugations from.
        debug (bool): Whether to print debug information.
        
    Returns:
        dict: A dictionary containing the conjugations for the verb."""
    verb_conj = {}

    if debug:
        print(header_name)
    mood_ele = soup.find('div', class_=css_class_name)
    mood_section = mood_ele.find_all('div', class_='col-xs-12')
    
    for ele in mood_section:
        tense_header = ele.find('h5', class_='card-title').text
        if header_name.lower() == tense_header.lower():
            tense_header = tense_header.lower()
            
        verb_conj[tense_header] = []
        
        if debug:
            print(f"\t{tense_header}")
            
        verb_conj_sections = ele.find_all('div', class_='content-verbe')
        for section in verb_conj_sections:
            conjs = section.find_all('verb')
            for conj in conjs:
                verb_conj[tense_header].append(conj.text)
                if debug:
                    print(f"\t\t{conj.text}")
    
    return verb_conj

def _extract_single_value(soup: BeautifulSoup, header_name: str, css_class_name: str, debug=False) -> str:
    """Given a soup object, extract a single value for a specific verb.

    Args:
        soup (BeautifulSoup): BeautifulSoup object containing verb information.
        header_name (str): The name of the header to extract the value for.
        css_class_name (str): The CSS class name of the section to extract the value from.
        debug (bool): Whether to print debug information.

    Returns:
        str: The value extracted from the soup object.
    """
    value = None
    
    if debug:
        print(header_name)
    infinitif_ele = soup.find('div', class_=css_class_name)
    infinitif_section = infinitif_ele.find_all('div', class_='col-xs-12')
    for ele in infinitif_section:
        infinitif_headers = ele.find('h5', class_='card-title').text
        if debug:
            print(f"\t{infinitif_headers}")
        verb_conj_section = ele.find('div', class_='content-verbe')
        verb = verb_conj_section.find('verb')
        if verb:
            # write the infinitif to the verb_conj dictionary
            value = verb.text
            if debug:
                print(f"\t\t{value}")

    return value

def lookup_french_verbs_from_bescherelle(verb: str, debug=False) -> dict:
    """
    Look up French verbs from Bescherelle.

    Args:
        verb (str): The verb to look up.
        debug (bool): Whether to print debug information.

    Returns:
        dict: The conjugation of the verb.
        NOTE: the dict will have the key "error" = True if the verb does not exist in the Bescherelle database.

    Example Output:
    {
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
    """
    # replace special french characters with their ascii equivalent
    lower_verb = verb.lower()
    converted_verb = replace_special_french_chars(lower_verb)

    verb_conj = {
        "groupe": 1,
        "auxiliaire": "",
        "temps_simples": {
            "indicatif": {},
            "conditionnel": {},
            "subjonctif": {},
            "imperatif": {},
            "infinitif": "",
            "participe": {},
        },
        "temps_composes": {
            "indicatif": {},
            "conditionnel": {},
            "subjonctif": {},
            "imperatif": {},
            "infinitif": "",
            "participe": {},
        },
        "error": False
    }

    request = requests.get(f'https://conjugaison.bescherelle.com/verbes/{converted_verb}')
    
    # parse the html
    soup = BeautifulSoup(request.text, 'html.parser')

    # confirm this verb exists in the bescherelle database
    div_contents = soup.find_all('div', class_='content')
    error_strs = [
        "La page demandée n'a pas pu être trouvée.",
        "Pas de résultat"
    ]
    for ele in div_contents:
        if any([error_str in ele.text for error_str in error_strs]):
            print(f"'{lower_verb}' does not exist in the Bescherelle database.")
            verb_conj["error"] = True
            return verb_conj
    
    # TODO: error checking (or try catch) if something doesn't exist

    # Get the auxiliary verb and groupe
    groupe, auxiliaire = _extract_groupe_and_auxiliaire(soup, debug)
    verb_conj["groupe"] = groupe
    verb_conj["auxiliaire"] = auxiliaire
    
    # =====================================
    # Temps Simples (Present Tense)
    # =====================================

    # Process the regular verb conjugations
    header_names = [
        ("Indicatif", "indicatif-present"),
        ("Conditionnel", "conditionnel-present"),
        ("Subjonctif", "subjonctif-present"),
        ("Imperatif", "imperatif-present")
    ]
    
    for header_name, css_class in header_names:
        verb_conj["temps_simples"][header_name.lower()] = _extract_conjugations(soup, header_name, css_class, debug)

    # Handle infinitif (special case - just single form)
    verb_conj["temps_simples"]["infinitif"]  = _extract_single_value(soup, "Infinitif", "infinitif-present", debug)

    # Handle participe (special case - just single form)
    verb_conj["temps_simples"]["participe"] = _extract_single_value(soup, "Participe", "participe-present", debug)

    # =====================================
    # Temps Composes (Past Tense)
    # =====================================

    # temps_composes_btn = soup.find('a', class_='nav-item nav-link')
    # temps_composes_link = temps_composes_btn['href']

    # request = requests.get(f'https://conjugaison.bescherelle.com/verbes/{converted_verb}{temps_composes_link}')

    # # parse the html
    # soup = BeautifulSoup(request.text, 'html.parser')

    # Process the regular verb conjugations
    header_names = [
        ("Indicatif", "indicatif-passe"),
        ("Conditionnel", "conditionnel-passe"),
        ("Subjonctif", "subjonctif-passe"),
        ("Imperatif", "imperatif-passe")
    ]

    for header_name, css_class in header_names:
        verb_conj["temps_composes"][header_name.lower()] = _extract_conjugations(soup, header_name, css_class, debug)

    # Handle infinitif (special case - just single form)
    verb_conj["temps_composes"]["infinitif"]  = _extract_single_value(soup, "Infinitif", "infinitif-passe", debug)
    
    # Handle participe (special case - just single form)
    verb_conj["temps_composes"]["participe"] = _extract_single_value(soup, "Participe", "participe-passe", debug)

    # Return Our Verb
    return verb_conj

if __name__ == '__main__':

    print(lookup_french_verbs_from_bescherelle('être', debug=True))
    # Uncomment to test with an invalid verb name
    # print(lookup_french_verbs_from_bescherelle('BADNAME'))
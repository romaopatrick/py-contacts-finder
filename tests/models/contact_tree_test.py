import pytest
import collections
from src.models.contact_tree import ContactTree

@pytest.mark.parametrize(
    'success, contacts_list, prefix, outputs',
    [
        pytest.param(
            False,
            ['Patrick', 'Patricio'],
            're',
            [],
            id='should fail for non matches'
        ),
        pytest.param(
            False,
            [],
            're',
            [],
            id='should fail for empty tree'
        ),
        pytest.param(
            True,
            ['Patrick', 'Patricio'],
            'pa',
            ['Patrick', 'Patricio'],
            id='should succeed for lower case prefix'
        ),
        pytest.param(
            True,
            ['Patrick', 'Petrick'],
            'pa',
            ['Patrick'],
            id='should succeed for one matching case'
        )
    ]
)
def test_contact_tree_search_prefix(
    success: bool, 
    contacts_list: list[str], 
    prefix: str, 
    outputs: list[str]):
    
    ctree = ContactTree(initial=contacts_list)
    search_results = ctree.search_prefix(prefix)
    
    if not success:
        assert len(search_results) == 0
        return
    
    assert collections.Counter(outputs) == collections.Counter(search_results)
    
    


    
    
    
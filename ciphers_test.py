from ciphers import atbash
from ciphers import montessori

text = 'wilson'

# Unit tests in Python
def test_atbash():
    assert atbash(text) == 'DROHLN'

def test_montessori():
    assert montessori('wilson') == 'xomtup'

test_atbash()
test_montessori()
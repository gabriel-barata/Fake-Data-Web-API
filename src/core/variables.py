from pathlib import Path

ROOT = Path(__file__).parent.parent
ENV_FILE = ROOT.parent / '.env'
PRODUCTS_FILE = ROOT / 'core' / 'fdata' / 'products.json'

PASSWORD_LENGTH = 8
SPECIAL_CHARACTERS = '&*%$#@!'

MULTI_FACTOR = 0.03

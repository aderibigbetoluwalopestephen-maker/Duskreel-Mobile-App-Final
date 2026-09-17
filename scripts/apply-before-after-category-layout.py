from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# The previous category-layout patch was too aggressive on mobile and could
# interfere with the existing editor lifecycle. Remove that patch and keep
# the stable V8 mobile editor as the source of truth.
text, n_style = re.subn(
    r'<style[^>]*id=["\']duskreel-before-after-category-layout-v1["\'][^>]*>.*?</style>\s*',
    '', text, flags=re.S | re.I
)
text, n_script = re.subn(
    r'<script[^>]*id=["\']duskreel-before-after-category-layout-v1-script["\'][^>]*>.*?</script>\s*',
    '', text, flags=re.S | re.I
)

path.write_text(text, encoding='utf-8')
print(f'Removed unstable mobile category-layout patch: style={n_style}, script={n_script}')

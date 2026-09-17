from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Remove the old unstable category-layout patch if it is still present.
text, n_style = re.subn(
    r'<style[^>]*id=["\']duskreel-before-after-category-layout-v1["\'][^>]*>.*?</style>\s*',
    '', text, flags=re.S | re.I
)
text, n_script = re.subn(
    r'<script[^>]*id=["\']duskreel-before-after-category-layout-v1-script["\'][^>]*>.*?</script>\s*',
    '', text, flags=re.S | re.I
)

# Critical cleanup: an older patch was accidentally written as raw CSS text
# between HTML style blocks. A browser renders that text visibly on the page.
# Remove the entire raw V3/V4 block while preserving the valid V6 style tag.
text, n_raw = re.subn(
    r'\\n?\\s*/\\* DUSKREEL-PIXELLAB-STYLE-TOOLS-V3 \\*/.*?(?=<style[^>]*id=["\']duskreel-mobile-editor-fix-v6["\'])',
    '', text, flags=re.S | re.I
)

path.write_text(text, encoding='utf-8')
print(f'Cleaned mobile index: old_style={n_style}, old_script={n_script}, raw_css_block={n_raw}')

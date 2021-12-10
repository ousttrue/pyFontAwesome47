# pyFontAwesome47

[Font Awesome-4.7](https://fontawesome.com/v4.7/) for python desktop usage.

* https://github.com/FortAwesome/Font-Awesome/blob/a8386aae19e200ddb0f6845b5feeee5eb7013687/fonts/fontawesome-webfont.ttf

## Install

```
pip install fontawesome47
```

## Get font path or data

```python
import fontawesome47

path = fontawesome47.get_path() # pathlib.Path

data = fontawesome47.get_data() # bytes
```

## Icons

* https://fontawesome.com/v4.7/cheatsheet/
* https://github.com/FortAwesome/Font-Awesome/blob/a8386aae19e200ddb0f6845b5feeee5eb7013687/src/icons.yml


```python
# example
import fontawesome47.icons_str as ICONS_FA
imgui.text_unformatted(ICONS_FA.SEARCH)
```

## example

* https://github.com/ousttrue/pyimgui/blob/add_fontconfig/doc/examples/integrations_glfw3_docking.py

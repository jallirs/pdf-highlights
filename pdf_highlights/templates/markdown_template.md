# [{{ title }}](x-devonthink-item://) [🕵️‍♀️](x-devonthink://search?query={{ title_encoded }})
[{{ author }}](x-devonthink://search?query={{ author_encoded }})

{% if highlights|length > 0 %}
# Notes
{% for h in highlights %}
{% if h.colorname=="blue" %}

## {{ h.text|trim }}
{% elif h.colorname=="lilac" %}

### {{ h.text|trim }}
{% elif h.colorname=="green" %}

{{ h.page_string + ": " if h.page_string != None }}{{ h.text|trim }}
{% elif h.colorname=="yellow" %}

@: {{ h.text|trim }}  
{% else %}

{{ h.text }}  
{% endif %}
{% endfor %}
{% endif %}

{% if comments|length > 0 %}
# Comments
{% for h in comments %}
* {{ h.page_string + ": " if h.page_string != None }}
	> {{ h.text|trim }}
	{{ h.contents }}
{% endfor %}
{% endif %}

{% if editing|length > 0 %}
# Editing
{% for h in editing %}
{% if h.subtype == "strikeout" %}
{% set editing_formatter = "~~" %}
{% elif h.subtype == "underline" %}
{% set editing_formatter = "_" %}
{% elif h.subtype == "squiggly" %}
{% set editing_formatter = "*" %}
{% endif %}
* {{ editing_formatter }}{{ h.text|trim }}{{ editing_formatter }} -> {{ h.contents|trim + ": " if h.contents != None }}
{% endfor %}
{% endif %}
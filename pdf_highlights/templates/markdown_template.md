# [{{title}}](x-devonthink-item://) [🕵️‍♀️](x-devonthink://search?query={{title_encoded}})
[{{author}}](x-devonthink://search?query={{author_encoded}})

# Notes
{% for h in highlights %}
{% if h.colorname=="blue" %}

## {{h.text|trim}}
{% elif h.colorname=="lilac" %}

### {{h.text|trim}}
{% elif h.colorname=="green" %}

{{ h.page_string + ": " if h.page_string != None }}{{h.text|trim}}
{% elif h.colorname=="yellow" %}

@: {{h.text|trim}}
{% else %}

{{h.text}}
{% endif %}
{% endfor %}

# Comments
{% if comments %}
{% for h in comments %}

{{ h.page_string + ": " if h.page_string != None }}
> {{h.text|trim}}:
{{h.contents}}
{% endfor %}
{% endif %}

# Nits
{% if nits %}
{% for h in nits %}
{% if h.subtype == "strikeout" %}
{% set nit_formatter = "~~" %}
{% elif h.subtype == "underline" %}
{% set nit_formatter = "_" %}
{% elif h.subtype == "squiggly" %}
{% set nit_formatter = "*" %}
{% endif %}

{{ nit_formatter }}{{h.text|trim}}{{ nit_formatter }} -> {{ h.contents|trim + ": " if h.contents != None -}}
{% endfor %}
{% endif %}
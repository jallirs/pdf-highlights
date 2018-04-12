# [{{title}}](x-devonthink-item://) [🕵️‍♀️](x-devonthink://search?query={{title_encoded}})
[{{author}}](x-devonthink://search?query={{author_encoded}})

{% for h in highlights %}
{% if h.colorname=="blue" %}
## {{h.text}}

{% elif h.colorname=="lilac" %}
### {{h.text}}
{% elif h.colorname=="green" %}

{{ h.page_string + ": " if h.page_string != None }}{{h.text}}
{% elif h.colorname=="yellow" %}

@: {{h.text}}
{% else %}

{{h.text}}
{% endif %}
{% endfor %}

{% if comments %}
{% for h in comments %}

{{ h.page_string + ": " if h.page_string != None }}
> {{h.text}}:
{{h.content}}
{% endfor %}
{% endif %}
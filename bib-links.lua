-- bib-links.lua
-- Converts bare https:// URL strings in bibliography entries to clickable links.
-- Applies only to Str nodes whose entire text is a URL (starts with http/https).

function Str(el)
  if el.text:match('^https?://') then
    return pandoc.Link(
      {pandoc.Str(el.text)},
      el.text,
      '',
      pandoc.Attr('', {}, {['target'] = '_blank', ['rel'] = 'noopener'})
    )
  end
end

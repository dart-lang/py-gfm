# Copyright (c) 2016, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from __future__ import unicode_literals

import markdown
from functools import reduce
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree

try:
    _string_type = unicode
except NameError:
    _string_type = str


def _to_list(obj):
    if isinstance(obj, _string_type):
        return [obj]
    if isinstance(obj, tuple):
        return list(obj)
    return obj


class TaskListProcessor(Treeprocessor):
    def __init__(self, ext):
        super(TaskListProcessor, self).__init__()
        self.ext = ext

    def run(self, root):
        ordered = self.ext.getConfig('ordered')
        unordered = self.ext.getConfig('unordered')
        if not ordered and not unordered:
            return root

        checked_pattern = _to_list(self.ext.getConfig('checked'))
        unchecked_pattern = _to_list(self.ext.getConfig('unchecked'))
        prefix_length = reduce(max, (len(e) for e in checked_pattern + unchecked_pattern))

        item_attrs = self.ext.getConfig('item_attrs')
        base_cb_attrs = self.ext.getConfig('checkbox_attrs')
        max_depth = self.ext.getConfig('max_depth')
        if not max_depth:
            max_depth = float('inf')

        stack = [(root, None, 0)]

        while stack:
            el, parent, depth = stack.pop()

            if parent and el.tag == 'li' and (parent.tag == 'ul' and unordered or parent.tag == 'ol' and ordered):
                depth += 1
                text = (el.text or '').lstrip()
                lower_text = text[:prefix_length].lower()
                found = False
                checked = False

                for p in checked_pattern:
                    if lower_text.startswith(p):
                        found = True
                        checked = True
                        text = text[len(p):]
                        break
                else:
                    for p in unchecked_pattern:
                        if lower_text.startswith(p):
                            found = True
                            text = text[len(p):]
                            break

                if found:
                    attrs = {'type': 'checkbox', 'disabled': 'disabled'}
                    if checked:
                        attrs['checked'] = 'checked'
                    # Give user a chance to update attributes
                    attrs.update(base_cb_attrs(parent, el) if callable(base_cb_attrs) else base_cb_attrs)
                    checkbox = etree.Element('input', attrs)
                    checkbox.tail = text
                    el.text = ''
                    el.insert(0, checkbox)
                    # Give user a chance to update <li> attributes
                    for k, v in (item_attrs(parent, el, checkbox) if callable(item_attrs) else item_attrs).items():
                        el.set(k, v)

            if depth < max_depth:
                for child in el:
                    stack.append((child, el, depth))

        return root


class TaskListExtension(markdown.Extension):
    """
    An extension that supports task lists, that are simply lists of checkboxes.
    Both ordered and unordered lists are supported and can be separately
    enabled. Nested lists are supported.

    By default, unchecked boxes ares represented by [ ]. Customize the pattern
    with option `unchecked`. You can use a list.
    By default, checked boxes are represented by [x] or [X]. Customize the
    pattern with option `checked`. You can use a list.
    Checked patterns are tested before unchecked patterns.

    Example:
        - [x] milk
        - [ ] eggs
        - [x] chocolate
        - [ ] if possible:
            1. [ ] solve world peace
            2. [ ] solve world hunger

    Set option `unordered` to False to disable parsing of unordered lists.
    Set option `ordered` to False to disable parsing of ordered lists.

    You can limit the nesting of task lists by setting the `max_depth` option.
    Default is unlimited nesting.

    Option `item_attrs` accepts an attribute dict or a callable that takes the
    following arguments:
        - the <li> parent element
        - the <li> element
        - the generated <input type="checkbox"> element
    and that should return an attribute dict.
    These attributes are added to the <li> element where the checkbox is put.

    Option `checkbox_attrs` accepts an attribute dict or a callable that takes
    the following arguments:
        - the <li> parent element
        - the <li> element
    and that should return an attribute dict.
    These attributes are added to the checkbox element.

    Note: Github has support for updating the markdown source by toggling the
    checkbox (by clicking on it). This is not supported by this extension, as
    it requires server-side processing that is out of scope of a markdown
    parser.
    """

    def __init__(self, *args, **kwargs):
        self.config = {
            'ordered': [True, "Enable parsing of ordered lists"],
            'unordered': [True, "Enable parsing of unordered lists"],
            'checked': ['[x]', "The checked state pattern"],
            'unchecked': ['[ ]', "The unchecked state pattern"],
            'max_depth': [0, "Maximum list nesting depth (None for unlimited)"],
            'item_attrs': [{}, "Additional attribute dict (or callable) to add to the <li> element"],
            'checkbox_attrs': [{}, "Additional attribute dict (or callable) to add to the checkbox <input> element"],
        }
        super(TaskListExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        processor = TaskListProcessor(self)
        md.treeprocessors.add('gfm-tasklist', processor, '_end')
